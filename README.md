# curso-aberto-audiobook-portugues-iso-27001-lead-implementer

Curso aberto, em português, para estudar para a certificação **ISO/IEC 27001 Lead Implementer** ouvindo — no carro, na caminhada, na academia.

**▶ Ouvir agora: https://rpagliuca.github.io/curso-aberto-audiobook-portugues-iso-27001-lead-implementer/**

## O que tem

- **Audiobook** — 6 episódios (~58 min) cobrindo os 7 domínios da prova, com resumo e quiz de 6 questões por episódio.
- **Capítulos extras** — 5 capítulos (~24 min) com o que o curso e a prova cobram além dos 6 episódios: a família de normas e os marcos vizinhos, o projeto de implementação, contexto e política na prática, documentos/treinamento/nuvem/IA, e medição, auditoria e o dia da prova. Cada um termina com duas perguntas para fixar.
- **Perguntas e respostas** — 11 capítulos (~88 min, 167 perguntas) no formato *pergunta → silêncio → resposta → explicação*, com repetição espaçada dentro de cada capítulo. Responda em voz alta durante o silêncio. Oito capítulos são temáticos e três misturam os temas.
- **Simulado diagnóstico** — 20 questões de múltipla escolha com nota por domínio e revisão comentada dos erros.
- **Player feito para dirigir** — os botões avançar/voltar do Bluetooth do carro ou do fone pulam 10 s e atravessam os capítulos como uma faixa contínua; ao terminar um capítulo o próximo começa sozinho; a posição é retomada ao reabrir a página.

## Ouvir num app de podcast

O feed `https://rpagliuca.github.io/curso-aberto-audiobook-portugues-iso-27001-lead-implementer/podcast.xml` tem três episódios longos, **Conteúdo** (~58 min, 6 capítulos), **Perguntas e respostas** (~88 min, 11 capítulos) e **Capítulos extras** (~24 min, 5 capítulos). Cada um é uma faixa só, para o ±10 s atravessar os capítulos; os capítulos vão no MP3 (ID3 CHAP) e em JSON (`podcast:chapters`).

Quando uma faixa já publicada é regenerada, incremente a versão dela em `VERSAO` no `generate_podcast.py`: o endereço do MP3 e do JSON ganha `?v=N` e o app Podcasts, que guarda o áudio pelo endereço, baixa o novo; `guid` e `pubDate` não mudam.

No Apple Podcasts: Biblioteca → ⋯ → Seguir um Programa por URL. Vale a pena no iPhone: com o player do site, o iOS congela a página depois de alguns minutos pausado e o play da tela de bloqueio para de responder; no app de podcast isso não acontece.

## O texto é o código-fonte

Todo áudio é **artefato gerado a partir de texto versionado neste repositório**. Para revisar, corrigir ou contribuir com conteúdo, edite o texto — nunca o MP3.

| Conteúdo | Fonte | Gerador |
|---|---|---|
| Audiobook (6 episódios) | `iso27001-roteiro-audio.md` | `generate_audiobook.py` |
| Capítulos extras (5) | `iso27001-roteiro-extras.md` | `generate_audiobook.py extras` |
| Perguntas e respostas | `perguntas/pNN-*.md` | `generate_perguntas.py` |
| Resumo para leitura (~1 h) | `iso27001-resumo-1h.md` | — |
| Site (GitHub Pages) | `docs/` | cards de perguntas gerados entre `QA:START` e `QA:END` do `docs/index.html` |

### Formato de um capítulo de perguntas

```markdown
# P1 — Título
tipo: tema            (ou: misto)
dominio: D1 Fundamentos 12%
topicos: ...

## Abertura
Texto falado no início.

## Perguntas

### id-da-pergunta
P: A pergunta.
R: Resposta curta, que dê para falar em voz alta.
E: Explicação de uma ou duas frases.

### = id-da-pergunta        ← re-pergunta (repetição espaçada): toca só P → silêncio → R

## Encerramento
Texto falado no fim.
```

### Como o silêncio é feito

O `edge-tts` não aceita pausas em SSML. Então cada trecho é sintetizado separadamente, decodificado para PCM, e o silêncio entra como amostras zeradas entre os trechos, com um único encode no final. A duração segue a lógica do método Pimsleur — proporcional à resposta esperada, não fixa: `tempo para lembrar + 1,4 × duração da resposta`, limitada a 5,5–10 s. As constantes ficam no topo de `generate_perguntas.py`.

## Gerar os áudios

Requer Python 3, `ffmpeg` e `pip install edge-tts`.

```bash
python generate_perguntas.py p07      # regenera só o capítulo P7 (sem argumento = todos)
python generate_audiobook.py          # regenera os 6 episódios do audiobook
python generate_audiobook.py extras   # regenera os 5 capítulos extras (docs/x01-… a x05-…)
python generate_audiobook.py extras 2 # regenera só o Extra 2
python generate_audiobook.py extras --texto   # só imprime o texto que vai para o TTS, para conferir a pronúncia
python generate_podcast.py            # remonta o feed de podcast (rode depois dos geradores acima)
python serve.py                       # serve docs/ em http://127.0.0.1:8742 com suporte a HTTP Range
```

> Não use `python -m http.server` para testar: ele não atende `Range`, e sem isso o navegador não consegue saltar dentro do MP3 nem retomar a posição salva.

Pronúncia: a voz é `pt-BR-AntonioNeural`. Siglas e termos em inglês são reescritos foneticamente pelos mapas `ACRONYM_MAP`/`PHONETIC_MAP` (`generate_audiobook.py`) e `EXTRA_PHONETIC` (`generate_perguntas.py`). Sigla falada letra por letra vai com pontos (`PECB` → `P.E.C.B.`); sigla falada como palavra e termo em inglês vão grafados como soam em português (`SaaS` → `sás`, `CISO` → `cízo`, `shall` → `chél`). As siglas casam só com as maiúsculas exatas, para não trocar palavras do português ("ia", "cio"). Ouviu algo estranho? Ajuste o mapa e regenere o capítulo.

## Testes do player

`testes/player-cdp-test.mjs` exercita o player num Chrome headless via DevTools Protocol (salto de 10 s, travessia entre capítulos, emenda automática, retomada de posição). Com o `serve.py` rodando:

```bash
google-chrome --headless=new --remote-debugging-port=9333 --autoplay-policy=no-user-gesture-required \
  --mute-audio --user-data-dir=$(mktemp -d) about:blank &
node testes/player-cdp-test.mjs
# contra o site publicado:
SITE_URL=https://rpagliuca.github.io/curso-aberto-audiobook-portugues-iso-27001-lead-implementer/index.html node testes/player-cdp-test.mjs
```

## Aviso

Material de estudo independente, sem vínculo com a ISO, a PECB ou qualquer organismo de certificação. O conteúdo foi escrito com apoio de IA e **não substitui a leitura da norma** nem o material oficial do curso. Achou um erro? Abra uma issue ou um pull request editando o texto-fonte.
