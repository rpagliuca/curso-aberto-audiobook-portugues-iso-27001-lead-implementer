# P1 — Fundamentos de segurança da informação
tipo: tema
dominio: D1 Fundamentos 12%
topicos: Tríade CIA · Ativo, ameaça, vulnerabilidade, risco · Família ISO 27000 · PDCA · Tipos de controle

## Abertura
Capítulo de perguntas e respostas número um: fundamentos de segurança da informação.
Funciona assim: eu faço uma pergunta e fico em silêncio por alguns segundos. Nesse silêncio, responda em voz alta,
mesmo que esteja sozinho no carro. Falar a resposta fixa muito mais do que só pensar nela. Depois eu digo a resposta
certa e uma explicação curta. Algumas perguntas vão voltar mais adiante, de propósito. Vamos começar.

## Perguntas

### cia
P: Quais são as três propriedades da tríade CIA?
R: Confidencialidade, integridade e disponibilidade.
E: Confidencialidade é só quem pode acessa. Integridade é a informação exata e completa. Disponibilidade é
acessível quando necessário.

### integridade-cenario
P: Um analista altera, sem autorização, o valor de um salário na planilha da folha de pagamento. Nada vazou e
o sistema não caiu. Qual propriedade foi comprometida?
R: Integridade.
E: Alteração indevida afeta a exatidão da informação. Não houve divulgação, então não é confidencialidade.

### vulnerabilidade
P: Como se chama a fraqueza de um ativo ou de um controle que pode ser explorada?
R: Vulnerabilidade.
E: Um servidor sem atualização é uma vulnerabilidade. Quem pode explorá-la é a ameaça.

### ameaca
P: E como se chama a causa potencial de um incidente indesejado?
R: Ameaça.
E: Um grupo criminoso, um incêndio ou um funcionário descuidado são ameaças. A ameaça explora a vulnerabilidade.

### = cia

### risco
P: Pela ISO 27000, qual é a definição de risco?
R: O efeito da incerteza sobre os objetivos.
E: Na prática, em segurança da informação, o risco é medido combinando a probabilidade de um evento com a sua
consequência.

### certificavel
P: Qual norma da família ISO 27000 é certificável?
R: A ISO 27001.
E: Só ela traz requisitos obrigatórios. As outras são guias e orientações.

### iso27002
P: Qual é o papel da ISO 27002?
R: Guia de implementação dos controles.
E: Ela detalha os noventa e três controles do Anexo A, com orientações. Ninguém se certifica na 27002.

### = vulnerabilidade

### iso27005
P: E qual norma da família orienta a gestão de riscos de segurança da informação?
R: A ISO 27005.
E: Ela é orientação, não requisito. A 27001 exige um processo de riscos, mas não obriga a usar a 27005.

### sgsi
P: O que significa a sigla SGSI?
R: Sistema de gestão de segurança da informação.
E: É o conjunto de políticas, processos, pessoas e controles que a organização usa para gerir os riscos à
informação. Não é um software nem um departamento.

### = risco

### pdca-fases
P: Quais são as quatro fases do ciclo PDCA?
R: Planejar, fazer, verificar e agir.
E: O SGSI é um ciclo de melhoria contínua, não um projeto com fim.

### pdca-auditoria
P: Em qual fase do PDCA fica a auditoria interna?
R: Verificar.
E: Auditoria, monitoramento e análise crítica pela direção são as atividades de verificação.

### = certificavel

### tipos-controle
P: Quanto ao tipo, a ISO 27002 classifica os controles em três categorias. Quais?
R: Preventivo, detectivo e corretivo.
E: Preventivo evita o incidente. Detectivo percebe que ele aconteceu. Corretivo repara o dano.

### backup-tipo
P: O backup é um controle preventivo, detectivo ou corretivo?
R: Corretivo.
E: Ele atua depois do incidente, restaurando a informação perdida.

### = iso27005

### si-vs-ti
P: Verdadeiro ou falso: segurança da informação é a mesma coisa que segurança de TI.
R: Falso.
E: Segurança da informação cobre a informação em qualquer forma: papel, conversa, conhecimento das pessoas.
Segurança de TI é só a parte tecnológica.

### disponibilidade-cenario
P: Um ataque de ransomware cifra o servidor de arquivos e a equipe fica dois dias sem acessar os documentos.
Qual propriedade foi a principal afetada?
R: Disponibilidade.
E: A informação deixou de estar acessível quando necessária. Se os dados também tivessem sido roubados,
haveria perda de confidencialidade.

### = pdca-auditoria

### = tipos-controle

## Encerramento
Fim do capítulo um. Se alguma resposta não veio na hora, ouça de novo amanhã: a repetição com intervalo é o que
leva para a memória de longo prazo. Até o próximo capítulo.
