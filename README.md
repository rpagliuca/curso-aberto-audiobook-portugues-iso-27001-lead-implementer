# curso-aberto-audiobook-portugues-iso-27001-lead-implementer

Curso aberto, em português, para estudar para a certificação **ISO/IEC 27001 Lead Implementer** ouvindo — no carro, na caminhada, na academia.

**▶ Ouvir agora: https://rpagliuca.github.io/curso-aberto-audiobook-portugues-iso-27001-lead-implementer/**

## O que tem

- **Audiobook** — 6 episódios (~58 min) cobrindo os 7 domínios da prova, com resumo e quiz de 6 questões por episódio.
- **Perguntas e respostas** — 11 capítulos (~88 min, 167 perguntas) no formato *pergunta → silêncio → resposta → explicação*, com repetição espaçada dentro de cada capítulo. Responda em voz alta durante o silêncio. Oito capítulos são temáticos e três misturam os temas.
- **Simulado diagnóstico** — 20 questões de múltipla escolha com nota por domínio e revisão comentada dos erros.
- **Player feito para dirigir** — os botões avançar/voltar do Bluetooth do carro ou do fone pulam 10 s e atravessam os capítulos como uma faixa contínua; ao terminar um capítulo o próximo começa sozinho; a posição é retomada ao reabrir a página.

## O texto é o código-fonte

Todo áudio é **artefato gerado a partir de texto versionado neste repositório**. Para revisar, corrigir ou contribuir com conteúdo, edite o texto — nunca o MP3.

| Conteúdo | Fonte | Gerador |
|---|---|---|
| Audiobook (6 episódios) | `iso27001-roteiro-audio.md` | `generate_audiobook.py` |
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
python serve.py                       # serve docs/ em http://127.0.0.1:8742 com suporte a HTTP Range
```

> Não use `python -m http.server` para testar: ele não atende `Range`, e sem isso o navegador não consegue saltar dentro do MP3 nem retomar a posição salva.

Pronúncia: a voz é `pt-BR-AntonioNeural`. Siglas e termos em inglês são reescritos foneticamente pelos mapas `ACRONYM_MAP`/`PHONETIC_MAP` (`generate_audiobook.py`) e `EXTRA_PHONETIC` (`generate_perguntas.py`). Ouviu algo estranho? Ajuste o mapa e regenere o capítulo.

## Testes do player

`testes/player-cdp-test.mjs` exercita o player num Chrome headless via DevTools Protocol (salto de 10 s, travessia entre capítulos, emenda automática, retomada de posição). Com o `serve.py` rodando:

```bash
google-chrome --headless=new --remote-debugging-port=9333 --autoplay-policy=no-user-gesture-required \
  --mute-audio --user-data-dir=$(mktemp -d) about:blank &
node testes/player-cdp-test.mjs
```

## Aviso

Material de estudo independente, sem vínculo com a ISO, a PECB ou qualquer organismo de certificação. O conteúdo foi escrito com apoio de IA e **não substitui a leitura da norma** nem o material oficial do curso. Achou um erro? Abra uma issue ou um pull request editando o texto-fonte.
