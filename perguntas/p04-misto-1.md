# P4 — Misto 1: fundamentos, contexto e riscos
tipo: misto
dominio: Temas misturados · D1 D2 D3
topicos: Cenários curtos misturando tríade CIA, família de normas, contexto, liderança, riscos e SoA

## Abertura
Capítulo quatro: perguntas misturadas sobre os três primeiros capítulos. Agora os temas vêm fora de ordem e em
forma de situação, como na prova. Responda em voz alta.

## Perguntas

### m-notebook
P: Um notebook sem criptografia é furtado com dados de clientes. Qual propriedade foi comprometida em primeiro lugar?
R: Confidencialidade.
E: Os dados ficaram expostos a quem não tem autorização. Se era a única cópia, houve também perda de
disponibilidade.

### m-sem-patch
P: Nesse mesmo caso, a falta de criptografia no disco é ameaça, vulnerabilidade ou risco?
R: Vulnerabilidade.
E: A ameaça é o ladrão. O risco é a combinação da chance do furto com o impacto do vazamento.

### m-quem-aceita
P: O gerente de TI quer aceitar um risco alto no sistema financeiro, mas o proprietário desse risco é o diretor
financeiro. Quem decide?
R: O diretor financeiro, que é o proprietário do risco.
E: Aceitar o risco residual é atribuição do proprietário do risco, não da área técnica.

### m-auditor-27002
P: Um consultor oferece certificar a empresa na ISO 27002. O que há de errado?
R: A 27002 não é certificável. Só a 27001.
E: A 27002 é guia de controles, sem requisitos obrigatórios.

### m-escopo-nuvem
P: A empresa usa um provedor de nuvem para hospedar o sistema que está no escopo. Onde isso deve aparecer ao definir
o escopo?
R: Nas interfaces e dependências.
E: Cláusula 4.3. O provedor fica fora da fronteira, mas a dependência precisa ser reconhecida e controlada.

### = m-sem-patch

### m-politica-assina
P: O CISO redigiu a política de segurança e ele mesmo aprovou e publicou. Qual é o problema?
R: A política deve ser estabelecida pela alta direção.
E: Cláusula 5.2. Sem o envolvimento da direção, falta evidência de liderança e comprometimento.

### m-terceirizar
P: A empresa terceiriza o data center para reduzir sua exposição. Qual opção da MECA é essa?
R: Compartilhar.
E: Terceirização e seguro são as formas típicas de compartilhar o risco.

### m-ordem
P: O que vem primeiro: a declaração de aplicabilidade ou a avaliação de riscos?
R: A avaliação de riscos.
E: A SoA é consequência do tratamento de riscos. Escolher controles antes de avaliar riscos é um erro clássico.

### = m-quem-aceita

### m-pdca-planejar
P: A avaliação de riscos pertence a qual fase do PDCA?
R: Planejar.
E: As cláusulas 4, 5, 6 e 7 compõem o planejar. A 8 é o fazer, a 9 é o verificar e a 10 é o agir.

### m-clausulas-auditaveis
P: Quais cláusulas da ISO 27001 contêm os requisitos auditáveis?
R: As cláusulas de quatro a dez.
E: As cláusulas de zero a três são introdução, escopo da norma, referências e termos.

### m-excluir-clausula
P: Uma organização pode excluir alguma das cláusulas de quatro a dez para se certificar?
R: Não. Nenhuma.
E: Exclusão só é possível para controles do Anexo A, e com justificativa. As cláusulas de quatro a dez são
todas obrigatórias.

### = m-ordem

### m-criterios
P: Dois analistas avaliam o mesmo risco e chegam a níveis totalmente diferentes. Qual requisito provavelmente
está falhando?
R: Os critérios e a metodologia de avaliação de riscos.
E: A norma exige resultados consistentes, válidos e comparáveis. Isso depende de critérios definidos e
documentados.

### m-partes
P: Um novo regulamento de proteção de dados entra em vigor. Em qual cláusula isso entra primeiro no SGSI?
R: Na cláusula 4, contexto e partes interessadas.
E: É uma questão externa e um requisito de parte interessada, o regulador. Depois pode gerar novos riscos e
controles.

### = m-excluir-clausula

### m-detectivo
P: Um sistema que alerta quando alguém tenta várias senhas erradas é um controle de que tipo?
R: Detectivo.
E: Ele percebe o evento. Se bloqueasse a conta automaticamente, teria também um efeito preventivo.

### m-integridade-hash
P: A empresa passa a usar assinatura digital nos contratos para garantir que não foram alterados. Qual propriedade
ela está protegendo?
R: Integridade.
E: A assinatura digital também dá autenticidade e não repúdio, mas a proteção contra alteração é integridade.

### = m-clausulas-auditaveis

### = m-criterios

## Encerramento
Fim do capítulo quatro. Se errou mais de cinco, volte aos capítulos um, dois e três antes de seguir.
