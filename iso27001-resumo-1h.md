# ISO 27001 Lead Implementer — Resumo Completo (~1 hora de leitura)

> Cobre todos os 7 domínios da prova com profundidade proporcional ao peso. Leitura linear recomendada na primeira vez.

---

## D1 — Fundamentos e Conceitos de SI (12%)

### Tríade CIA
- **Confidencialidade:** acesso à informação apenas por quem é autorizado.
- **Integridade:** informação completa, exata e não alterada sem autorização.
- **Disponibilidade:** informação e sistemas acessíveis quando necessário.

Extensões da tríade: **autenticidade** (identidade verificada), **não-repúdio** (impossível negar autoria), **confiabilidade** (comportamento consistente e esperado).

### Conceitos essenciais

| Termo | Definição |
|-------|-----------|
| **Ativo** | Qualquer coisa com valor para a organização (dados, sistemas, pessoas, processos, reputação) |
| **Ameaça** | Causa potencial de um incidente indesejado (agente externo/interno) |
| **Vulnerabilidade** | Fraqueza que pode ser explorada por uma ameaça |
| **Risco** | Probabilidade × Impacto de uma ameaça explorar uma vulnerabilidade |
| **Impacto** | Consequência de um incidente sobre os objetivos de negócios |
| **Controle** | Medida que modifica o risco (preventivo, detectivo ou corretivo) |
| **Incidente de SI** | Evento não desejado que compromete a CIA |
| **Evento de SI** | Ocorrência identificada que pode ser um incidente ou não |

### Família ISO 27000

| Norma | Função |
|-------|--------|
| **ISO 27000** | Vocabulário e definições |
| **ISO 27001** | **Requisitos** do SGSI (certificável) |
| **ISO 27002** | **Guia** de implementação dos controles do Anexo A |
| **ISO 27005** | Gestão de riscos de SI |
| **ISO 27017** | Controles para serviços em nuvem |
| **ISO 27018** | Proteção de dados pessoais na nuvem |
| **ISO 27701** | Extensão para privacidade (SGSI → SGPI) |

**Regra chave:** ISO 27001 = **requisitos** (o que a organização DEVE fazer). ISO 27002 = **guia** (como implementar). Certificação é possível apenas contra a 27001.

### PDCA aplicado ao SGSI

```
PLAN  → Estabelecer o SGSI (cláusulas 4, 5, 6)
DO    → Implementar e operar (cláusulas 7, 8)
CHECK → Monitorar e analisar (cláusula 9)
ACT   → Melhorar continuamente (cláusula 10)
```

### High Level Structure (Annex SL / HLS)
ISO 27001 segue a estrutura padrão de normas ISO: cláusulas 1-3 são introdutórias; **cláusulas 4-10 são os requisitos** e têm a mesma numeração em todas as normas de gestão (ISO 9001, ISO 14001 etc.), facilitando integração.

---

## D2 — Iniciação ao SGSI (10%)

### Por que implementar um SGSI
- Proteger informações críticas contra ameaças crescentes
- Cumprir requisitos legais, regulatórios e contratuais (LGPD, GDPR, contratos com clientes)
- Aumentar confiança de clientes, parceiros e partes interessadas
- Estruturar resposta a incidentes e reduzir perdas financeiras/reputacionais
- Habilitar negócios (alguns setores exigem ISO 27001 para firmar contratos)

### Fatores críticos de sucesso
1. **Comprometimento da alta direção** — sem isso, o SGSI não sai do papel
2. Escopo realista e bem definido
3. Recursos adequados (orçamento, pessoas, tempo)
4. Cultura de segurança — conscientização em todos os níveis
5. Abordagem baseada em risco — não é checklist

### Estrutura de um projeto de implementação
Fases típicas de um projeto Lead Implementer:
1. **Iniciação:** patrocinador, equipe, escopo, cronograma
2. **Diagnóstico:** gap analysis — o que já existe vs. o que a norma exige
3. **Planejamento:** avaliação de riscos, SoA, PTR
4. **Implementação:** políticas, procedimentos, controles técnicos
5. **Treinamento e conscientização**
6. **Auditoria interna**
7. **Revisão pela direção**
8. **Auditoria de certificação** (fase 1 documental + fase 2 operacional)

### Papéis e responsabilidades

| Papel | Responsabilidade |
|-------|-----------------|
| **Alta direção** | Comprometimento, recursos, aprovação da política, revisão do SGSI |
| **Representante da gestão / CISO** | Coordenar implementação, relatar à direção |
| **Proprietário de ativo** | Identificar e tratar riscos associados aos seus ativos |
| **Comitê de SI** | Governança, decisões estratégicas de SI |
| **Usuários** | Cumprir políticas, reportar incidentes |
| **Auditores internos** | Verificar conformidade (não podem auditar áreas sob sua responsabilidade) |

### Certificação vs conformidade
- **Conformidade:** a organização atende aos requisitos da norma (pode ser autodeclarada)
- **Certificação:** um organismo de certificação acreditado (OC) verifica e emite certificado
- Certificado válido por **3 anos**, com auditorias de manutenção anuais (surveillance audits)

---

## D3 — Planejamento do SGSI — Cláusulas 4-6 (18%)

### Cláusula 4 — Contexto da organização

**4.1 — Contexto interno e externo**
- **Externo:** fatores políticos, econômicos, tecnológicos, legais, concorrência, cultura regional
- **Interno:** estratégia, estrutura, cultura, capacidades, sistemas existentes, obrigações contratuais

Ferramenta usual: análise **PESTLE** (externo) + **SWOT** (interno/externo combinados).

**4.2 — Partes interessadas e requisitos**
- Identificar partes interessadas relevantes: clientes, reguladores, fornecedores, acionistas, funcionários
- Mapear seus requisitos (legais, contratuais, expectativas)
- Esses requisitos influenciam o escopo e os controles selecionados

**4.3 — Escopo do SGSI**
- Definir os limites: unidades organizacionais, localizações, ativos, tecnologias incluídas
- Escopo deve ser **documentado** (informação documentada obrigatória)
- Escopo amplo = mais proteção, mais esforço; escopo estreito = certificação mais rápida, mas proteção parcial

**4.4 — SGSI**
- A organização deve estabelecer, implementar, manter e **melhorar continuamente** o SGSI

### Cláusula 5 — Liderança

**5.1 — Comprometimento da liderança**
A alta direção deve (são requisitos, não sugestões):
- Assegurar que política e objetivos de SI são compatíveis com a estratégia
- Integrar os requisitos do SGSI nos processos de negócio
- Assegurar recursos
- Comunicar a importância da gestão eficaz de SI
- Conduzir revisões pela direção (cláusula 9.3)

**5.2 — Política de segurança da informação**
A política deve:
- Ser apropriada ao propósito da organização
- Incluir objetivos ou estrutura para definir objetivos
- Incluir comprometimento de atender requisitos aplicáveis
- Incluir comprometimento de melhoria contínua
- Estar disponível como **informação documentada**
- Ser comunicada internamente e, quando pertinente, a partes interessadas

**5.3 — Papéis, responsabilidades e autoridades**
- Atribuição de responsabilidades para assegurar conformidade com a norma
- Notificar o desempenho do SGSI à alta direção

### Cláusula 6 — Planejamento

**6.1.1 — Ações para tratar riscos e oportunidades**
Ao planejar o SGSI, a organização deve considerar as questões do item 4.1 e os requisitos do item 4.2, e determinar riscos e oportunidades para:
- Assegurar que o SGSI atinja os resultados pretendidos
- Prevenir ou reduzir efeitos indesejados
- Alcançar melhoria contínua

**6.1.2 — Avaliação de riscos de SI**
A organização deve definir e aplicar um processo de avaliação de riscos que:
- Estabeleça **critérios de risco** (aceitação e avaliação) — deve ser consistente e reproduzível
- Identifique riscos associados à perda de CIA
- Analise os riscos (probabilidade e impacto)
- Avalie e priorize os riscos (comparar com critérios de aceitação)

**Processo de gestão de riscos (ISO 27005):**
```
Identificação → Análise → Avaliação → Tratamento → Monitoramento
```

**6.1.3 — Tratamento de riscos de SI**
Quatro opções de tratamento (mnemônico **MECA**):
- **M**odificar (mitigar): implementar controles para reduzir probabilidade ou impacto
- **E**vitar: eliminar a atividade que gera o risco
- **C**ompartilhar (transferir): seguros, terceirização, contratos
- **A**ceitar (reter): risco dentro do critério de aceitação, ou custo do controle > benefício

**Declaração de Aplicabilidade (SoA — Statement of Applicability):**
- Documento **obrigatório** pela norma (6.1.3 d)
- Lista **todos os 93 controles** do Anexo A
- Para cada controle: incluído ou excluído, justificativa, status de implementação
- Controles excluídos devem ter justificativa plausível (o risco não existe, o escopo não cobre etc.)
- **Não se pode excluir um controle apenas por ser difícil de implementar**

**Plano de Tratamento de Riscos (PTR):**
- O que será feito, por quem, quando e com quais recursos
- Para cada risco não aceito: controle(s) selecionado(s) do Anexo A
- Aprovação dos proprietários dos riscos

**6.2 — Objetivos de SI e planejamento para alcançá-los**
Objetivos devem ser: mensuráveis, monitoráveis, comunicados, atualizados. Devem ter plano de ação (quem, quando, como, recursos, avaliação).

**6.3 — Planejamento de mudanças**
Mudanças no SGSI devem ser feitas de forma planejada (não ad hoc).

---

## D4 — Implementação do SGSI — Cláusulas 7-8 (18%)

### Cláusula 7 — Suporte

**7.1 — Recursos**
A organização deve determinar e prover recursos necessários para estabelecer, implementar, manter e melhorar o SGSI.

**7.2 — Competência**
- Determinar competências necessárias para pessoas que afetam o desempenho do SGSI
- Assegurar que essas pessoas são competentes (educação, treinamento ou experiência)
- Tomar ações para adquirir competências necessárias
- Reter **evidências** de competência (registros de treinamentos)

**7.3 — Conscientização**
Pessoas devem estar conscientes de:
- A política de SI
- Sua contribuição para a eficácia do SGSI
- Implicações de não conformidade

**7.4 — Comunicação**
Definir: o que comunicar, quando, para quem, como e quem comunica — tanto interna quanto externamente.

**7.5 — Informação documentada**
O SGSI deve incluir informação documentada:
- Exigida pela norma (obrigatórios)
- Determinada necessária pela organização (discricionários)

**Documentos obrigatórios pela ISO 27001:**
1. Escopo do SGSI (4.3)
2. Política de SI (5.2)
3. Processo de avaliação de riscos (6.1.2)
4. Processo de tratamento de riscos (6.1.3)
5. Objetivos de SI (6.2)
6. Evidências de competência (7.2)
7. Outros evidenciados nos controles implementados
8. **Declaração de Aplicabilidade — SoA** (6.1.3 d)
9. Plano de Tratamento de Riscos — PTR (6.1.3 e)
10. Resultados de avaliação de riscos (8.2)
11. Resultados de tratamento de riscos (8.3)
12. Evidências de monitoramento e medição (9.1)
13. Programa de auditoria interna (9.2)
14. Resultados de auditorias internas (9.2)
15. Resultados de revisão pela direção (9.3)
16. Não conformidades e ações corretivas (10.2)

**Controle de informação documentada:**
- Distribuição, acesso, recuperação
- Armazenamento e preservação (incluindo legibilidade)
- Controle de mudanças
- Retenção e disposição
- Informação documentada de origem externa também deve ser identificada e controlada

### Cláusula 8 — Operação

**8.1 — Planejamento e controle operacional**
- Implementar processos necessários para atender requisitos
- Controlar mudanças planejadas, revisar consequências de mudanças não intencionais
- Controlar processos terceirizados

**8.2 — Avaliação de riscos de SI**
- Executar avaliações de riscos em intervalos planejados
- E quando mudanças significativas ocorrerem
- Reter resultados como informação documentada

**8.3 — Tratamento de riscos de SI**
- Implementar o plano de tratamento de riscos
- Reter resultados como informação documentada

### Implementação prática de controles

Ao implementar controles do Anexo A:
1. Verificar se o controle está marcado como aplicável no SoA
2. Definir proprietário do controle
3. Documentar procedimento/política de implementação
4. Testar eficácia do controle
5. Monitorar continuamente

**Gestão de ativos:** inventário de ativos deve existir (controle A.5.9), cada ativo com proprietário definido. Classificação da informação (A.5.12) define rótulos e manipulação.

**Segurança em RH:** triagem (A.6.1), termos de trabalho (A.6.2), conscientização (A.6.3), processo disciplinar (A.6.4), devolução de ativos ao desligar (A.6.5).

---

## D5 — Monitoramento, Medição e Revisão — Cláusula 9 (14%)

### Cláusula 9 — Avaliação de desempenho

**9.1 — Monitoramento, medição, análise e avaliação**
A organização deve determinar:
- O que monitorar e medir (processos, controles, objetivos)
- Métodos de análise e avaliação (para resultados válidos)
- Quando monitorar e medir
- Quando analisar e avaliar os resultados
- Quem analisa e avalia

Resultados devem ser retidos como **informação documentada** (evidência).

**Métricas e KPIs de SI:**
- Número de incidentes por período
- Tempo médio de detecção/resposta a incidentes
- Percentual de usuários treinados
- Número de vulnerabilidades não tratadas por criticidade
- Taxa de conformidade com políticas

**9.2 — Auditoria interna**
Auditoria interna deve ser conduzida em intervalos planejados para verificar se o SGSI:
- Está conforme com os requisitos da organização e da norma
- Está implementado e mantido eficazmente

**Programa de auditoria interna** deve considerar: importância dos processos, resultados de auditorias anteriores.

**Requisitos do auditor interno:**
- Imparcialidade: auditores **não auditam seu próprio trabalho**
- Objetividade
- Competência (pode ser interno treinado ou externo contratado)

**Critérios de auditoria:** norma + requisitos legais + políticas internas + SoA.

**Tipos de auditoria:**
| Tipo | Descrição |
|------|-----------|
| 1ª parte | Interna, conduzida pela própria organização |
| 2ª parte | Conduzida por cliente ou parte com interesse (ex: auditoria de fornecedor) |
| 3ª parte | Conduzida por organismo independente (certificação, regulatória) |

**Processo de auditoria:**
1. Planejamento e escopo
2. Documentação (revisão de documentos)
3. Execução no local (entrevistas, observação, testes)
4. Relatório (conformidades, não conformidades, observações)
5. Follow-up (verificação de ações corretivas)

**9.3 — Revisão pela direção**
A alta direção deve revisar o SGSI em intervalos planejados. A revisão considera:
- Status de ações de revisões anteriores
- Mudanças em questões internas/externas e partes interessadas
- Feedback de desempenho de SI:
  - Tendências em não conformidades e ações corretivas
  - Resultados de monitoramento e medição
  - Resultados de auditorias
  - Cumprimento dos objetivos de SI
  - Feedback de partes interessadas
  - Resultados de avaliação de riscos e status do PTR
- Oportunidades de melhoria contínua

**Saídas da revisão pela direção:**
- Decisões sobre oportunidades de melhoria contínua
- Mudanças necessárias no SGSI
- Necessidades de recursos

Tudo deve ser **documentado** (informação documentada obrigatória).

---

## D6 — Melhoria Contínua — Cláusula 10 (10%)

### Cláusula 10 — Melhoria

**10.1 — Melhoria contínua**
A organização deve melhorar continuamente a adequação, suficiência e eficácia do SGSI.

**10.2 — Não conformidade e ação corretiva**
Quando ocorre uma não conformidade, a organização deve:
1. **Reagir** à não conformidade: controlar, corrigir, lidar com as consequências (isso é a **correção**)
2. **Avaliar** a necessidade de ação corretiva (eliminar a **causa raiz**)
3. **Implementar** ações corretivas
4. **Revisar** a eficácia das ações corretivas
5. **Atualizar** o SGSI se necessário
6. **Documentar** não conformidades e ações tomadas

**Diferença fundamental:**
- **Correção:** resolve o sintoma (ex: bloquear acesso indevido identificado)
- **Ação corretiva:** elimina a causa raiz para que não se repita (ex: rever processo de concessão de acesso)

**Não conformidades vs Observações vs Oportunidades de melhoria:**
- **Não conformidade maior:** requisito da norma não implementado ou ineficaz — impede certificação
- **Não conformidade menor:** falha isolada, desvio parcial — deve ser corrigida mas não impede certificação
- **Observação/oportunidade:** não é não conformidade, mas pode se tornar se não tratada

**Fontes de entrada para melhoria:**
- Incidentes de SI
- Resultados de auditorias
- Revisão pela direção
- Feedback de funcionários e partes interessadas
- Análise de tendências
- Benchmarking

---

## D7 — Controles do Anexo A — ISO 27002:2022 (18%)

### Estrutura do Anexo A / ISO 27002:2022

**4 temas, 11 cláusulas, 93 controles** (atualização de 2022 — era 114 controles em 14 domínios na versão 2013).

```
Tema 1 — Organizacional (A.5):  37 controles
Tema 2 — Pessoas (A.6):          8 controles
Tema 3 — Físico (A.7):          14 controles
Tema 4 — Tecnológico (A.8):     34 controles
Total:                          93 controles
```

**Mnemônico para os temas: OPFT** — Organizacional, Pessoas, Físico, Tecnológico.

### Atributos dos controles (novidade na versão 2022)

Cada controle possui atributos que permitem filtragem e categorização:

**1. Tipo de controle:**
- `#Preventivo` — evita que o evento ocorra
- `#Detectivo` — identifica que o evento ocorreu
- `#Corretivo` — minimiza o impacto após o evento

**2. Propriedades de SI:**
- `#Confidencialidade`, `#Integridade`, `#Disponibilidade`

**3. Conceitos de segurança cibernética (Framework NIST-like):**
- `#Identificar`, `#Proteger`, `#Detectar`, `#Responder`, `#Recuperar`

**4. Capacidades operacionais** (ex): `#Governança`, `#Gestão_de_ativos`, `#Proteção_da_informação`, `#Segurança_de_RH`, `#Segurança_física`, etc.

**5. Domínios de segurança:**
- `#Governança_e_ecossistema`, `#Proteção`, `#Defesa`, `#Resiliência`

### Tema Organizacional — A.5 (37 controles) — Seleção-chave

| Controle | Descrição |
|----------|-----------|
| A.5.1 | Políticas de SI |
| A.5.2 | Papéis e responsabilidades de SI |
| A.5.9 | **Inventário de ativos de informação** |
| A.5.10 | Uso aceitável de ativos |
| A.5.12 | Classificação da informação |
| A.5.13 | Rotulagem da informação |
| A.5.14 | Transferência de informações |
| A.5.15 | Controle de acesso |
| A.5.16 | Gestão de identidade |
| A.5.17 | Informações de autenticação |
| A.5.19 | SI na cadeia de fornecimento |
| A.5.23 | SI para uso de serviços em nuvem *(novo em 2022)* |
| A.5.24 | Planejamento e preparação para gestão de incidentes |
| A.5.29 | SI durante disrupção |
| A.5.30 | **Preparação de TIC para continuidade de negócios** *(novo)* |
| A.5.34 | Privacidade e proteção de dados pessoais |
| A.5.36 | Conformidade com políticas e normas de SI |
| A.5.37 | Procedimentos operacionais documentados |

### Tema Pessoas — A.6 (8 controles)

| Controle | Descrição |
|----------|-----------|
| A.6.1 | Triagem (background check) |
| A.6.2 | Termos e condições de emprego |
| A.6.3 | Conscientização, educação e treinamento em SI |
| A.6.4 | Processo disciplinar |
| A.6.5 | Responsabilidades após término ou mudança de emprego |
| A.6.6 | Acordos de confidencialidade |
| A.6.7 | Trabalho remoto |
| A.6.8 | **Relato de eventos de SI** *(todos devem saber como reportar)* |

### Tema Físico — A.7 (14 controles)

| Controle | Descrição |
|----------|-----------|
| A.7.1 | Perímetros de segurança física |
| A.7.2 | Controle de acesso físico |
| A.7.3 | Segurança de escritórios, salas e instalações |
| A.7.4 | **Monitoramento de segurança física** *(novo em 2022)* |
| A.7.5 | Proteção contra ameaças físicas e ambientais |
| A.7.6 | Trabalho em áreas seguras |
| A.7.7 | Mesa e tela limpa |
| A.7.8 | Localização e proteção de equipamentos |
| A.7.9 | Segurança de ativos fora das instalações |
| A.7.10 | Mídia de armazenamento |
| A.7.11 | Utilitários de suporte (energia, água, etc.) |
| A.7.12 | Segurança de cabeamento |
| A.7.13 | Manutenção de equipamentos |
| A.7.14 | Descarte ou reutilização segura de equipamentos |

### Tema Tecnológico — A.8 (34 controles) — Seleção-chave

| Controle | Descrição |
|----------|-----------|
| A.8.1 | Dispositivos de endpoint de usuário |
| A.8.2 | Direitos de acesso privilegiado |
| A.8.3 | Restrição de acesso à informação |
| A.8.4 | Acesso ao código-fonte |
| A.8.5 | Autenticação segura |
| A.8.6 | Gestão de capacidade |
| A.8.7 | Proteção contra malware |
| A.8.8 | Gestão de vulnerabilidades técnicas |
| A.8.9 | Gestão de configuração |
| A.8.10 | Exclusão de informações |
| A.8.11 | Mascaramento de dados |
| A.8.12 | Prevenção de vazamento de dados (DLP) *(novo)* |
| A.8.13 | Backup da informação |
| A.8.14 | Redundância de instalações de processamento da informação |
| A.8.15 | Registro de logs |
| A.8.16 | **Monitoramento de atividades** *(novo)* |
| A.8.20 | Segurança de redes |
| A.8.23 | Filtragem de conteúdo web *(novo)* |
| A.8.24 | Uso de criptografia |
| A.8.25 | Ciclo de vida de desenvolvimento seguro |
| A.8.28 | Codificação segura *(novo)* |
| A.8.29 | Testes de segurança em desenvolvimento e aceitação |
| A.8.30 | Desenvolvimento terceirizado |
| A.8.31 | Separação de ambientes (dev/test/prod) |
| A.8.32 | Gestão de mudanças |
| A.8.33 | Informações de teste |
| A.8.34 | Proteção de sistemas em testes de auditoria |

### Controles novos na ISO 27002:2022 (11 adicionados)

Mnemônico para lembrar os 11 novos: **Inteligência + Nuvem + Dados + Código**

1. A.5.7 — Inteligência de ameaças
2. A.5.23 — SI para uso de serviços em nuvem
3. A.5.30 — Preparação de TIC para continuidade de negócios
4. A.7.4 — Monitoramento de segurança física
5. A.8.9 — Gestão de configuração
6. A.8.10 — Exclusão de informações
7. A.8.11 — Mascaramento de dados
8. A.8.12 — Prevenção de vazamento de dados (DLP)
9. A.8.16 — Monitoramento de atividades
10. A.8.23 — Filtragem de conteúdo web
11. A.8.28 — Codificação segura

### SoA — o que fazer com cada controle
Para cada um dos 93 controles, o SoA deve registrar:
- **Aplicável?** (Sim/Não)
- **Justificativa** para inclusão ou exclusão
- **Status de implementação** (planejado, em implementação, implementado)
- **Referência** à política/procedimento que implementa o controle

---

## Tabelas de Referência Rápida

### Números que a prova cobra
| Informação | Valor |
|-----------|-------|
| Controles no Anexo A (versão 2022) | **93** |
| Controles na versão anterior (2013) | 114 |
| Controles novos em 2022 | **11** |
| Temas no Anexo A | **4** |
| Controles organizacionais (A.5) | **37** |
| Controles de pessoas (A.6) | **8** |
| Controles físicos (A.7) | **14** |
| Controles tecnológicos (A.8) | **34** |
| Validade do certificado ISO 27001 | **3 anos** |
| Cláusulas de requisito da norma | **4-10** |

### Documentos obrigatórios — o que a norma exige explicitamente
A norma usa "deve manter" (documentos) e "deve reter" (registros). Memorize os principais:
- **Manter:** escopo, política, processo de avaliação e tratamento de riscos, objetivos, SoA
- **Reter:** resultados de avaliação de riscos, resultados de tratamento de riscos, evidências de competência, resultados de monitoramento, programa e resultados de auditorias, resultados de revisão pela direção, não conformidades e ações corretivas

### Fluxo completo de implementação do SGSI (mapa mental)

```
CONTEXTO (4)
├── Questões internas/externas
├── Partes interessadas e requisitos
└── Definição do ESCOPO ────────────────────────────────────┐
                                                             │
LIDERANÇA (5)                                                │
├── Comprometimento da alta direção                          │
├── POLÍTICA DE SI ◄──────────────────────────────────────┐ │
└── Papéis e responsabilidades                             │ │
                                                          │ │
PLANEJAMENTO (6)                                          │ │
├── Avaliação de riscos                                   │ │
│   └── Identificar → Analisar → Avaliar                  │ │
├── Tratamento de riscos (MECA)                           │ │
│   └── SoA + PTR ◄────────────────────────────────────┐ │ │
└── Objetivos de SI                                     │ │ │
                                                        │ │ │
SUPORTE (7)                                             │ │ │
├── Recursos, Competência, Conscientização               │ │ │
├── Comunicação                                          │ │ │
└── Informação documentada ◄────────────────────────────┘ │ │
                                                           │ │
OPERAÇÃO (8)                                               │ │
├── Implementar controles do SoA                           │ │
├── Executar avaliação periódica de riscos                 │ │
└── Executar PTR                                           │ │
                                                           │ │
AVALIAÇÃO DE DESEMPENHO (9)                                │ │
├── Monitoramento e medição (KPIs)                         │ │
├── Auditoria interna (imparcial)                          │ │
└── Revisão pela direção ────────────────────────────────► │ │
                                                           │ │
MELHORIA (10)                                              │ │
├── Não conformidades → ação corretiva (causa raiz)        │ │
└── Melhoria contínua ──────────────────────────────────── ┘ ┘
```

---

## Dicas Finais para a Prova

**Armadilhas comuns:**
1. Confundir ISO 27001 (requisitos) com ISO 27002 (guia) — a certificação é **apenas contra a 27001**
2. Confundir **correção** (trata o sintoma) com **ação corretiva** (elimina a causa raiz)
3. Esquecer que o SoA inclui **todos** os 93 controles — mesmo os excluídos devem estar listados com justificativa
4. Confundir **informação documentada para manter** (documentos) com **para reter** (registros/evidências)
5. Não conformidade ≠ incidente de SI. São processos distintos.
6. A auditoria interna pode ser feita por auditor **interno treinado** ou **externo contratado** — o que não pode é auditar o próprio trabalho.

**Perguntas frequentes estilo prova:**
- "Qual documento lista todos os controles com justificativa de aplicabilidade?" → **SoA**
- "O que a alta direção DEVE fazer no SGSI?" → recursos, política, revisão, integração na estratégia
- "Quais são as opções de tratamento de risco?" → modificar, evitar, compartilhar, aceitar (MECA)
- "Quantos controles tem o Anexo A da versão 2022?" → **93**
- "Qual a diferença entre auditoria de 1ª e 3ª parte?" → interna vs organismo independente
- "Quando ocorre uma não conformidade, qual é a sequência correta?" → reagir → analisar causa → implementar ação corretiva → verificar eficácia

---

*Documento gerado em 2026-06-20. Próximo material: `clausulas-4-10-detalhado.md` e `anexo-a-controles.md`.*
