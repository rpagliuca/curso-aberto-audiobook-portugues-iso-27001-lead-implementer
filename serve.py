#!/usr/bin/env python3
"""Servidor estático do hotsite com suporte a HTTP Range (o `python3 -m http.server` NÃO tem).

Sem Range o navegador não consegue saltar para um trecho do MP3 que ainda não baixou: retomar a
posição salva e os saltos longos voltam para 0:00. Uso:  python3 serve.py  (serve ./docs em 127.0.0.1:8742)
"""
import os, re, sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8742


class RangeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        if self.path.split("?")[0].endswith((".html", "/")):
            self.send_header("Cache-Control", "no-cache")   # página sempre fresca; MP3 pode cachear
        super().end_headers()

    def send_head(self):
        rng = self.headers.get("Range")
        path = self.translate_path(self.path)
        m = re.fullmatch(r"bytes=(\d*)-(\d*)", rng.strip()) if rng else None
        if not m or not os.path.isfile(path) or (m.group(1) == "" and m.group(2) == ""):
            return super().send_head()
        size = os.path.getsize(path)
        if m.group(1) == "":                                  # sufixo: últimos N bytes
            start, end = max(0, size - int(m.group(2))), size - 1
        else:
            start = int(m.group(1))
            end = min(int(m.group(2)), size - 1) if m.group(2) else size - 1
        if start >= size or start > end:
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return None
        f = open(path, "rb")
        f.seek(start)
        self._remaining = end - start + 1
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(self._remaining))
        self.send_header("Last-Modified", self.date_time_string(os.path.getmtime(path)))
        self.end_headers()
        return f

    def copyfile(self, source, outputfile):
        remaining = getattr(self, "_remaining", None)
        if remaining is None:
            return super().copyfile(source, outputfile)
        self._remaining = None
        while remaining > 0:
            chunk = source.read(min(65536, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)


if __name__ == "__main__":
    ThreadingHTTPServer.allow_reuse_address = True
    ThreadingHTTPServer(("127.0.0.1", PORT), RangeHandler).serve_forever()
