#!/usr/bin/env python3
"""Gera o feed de podcast (docs/podcast.xml) com duas faixas únicas: conteúdo e perguntas.

Por que faixa única: num app de podcast, voltar 10 s no começo de um episódio não cai no fim do
anterior. Juntando os capítulos num só MP3, o ±10 s atravessa os capítulos como no player do site,
e cada capítulo vira um marcador (ID3 CHAP dentro do MP3 e podcast:chapters em JSON).

Fonte: os MP3 já gerados em docs/ e os títulos dos cards do docs/index.html. Rode depois de
generate_audiobook.py ou generate_perguntas.py. Requer ffmpeg/ffprobe.

    python generate_podcast.py
"""
import email.utils
import html
import json
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

DOCS = Path(__file__).parent / "docs"
SITE = "https://rpagliuca.github.io/curso-aberto-audiobook-portugues-iso-27001-lead-implementer/"
TITLE = "ISO 27001 Lead Implementer — curso em áudio"
AUTHOR = "rpagliuca"
SUMMARY = ("Curso aberto, em português, para estudar para a certificação ISO/IEC 27001 Lead Implementer "
           "ouvindo. Dois episódios longos, com capítulos: o conteúdo e as perguntas e respostas.")
# Datas fixas: regenerar o feed não deve fazer o app achar que há episódio novo.
PUB = {"conteudo": datetime(2026, 11, 17, 12, 0, tzinfo=timezone.utc),
       "perguntas": datetime(2026, 11, 17, 12, 1, tzinfo=timezone.utc)}


def cards():
    """(src, rótulo, título) de cada player, na ordem do site."""
    page = (DOCS / "index.html").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<div class="card" id="card-\d+">(.*?)<div class="player" ([^>]*)>', page, re.S):
        attrs = dict(re.findall(r'data-(\w+)="([^"]*)"', m.group(2)))
        h2 = re.search(r"<h2>(.*?)</h2>", m.group(1), re.S).group(1)
        label = attrs.get("label") or f"Episódio {attrs['ep']}"
        out.append((attrs["src"], label, html.unescape(re.sub(r"<[^>]+>", "", h2)).strip()))
    return out


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def hms(s):
    s = int(round(s))
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"


def build(slug, title, parts):
    """Concatena os MP3 sem recodificar e grava os capítulos. Devolve os dados do episódio."""
    chapters, t = [], 0.0
    for src, label, name in parts:
        d = duration(DOCS / src)
        chapters.append({"startTime": round(t, 3), "title": f"{label} — {name}", "end": t + d})
        t += d
    meta = [";FFMETADATA1", f"title={title}", f"artist={AUTHOR}", f"album={TITLE}", "genre=Podcast"]
    for c in chapters:
        meta += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={int(c['startTime'] * 1000)}",
                 f"END={int(c['end'] * 1000)}", f"title={c['title']}"]
    out = DOCS / f"podcast-{slug}.mp3"
    with tempfile.TemporaryDirectory() as tmp:
        lst, mf = Path(tmp) / "lista.txt", Path(tmp) / "meta.txt"
        lst.write_text("".join(f"file '{(DOCS / s).resolve()}'\n" for s, _, _ in parts), encoding="utf-8")
        mf.write_text("\n".join(meta) + "\n", encoding="utf-8")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-i", str(mf), "-map", "0:a", "-map_metadata", "1", "-map_chapters", "1",
                        "-c", "copy", "-id3v2_version", "3", "-write_xing", "1", str(out)], check=True)
    (DOCS / f"podcast-{slug}.chapters.json").write_text(json.dumps(
        {"version": "1.2.0", "chapters": [{"startTime": c["startTime"], "title": c["title"]} for c in chapters]},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"slug": slug, "title": title, "file": out.name, "bytes": out.stat().st_size,
            "duration": duration(out), "chapters": chapters}


def item(ep, n):
    esc = html.escape
    lines = "\n".join(f"{hms(c['startTime'])} {c['title']}" for c in ep["chapters"])
    desc = (f"{len(ep['chapters'])} capítulos numa faixa só: o ±10 s atravessa os capítulos.\n\n{lines}\n\n"
            f"Quizzes, simulado e roteiro: {SITE}")
    return f"""  <item>
   <title>{esc(ep['title'])}</title>
   <itunes:title>{esc(ep['title'])}</itunes:title>
   <itunes:episode>{n}</itunes:episode>
   <itunes:episodeType>full</itunes:episodeType>
   <guid isPermaLink="false">iso27001-lead-implementer-{ep['slug']}</guid>
   <pubDate>{email.utils.format_datetime(PUB[ep['slug']])}</pubDate>
   <enclosure url="{SITE}{ep['file']}" length="{ep['bytes']}" type="audio/mpeg"/>
   <itunes:duration>{int(round(ep['duration']))}</itunes:duration>
   <description>{esc(desc)}</description>
   <podcast:chapters url="{SITE}podcast-{ep['slug']}.chapters.json" type="application/json+chapters"/>
   <itunes:explicit>false</itunes:explicit>
  </item>"""


def main():
    cs = cards()
    eps = [build("conteudo", "Conteúdo — os 7 domínios da prova", [c for c in cs if not c[0].startswith("p")]),
           build("perguntas", "Perguntas e respostas — responda em voz alta", [c for c in cs if c[0].startswith("p")])]
    esc = html.escape
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:podcast="https://podcastindex.org/namespace/1.0" xmlns:atom="http://www.w3.org/2005/Atom">
 <channel>
  <title>{esc(TITLE)}</title>
  <link>{SITE}</link>
  <atom:link href="{SITE}podcast.xml" rel="self" type="application/rss+xml"/>
  <language>pt-BR</language>
  <description>{esc(SUMMARY)}</description>
  <itunes:summary>{esc(SUMMARY)}</itunes:summary>
  <itunes:author>{esc(AUTHOR)}</itunes:author>
  <itunes:image href="{SITE}podcast-artwork.png"/>
  <image><url>{SITE}podcast-artwork.png</url><title>{esc(TITLE)}</title><link>{SITE}</link></image>
  <itunes:category text="Education"/>
  <itunes:explicit>false</itunes:explicit>
  <itunes:type>serial</itunes:type>
{chr(10).join(item(e, n) for n, e in enumerate(eps, 1))}
 </channel>
</rss>
"""
    (DOCS / "podcast.xml").write_text(feed, encoding="utf-8")
    art = DOCS / "podcast-artwork.png"
    if not art.exists():   # o Apple Podcasts pede no mínimo 1400×1400
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(DOCS / "artwork.png"), "-vf",
                        "scale=1400:1400:flags=lanczos", str(art)], check=True)
    for e in eps:
        print(f"{e['file']}: {hms(e['duration'])}, {e['bytes'] / 1e6:.1f} MB, {len(e['chapters'])} capítulos")
    print("docs/podcast.xml")


if __name__ == "__main__":
    main()
