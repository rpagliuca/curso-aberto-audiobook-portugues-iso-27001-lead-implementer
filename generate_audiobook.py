#!/usr/bin/env python3
"""
Gera MP3s de um roteiro em Markdown usando edge-tts.

    python generate_audiobook.py           # os 6 episódios (iso27001-roteiro-audio.md)
    python generate_audiobook.py extras    # os 5 capítulos extras (iso27001-roteiro-extras.md)

Estratégia de pronúncia:
  - Siglas PT-BR → pontuadas (TI → T.I.) para soletramento.
  - Termos ingleses → transcrição fonética PT-BR para pronúncia aceitável
    com voz pt-BR-AntonioNeural.
"""
import re
import asyncio
import os
import sys

try:
    import edge_tts
except ImportError:
    print("Erro: edge-tts não instalado.")
    sys.exit(1)

VOICE = "pt-BR-AntonioNeural"
RATE  = "+10%"
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "docs")
# roteiro → (fonte, padrão do título "## ...", prefixo do arquivo, cláusula 7.5 lida "7 ponto 5")
ROTEIROS = {
    "audiobook": ("iso27001-roteiro-audio.md",  r"Episódio \d+ — .+", "",  False),
    "extras":    ("iso27001-roteiro-extras.md", r"Extra \d+ — .+",    "x", True),
}

# ---------------------------------------------------------------------------
# Siglas PT-BR — do mais longo ao mais curto para evitar substituições
# parciais (SGSI antes de SI).
# ---------------------------------------------------------------------------
ACRONYM_MAP = [
    # Sensível a maiúsculas e palavra inteira: "ia", "cio" e "pás" do português não casam.
    (r'\bPCI DSS\b', 'P.C.I. D.S.S.'),
    (r'\bCSA STAR\b', 'C.S.A. istár'),
    (r'\b17021-1\b', '17021 parte 1'),
    (r'\bPECB\b',  'P.E.C.B.'),
    (r'\bIMS2\b',  'I.M.S. dois'),
    # Siglas lidas como palavra, na pronúncia pedida pelo Rafael.
    (r'\bCISO\b',  'cízo'),
    (r'\bSWOT\b',  'suóti'),
    (r'\bPEST\b',  'pésti'),
    (r'\bSaaS\b',  'sás'),
    (r'\bPaaS\b',  'pás'),
    (r'\bIaaS\b',  'i-ás'),
    (r'\bCIO\b',   'ci-ai-ôu'),
    (r'\bSGSI\b',  'S.G.S.I.'),
    (r'\bMTTD\b',  'M.T.T.D.'),
    (r'\bMTTR\b',  'M.T.T.R.'),
    (r'\bOPFT\b',  'O.P.F.T.'),
    (r'\bPDCA\b',  'P.D.C.A.'),
    (r'\bLGPD\b',  'L.G.P.D.'),
    (r'\bGDPR\b',  'G.D.P.R.'),
    (r'\bPTR\b',   'P.T.R.'),
    (r'\bDLP\b',   'D.L.P.'),
    (r'\bTIC\b',   'T.I.C.'),
    (r'\bMFA\b',   'M.F.A.'),
    (r'\bVPN\b',   'V.P.N.'),
    (r'\bSoA\b',   'S.o.A.'),
    (r'\bIEC\b',   'I.E.C.'),
    (r'\bSOC\b',   'S.O.C.'),
    (r'\bACS\b',   'A.C.S.'),
    (r'\bSSL\b',   'S.S.L.'),
    (r'\bTLS\b',   'T.L.S.'),
    (r'\bIAF\b',   'I.A.F.'),
    # ISO: TTS já pronuncia como palavra ("ízo") — sem pontos.
    (r'\bRH\b',    'R.H.'),
    (r'\bTI\b',    'T.I.'),
    (r'\bSI\b',    'S.I.'),
    (r'\bIA\b',    'I.A.'),
    # CIA: TTS já pronuncia como palavra — sem pontos.
]

# ---------------------------------------------------------------------------
# Termos ingleses → transcrição fonética PT-BR.
#
# Regras aplicadas:
#   ph      → f        ("phishing" começa com /f/, não /p/+/h/)
#   -ching  → /ʃ/      ("ch" em pt-BR = /ʃ/, equivale a "sh" inglês)
#   -ware   → -uér     ("w" → "u", evita leitura como /v/)
#   -wall   → -uôl     (idem para "wall")
#   check-  → tchéque- ("ch" inglês = /tʃ/; em pt-BR "tch" produz /tʃ/)
#   back-   → béic-    (vogal inglesa /æ/ → "ei" pt-BR)
#   feed-   → fíd-     (/iː/ → "í")
#   -tch    → -tch     (já produz /tʃ/ no motor pt-BR)
# ---------------------------------------------------------------------------
PHONETIC_MAP = [
    # Mais longos primeiro para evitar substituição parcial
    (r'\bstatement of applicability\b', 'istêiti-mênti ófi aplí-cabíliti'),
    (r'\bsurveillance audit\b',         'sãrvêilenci audíti'),
    (r'\bLead Implementer\b',           'líd implemênter'),
    (r'\bbusiness case\b',              'bíznes quêis'),
    (r'\bKirkpatrick\b',     'Kêrk-pétrik'),
    (r'\bconfidentiality\b', 'confidênciáliti'),
    (r'\bavailability\b',    'avêilabíliti'),
    (r'\bransomware\b',      'rânsomuér'),
    (r'\bfirewall\b',        'fáier-uôl'),
    (r'\bchecklist\b',       'tchéque-líste'),
    (r'\bintegrity\b',       'intégriti'),
    (r'\bmalware\b',         'mal-uér'),
    (r'\bsoftware\b',        'sóftuér'),
    (r'\bhardware\b',        'rárd-uér'),
    (r'\bfeedback\b',        'fídbéque'),
    (r'\bphishing\b',        'fíching'),
    (r'\bpatches\b',         'pétches'),
    (r'\bbackup\b',          'bêcápi'),
    (r'\bpatch\b',           'pétch'),
    (r'\bbackdoor\b',        'béc-dór'),
    (r'\bPorter\b',          'Pórter'),
    (r'\bshould\b',          'chúd'),
    (r'\bshall\b',           'chél'),
    (r'\blog\b',             'lóg'),
    # Verbos da norma (Extra 4); palavra inteira, não existem em português.
    (r'\bmay\b',             'mêi'),
    (r'\bcan\b',             'quén'),
    # Correções de acentuação PT-BR
    (r'\bperceba\b',         'percêba'),
]


def apply_acronyms(text: str) -> str:
    for pattern, replacement in ACRONYM_MAP:
        text = re.sub(pattern, replacement, text)
    return text


def apply_phonetics(text: str) -> str:
    for pattern, replacement in PHONETIC_MAP:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text


def clean_for_tts(text: str, clausula_com_ponto: bool = False) -> str:
    # 1. Strip markdown
    text = re.sub(r"^#{1,6}\s+(.+)$", r"\1.", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"^[-*]{3,}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()
    if clausula_com_ponto:                                   # cláusula 7.5 → "7 ponto 5"
        text = re.sub(r"(?<=\d)\.(?=\d)", " ponto ", text)
    # 2. Siglas PT-BR
    text = apply_acronyms(text)
    # 3. Fonética inglesa
    text = apply_phonetics(text)
    return text


def parse_episodes(path: str, title_re: str = r"Episódio \d+ — .+",
                   clausula_com_ponto: bool = False) -> list[tuple[str, str]]:
    raw = open(path, encoding="utf-8").read()
    pattern = re.compile(rf"^## ({title_re})$", re.MULTILINE)
    positions = [(m.start(), m.group(1)) for m in pattern.finditer(raw)]
    episodes = []
    for i, (start, title) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(raw)
        body = raw[start:end]
        body = re.sub(r"^## .+\n", "", body, count=1)
        body = clean_for_tts(body, clausula_com_ponto)
        if body:
            episodes.append((title, body))
    return episodes


async def generate_all(episodes: list[tuple[str, str]], prefix: str = "") -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tasks = []
    for i, (title, text) in enumerate(episodes, 1):
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower())[:60].strip("-")
        filename = f"{prefix}{i:02d}-{slug}.mp3"
        output_path = os.path.join(OUTPUT_DIR, filename)
        print(f"  [{i:02d}] {filename}  ({len(text.split())} palavras)")
        tasks.append((i, output_path, text, title))

    print(f"\nGerando {len(tasks)} MP3s em paralelo...\n")

    async def render(idx, path, text, title):
        print(f"  ▶ [{idx:02d}] {os.path.basename(path)} ...", flush=True)
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(path)
        size_kb = os.path.getsize(path) // 1024
        print(f"  ✓ [{idx:02d}] {os.path.basename(path)}  {size_kb} KB")

    await asyncio.gather(*[render(i, p, t, title) for i, p, t, title in tasks])
    print(f"\nConcluído! Arquivos em {OUTPUT_DIR}/")


async def main() -> None:
    nome = sys.argv[1] if len(sys.argv) > 1 else "audiobook"
    if nome not in ROTEIROS:
        sys.exit(f"Roteiro desconhecido: {nome} (opções: {', '.join(ROTEIROS)})")
    fonte, title_re, prefix, clausula = ROTEIROS[nome]
    source = os.path.join(BASE_DIR, fonte)
    if not os.path.exists(source):
        print(f"Arquivo não encontrado: {source}")
        sys.exit(1)
    episodes = parse_episodes(source, title_re, clausula)
    if not episodes:
        print("Nenhum episódio encontrado.")
        sys.exit(1)
    if "--texto" in sys.argv:          # só imprime o texto que vai para o TTS (conferência de pronúncia)
        for title, text in episodes:
            print(f"===== {title}\n{text}\n")
        return
    print(f"\nEncontrados {len(episodes)} episódios em {fonte}\n")
    await generate_all(episodes, prefix)


if __name__ == "__main__":
    asyncio.run(main())
