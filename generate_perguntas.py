#!/usr/bin/env python3
"""
Gera os capítulos de PERGUNTAS E RESPOSTAS (estilo Pimsleur) a partir de perguntas/*.md.

O texto em perguntas/*.md é o CÓDIGO-FONTE; o MP3 é só artefato. Para revisar conteúdo, leia o .md.

Como o silêncio é feito: o edge-tts não aceita <break> em SSML, então cada trecho (pergunta, resposta,
explicação) vira um áudio separado, é decodificado para PCM e o silêncio entra como amostras zeradas
entre eles. Um único encode no final — sem emenda audível.

Duração do silêncio (padrão Pimsleur: a pausa é dimensionada pela resposta esperada, não fixa):
    pausa = tempo_para_lembrar + FATOR_FALA × duração_da_resposta_falada     (limitada a [MIN, MAX])
Re-perguntas (repetição espaçada dentro do capítulo) usam menos tempo para lembrar.

Uso:  source ~/.venvs/tts/bin/activate && python generate_perguntas.py [p01 p02 ...]   (sem args = todos)
"""
import asyncio, hashlib, html, json, os, re, subprocess, sys
import edge_tts
from generate_audiobook import VOICE, RATE, apply_acronyms, apply_phonetics

BASE   = os.path.dirname(os.path.abspath(__file__))
SRC    = os.path.join(BASE, "perguntas")
OUT    = os.path.join(BASE, "docs")
CACHE  = os.path.join(BASE, ".tts-cache")
INDEX  = os.path.join(OUT, "index.html")
SR     = 24000                       # edge-tts entrega 24 kHz mono

PENSAR_NOVA, PENSAR_REVISAO = 4.0, 2.5     # s para lembrar
FATOR_FALA                  = 1.4          # × duração da resposta curta (fala humana é mais lenta que o TTS)
PAUSA_MIN, PAUSA_MAX        = 5.5, 10.0
GAP_POS_RESPOSTA            = 0.5          # entre resposta curta e explicação
GAP_ENTRE_ITENS             = 1.6
CAUDA_TTS                   = 0.75         # silêncio que o próprio edge-tts já deixa no fim de cada trecho

EXTRA_PHONETIC = [
    (r'\bPimsleur\b', 'Pímsler'), (r'\bcompliance\b', 'complaiânce'), (r'\bstakeholders?\b', 'istêique-rôlders'),
    (r'\bgap analysis\b', 'guépi análise'), (r'\bbusiness case\b', 'bíznes quêis'), (r'\brisk owners?\b', 'rísqui ôuner'),
    (r'\bAnnex SL\b', 'Ânex S.L.'), (r'\bStage\b', 'istêidj'), (r'\bweb\b', 'uéb'), (r'\blogs\b', 'lógs'),
    (r'\blog\b', 'lóg'), (r'\bclear desk\b', 'clír désqui'), (r'\bcloud\b', 'cláud'), (r'\bBYOD\b', 'B.Y.O.D.'),
    (r'\bNDA\b', 'N.D.A.'), (r'\bKPIs?\b', 'K.P.I.'), (r'\bBIA\b', 'B.I.A.'), (r'\bRTO\b', 'R.T.O.'), (r'\bRPO\b', 'R.P.O.'),
    (r'\bNC\b', 'não conformidade'),
]


def tts_text(t: str) -> str:
    t = re.sub(r"\*\*?([^*]+)\*\*?", r"\1", t)
    t = re.sub(r"(?<=\d)\.(?=\d)", " ponto ", t)          # cláusula 6.1.3 → "6 ponto 1 ponto 3"
    t = apply_phonetics(apply_acronyms(t))
    for pat, rep in EXTRA_PHONETIC:
        t = re.sub(pat, rep, t, flags=re.IGNORECASE)
    return t.strip()


# ─── Parser do formato-fonte ────────────────────────────────────────────────
def parse(path):
    ch = {"meta": {}, "abertura": "", "encerramento": "", "itens": []}
    sec, item, by_id = None, None, {}
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if line.startswith("# "):
            ch["titulo"] = line[2:].strip(); continue
        m = re.match(r"^(tipo|dominio|topicos|rotulo):\s*(.+)$", line)
        if m and sec is None:
            ch["meta"][m.group(1)] = m.group(2).strip(); continue
        if line.startswith("## "):
            sec = line[3:].strip().lower(); item = None; continue
        m = re.match(r"^### (=)?\s*(\S+)", line)
        if m:
            if m.group(1):
                if m.group(2) not in by_id: raise SystemExit(f"{path}: re-pergunta de id inexistente: {m.group(2)}")
                item = None; ch["itens"].append({"revisao": True, **{k: by_id[m.group(2)][k] for k in ("id", "P", "R")}})
            else:
                item = {"id": m.group(2), "revisao": False, "P": "", "R": "", "E": ""}
                by_id[item["id"]] = item; ch["itens"].append(item)
            continue
        if sec in ("abertura", "encerramento"):
            ch[sec] = (ch[sec] + " " + line.strip()).strip(); continue
        if item is not None and line.strip():
            m = re.match(r"^([PRE]):\s*(.*)$", line)
            if m: cur = m.group(1); item[cur] = m.group(2).strip(); item["_cur"] = cur
            elif "_cur" in item: item[item["_cur"]] += " " + line.strip()
    for it in ch["itens"]:
        it.pop("_cur", None)
        if not it["P"] or not it["R"]: raise SystemExit(f"{path}: item {it['id']} sem P ou R")
    return ch


# ─── TTS com cache por hash do texto ────────────────────────────────────────
SEM = None
async def synth(text):
    os.makedirs(CACHE, exist_ok=True)
    spoken = tts_text(text)
    key = hashlib.sha1(f"{VOICE}|{RATE}|{spoken}".encode()).hexdigest()
    mp3 = os.path.join(CACHE, key + ".mp3")
    if not os.path.exists(mp3) or os.path.getsize(mp3) < 500:
        async with SEM:
            for attempt in range(4):
                try:
                    await edge_tts.Communicate(spoken, VOICE, rate=RATE).save(mp3 + ".part")
                    os.replace(mp3 + ".part", mp3); break
                except Exception as e:
                    if attempt == 3: raise
                    await asyncio.sleep(2 * (attempt + 1))
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", mp3, "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         check=True, capture_output=True).stdout
    return pcm

def silence(sec): return b"\x00\x00" * int(max(0, sec) * SR)
def dur(pcm): return len(pcm) / 2 / SR


async def build(path):
    ch = parse(path)
    slug = os.path.splitext(os.path.basename(path))[0]
    texts = [ch["abertura"], ch["encerramento"]]
    for it in ch["itens"]:
        texts += [it["P"], it["R"]] + ([it["E"]] if it.get("E") else [])
    uniq = [t for t in dict.fromkeys(texts) if t]
    audio = dict(zip(uniq, await asyncio.gather(*[synth(t) for t in uniq])))

    out, cues = bytearray(), []
    def add(b): out.extend(b)
    if ch["abertura"]: add(audio[ch["abertura"]]); add(silence(1.0))
    for it in ch["itens"]:
        r = audio[it["R"]]
        fala = max(0.5, dur(r) - CAUDA_TTS)
        pausa = (PENSAR_REVISAO if it["revisao"] else PENSAR_NOVA) + FATOR_FALA * fala
        pausa = min(PAUSA_MAX, max(PAUSA_MIN, pausa))
        cue = {"id": it["id"], "revisao": it["revisao"], "t_pergunta": round(dur(out), 2)}
        add(audio[it["P"]]); cue["t_pausa"] = round(dur(out), 2); cue["pausa"] = round(pausa, 1)
        add(silence(pausa - CAUDA_TTS)); cue["t_resposta"] = round(dur(out), 2)
        add(r)
        if it.get("E"): add(silence(GAP_POS_RESPOSTA)); add(audio[it["E"]])
        add(silence(GAP_ENTRE_ITENS)); cues.append(cue)
    if ch["encerramento"]: add(audio[ch["encerramento"]])

    mp3 = os.path.join(OUT, slug + ".mp3")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ac", "1", "-ar", str(SR), "-i", "-",
                    "-c:a", "libmp3lame", "-b:a", "48k", mp3], input=bytes(out), check=True)
    total = dur(out)
    json.dump({"slug": slug, "duracao": round(total, 1), "cues": cues},
              open(os.path.join(OUT, slug + ".cues.json"), "w"), ensure_ascii=False, indent=1)
    novas = sum(1 for i in ch["itens"] if not i["revisao"]); rev = len(ch["itens"]) - novas
    pausas = [c["pausa"] for c in cues]
    print(f"  ✓ {slug}.mp3  {int(total//60)}:{int(total%60):02d}  {novas} perguntas + {rev} revisões  "
          f"pausa média {sum(pausas)/len(pausas):.1f}s (mín {min(pausas)}, máx {max(pausas)})")
    ch.update(slug=slug, duracao=total, novas=novas, rev=rev)
    return ch


# ─── Cards no index.html (entre os marcadores QA:START / QA:END) ────────────
def card(ch, num):
    e = html.escape
    n = 100 + num                                   # id numérico do player: 101, 102… (episódios usam 1–6)
    m = ch["meta"]; d = ch["duracao"]
    seen, lis = set(), []
    for it in ch["itens"]:
        if it["id"] in seen: continue
        seen.add(it["id"])
        lis.append(f'<li><details><summary>{e(it["P"])}</summary><p><strong>{e(it["R"])}</strong> {e(it.get("E",""))}</p></details></li>')
    misto = m.get("tipo", "tema") == "misto"
    return f'''<div class="card" id="card-{n}">
  <div class="card-header">
    <div class="ep-num qa">P{num}</div>
    <div class="card-meta">
      <h2>{e(re.sub(r"^P\d+\s*[—-]\s*", "", ch["titulo"]))}</h2>
      <div class="topics">{e(m.get("topicos", ""))}</div>
    </div>
    <div class="duration">{int(d//60)}:{int(d%60):02d}</div>
  </div>
  <div class="player" data-ep="{n}" data-label="P{num}" data-src="{ch["slug"]}.mp3">
    <button class="pp" aria-label="Tocar ou pausar P{num}">▶</button>
    <input class="seek" type="range" min="0" max="1000" value="0" step="1" aria-label="Posição em P{num}">
    <span class="time">0:00</span>
  </div>
  <div class="skip-row">
    <button class="btn-skip" onclick="skip('audio-{n}',-30)">−30s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',-5)">−5s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',+5)">+5s</button>
    <button class="btn-skip" onclick="skip('audio-{n}',+30)">+30s</button>
  </div>
  <div class="tags">
    <span class="tag {"purple" if misto else ""}">{e(m.get("dominio", "Temas misturados"))}</span>
    <span class="tag green">{ch["novas"]} perguntas</span>
    <span class="tag amber">{ch["rev"]} revisões espaçadas</span>
  </div>
  <div class="actions">
    <button class="btn-toggle" onclick="togglePanel('resumo-{n}',this)">📄 Transcrição — perguntas e respostas</button>
  </div>
  <div class="panel" id="resumo-{n}">
    <div class="panel-inner">
      <div class="resumo-title">Toque na pergunta para ver a resposta</div>
      <ul class="resumo-list qa-list">
        {chr(10).join("        " + l for l in lis).strip()}
      </ul>
    </div>
  </div>
</div>
'''

def update_index(chapters):
    s = open(INDEX, encoding="utf-8").read()
    a, b = s.index("<!-- QA:START -->"), s.index("<!-- QA:END -->")
    body = "\n".join(card(ch, int(re.match(r"p(\d+)", ch["slug"]).group(1))) for ch in chapters)
    open(INDEX, "w", encoding="utf-8").write(s[:a] + "<!-- QA:START -->\n" + body + s[b:])


async def main():
    global SEM
    SEM = asyncio.Semaphore(6)
    want = [a.lower() for a in sys.argv[1:]]
    files = sorted(f for f in os.listdir(SRC) if re.match(r"p\d+.*\.md$", f))
    chapters = []
    for f in files:
        slug = f[:-3]
        if want and not any(slug.startswith(w) for w in want) and os.path.exists(os.path.join(OUT, slug + ".cues.json")):
            # não pedido e já gerado: só relê o fonte para manter o card atualizado
            ch = parse(os.path.join(SRC, f)); cj = json.load(open(os.path.join(OUT, slug + ".cues.json")))
            novas = sum(1 for i in ch["itens"] if not i["revisao"])
            ch.update(slug=slug, duracao=cj["duracao"], novas=novas, rev=len(ch["itens"]) - novas)
        else:
            ch = await build(os.path.join(SRC, f))
        chapters.append(ch)
    update_index(chapters)
    print(f"index.html atualizado com {len(chapters)} capítulo(s) de perguntas.")

if __name__ == "__main__":
    asyncio.run(main())
