#!/usr/bin/env python3
"""
Gera MP3s do roteiro iso27001-roteiro-audio.md usando edge-tts.

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
SOURCE    = os.path.join(os.path.dirname(__file__), "iso27001-roteiro-audio.md")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "docs")

# ---------------------------------------------------------------------------
# Siglas PT-BR — do mais longo ao mais curto para evitar substituições
# parciais (SGSI antes de SI).
# ---------------------------------------------------------------------------
ACRONYM_MAP = [
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
    # ISO: TTS já pronuncia como palavra ("ízo") — sem pontos.
    (r'\bRH\b',    'R.H.'),
    (r'\bTI\b',    'T.I.'),
    (r'\bSI\b',    'S.I.'),
    # CIA e CISO: TTS já pronuncia como palavra — sem pontos.
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


def clean_for_tts(text: str) -> str:
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
    # 2. Siglas PT-BR
    text = apply_acronyms(text)
    # 3. Fonética inglesa
    text = apply_phonetics(text)
    return text


def parse_episodes(path: str) -> list[tuple[str, str]]:
    raw = open(path, encoding="utf-8").read()
    pattern = re.compile(r"^## (Episódio \d+ — .+)$", re.MULTILINE)
    positions = [(m.start(), m.group(1)) for m in pattern.finditer(raw)]
    episodes = []
    for i, (start, title) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(raw)
        body = raw[start:end]
        body = re.sub(r"^## .+\n", "", body, count=1)
        body = clean_for_tts(body)
        if body:
            episodes.append((title, body))
    return episodes


async def generate_all(episodes: list[tuple[str, str]]) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tasks = []
    for i, (title, text) in enumerate(episodes, 1):
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower())[:60].strip("-")
        filename = f"{i:02d}-{slug}.mp3"
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
    if not os.path.exists(SOURCE):
        print(f"Arquivo não encontrado: {SOURCE}")
        sys.exit(1)
    episodes = parse_episodes(SOURCE)
    if not episodes:
        print("Nenhum episódio encontrado.")
        sys.exit(1)
    print(f"\nEncontrados {len(episodes)} episódios em {os.path.basename(SOURCE)}\n")
    await generate_all(episodes)


if __name__ == "__main__":
    asyncio.run(main())
