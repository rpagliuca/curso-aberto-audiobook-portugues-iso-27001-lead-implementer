# ISO 27001 Lead Implementer — Roteiro dos capítulos extras
# 5 capítulos · ~5 min cada · ~25 min total
# Escrito para escuta, não leitura. Sem tabelas, sem listas.

---

## Extra 1 — A família de normas e os marcos vizinhos

Este é o primeiro de cinco capítulos extras. Eles cobrem assuntos que aparecem no curso e na prova de Lead Implementer, mas que ficaram de fora dos seis episódios principais. Cada um dura cerca de cinco minutos. Vamos começar pelo mapa das normas.

A ISO 27001 não anda sozinha. Ela pertence a uma família, e a prova espera que você saiba o papel de cada integrante. A ISO 27000 traz a visão geral e o vocabulário: é o dicionário da família. A ISO 27001 traz os requisitos, e é a única contra a qual uma organização é certificada. A ISO 27002 detalha os controles do Anexo A, com orientação para implementar cada um. A ISO 27003 orienta a implementação do próprio sistema de gestão, cláusula por cláusula. A ISO 27004 trata de monitoramento e medição. A ISO 27005 trata da gestão de riscos. E a ISO 27701 trata da gestão da privacidade da informação.

Guarde uma distinção que vale pontos: só a 27001 contém requisitos. As demais são diretrizes, escritas na linguagem da recomendação. Uma organização pode ser certificada sem seguir a 27002 ou a 27003 ao pé da letra. Se uma questão disser que o auditor abriu uma não conformidade apenas porque a empresa não seguiu uma orientação da 27003, desconfie. Diretriz não cria obrigação, a menos que a própria organização a tenha adotado como regra interna.

Há ainda duas normas voltadas a quem audita. A ISO 27006 define os requisitos para os organismos que certificam sistemas de gestão de segurança da informação. E a ISO 27007 orienta como auditar esses sistemas.

Agora, os marcos vizinhos, que não são normas ISO. O primeiro é o PCI DSS, o padrão de segurança de dados do setor de cartões de pagamento. Ele tem doze requisitos e vale para quem armazena, processa ou transmite dados de cartão. Não é lei: é uma obrigação contratual, imposta pelas bandeiras de cartão.

O segundo é o CSA STAR, um programa de garantia para provedores de nuvem. No nível um, o provedor faz uma autoavaliação e a publica. No nível dois, passa por uma auditoria independente, que pode ser feita junto com a certificação ISO 27001.

O terceiro grupo é o das leis de proteção de dados. Na Europa, o GDPR, aplicado desde maio de 2018. No Brasil, a LGPD. Aqui mora uma pegadinha clássica: ter a certificação ISO 27001 não significa cumprir automaticamente o GDPR, a LGPD ou o PCI DSS. O sistema de gestão ajuda a cumprir uma parte dessas exigências, porque obriga a identificar requisitos legais e contratuais e a tratar riscos. Mas cada marco tem exigências próprias, que a norma não cobre.

Por fim, quem certifica quem. No topo ficam os organismos de acreditação, que seguem a ISO 17011 e se reúnem no Fórum Internacional de Acreditação, o IAF. Eles avaliam os organismos de certificação. Os organismos que certificam sistemas de gestão seguem a ISO 17021-1. Os que certificam pessoas seguem a ISO 17024: é o caso da sua certificação de Lead Implementer. E os que certificam produtos, processos e serviços seguem a ISO 17065.

Um jeito simples de lembrar: a acreditação avalia quem certifica, e a certificação avalia quem implementa.

Duas perguntas para fixar.

Pergunta um: uma empresa certificada na ISO 27001 processa pagamentos com cartão. Ela pode afirmar a um cliente que, por causa da certificação, já está em conformidade com o PCI DSS? Pense. Não pode. São marcos diferentes, com exigências e avaliações próprias. A certificação ISO 27001 ajuda, mas a conformidade com o PCI DSS precisa ser demonstrada à parte.

Pergunta dois: qual norma define os requisitos para um organismo que certifica pessoas, como os profissionais de segurança da informação? Pense. A ISO 17024. A 17021-1 vale para sistemas de gestão, e a 17065, para produtos, processos e serviços.

Fechando este capítulo: a 27001 é a única da família com requisitos; as demais orientam. PCI DSS, CSA STAR, GDPR e LGPD são marcos vizinhos, que a certificação não substitui. E a cadeia de confiança vai da acreditação, pela 17011, até a certificação de sistemas, de pessoas e de produtos.

---

## Extra 2 — O projeto de implementação e quem decide

Neste segundo capítulo extra, o assunto é o projeto: como a implementação do SGSI começa, quem participa e quem decide.

Primeiro, uma separação importante. Implementar o SGSI é um projeto: tem começo, fim, orçamento e entregas. Operar o SGSI é rotina: não termina nunca. A prova de Lead Implementer olha principalmente para o projeto. Em organizações de porte médio, é comum que ele leve de seis a doze meses, do planejamento até o fim do primeiro ciclo de auditorias. E o principal fator de esforço é o tamanho do escopo.

Antes de começar, a alta direção precisa aprovar o projeto, e o instrumento para isso é o business case. Ele é o documento que justifica o investimento. Mostra os benefícios esperados, os custos, os riscos do projeto, as consequências financeiras da decisão e como o sucesso será medido. Sem ele, o projeto depende de boa vontade, e boa vontade acaba no primeiro corte de orçamento.

Para organizar o trabalho, o curso da PECB usa uma metodologia própria, chamada IMS2. Ela divide a implementação em fases, que acompanham o ciclo de planejar, executar, verificar e agir, e cada fase se desdobra em etapas, atividades e tarefas. Dois pontos sobre ela caem na prova. Primeiro: a metodologia é uma boa prática, não um requisito da norma. Segundo: ela não é rígida. A ordem das etapas pode mudar conforme a organização, e várias etapas são iterativas, ou seja, você volta a elas mais de uma vez.

Agora, as pessoas. O patrocinador é alguém da alta direção que defende o projeto e remove obstáculos. O gerente de projeto planeja, coordena e presta contas. E a equipe do projeto deve ser multidisciplinar: gente de TI, de recursos humanos, do jurídico e das áreas de negócio. Segurança da informação não é assunto só de tecnologia.

Dois cargos costumam confundir. O CISO é o executivo responsável pela segurança da informação: cuida dos riscos e do sistema de gestão. O CIO é o executivo responsável pela tecnologia da informação: cuida da operação e da entrega dos serviços de TI. Quando a segurança fica dentro do departamento de TI, a vantagem é reunir a competência técnica num lugar só. As desvantagens são a falta de independência, o conflito de interesse, porque quem opera também fiscaliza, e o risco de reduzir a segurança a um tema de tecnologia. Por isso, é comum o CISO responder diretamente à alta direção.

Vamos aos comitês. A norma não exige nenhum comitê pelo nome. O que ela exige, na cláusula 5.3, Papéis, responsabilidades e autoridades organizacionais, é que as responsabilidades de segurança sejam atribuídas e comunicadas. E, na cláusula 9.3, Análise crítica pela direção, que a alta direção analise o sistema em intervalos planejados. Na prática, três comitês aparecem. O comitê executivo, formado pela alta direção, aprova a política, os recursos e os riscos aceitos, e faz a análise crítica ao menos uma vez por ano. O comitê de segurança da informação reúne várias áreas, costuma ser presidido pelo CISO e acompanha o dia a dia do sistema. E o comitê diretor do projeto existe só enquanto dura a implementação: inclui pelo menos o patrocinador e o gerente de projeto, e decide sobre prazo, custo e escopo do projeto. A recomendação é aproveitar comitês que já existem, em vez de criar novos.

Duas perguntas para fixar.

Pergunta um: o gerente de projeto decide inverter a ordem de duas etapas da metodologia, porque a organização já tem um inventário de ativos pronto. Isso é uma não conformidade? Pense. Não é. A metodologia de implementação é uma boa prática, flexível e iterativa. Não conformidade é o descumprimento de um requisito, e a ordem das etapas não é requisito da norma.

Pergunta dois: numa empresa, o responsável pela segurança da informação responde ao gerente de infraestrutura de TI, que é avaliado pela disponibilidade dos sistemas. Qual é o principal problema dessa estrutura? Pense. A falta de independência. Há conflito de interesse: quem responde pela operação tende a priorizar a entrega, e a segurança fica sem voz para levar os riscos à alta direção.

Fechando este capítulo: o projeto de implementação tem começo e fim, e nasce de um business case aprovado. A metodologia organiza o trabalho, mas não é requisito. O patrocinador dá força, o gerente coordena e a equipe é multidisciplinar. E os comitês separam três níveis de decisão: o da alta direção, o da segurança e o do projeto.

---

## Extra 3 — Contexto, escopo e política na prática

O episódio dois apresentou o contexto, a liderança e o escopo. Este capítulo extra acrescenta as ferramentas e os detalhes que a prova gosta de cobrar.

Começando pela cláusula 4.1, Entendendo a organização e seu contexto. A norma pede que você determine as questões internas e externas que afetam o SGSI, mas não diz como. Três ferramentas clássicas ajudam. A análise SWOT cruza dois olhares: para dentro, as forças e as fraquezas; para fora, as oportunidades e as ameaças. A análise PEST olha só para fora, em quatro dimensões: política, econômica, social e tecnológica. E as Cinco Forças de Porter analisam a concorrência no setor: os rivais, os novos entrantes, os produtos substitutos, e o poder de negociação dos clientes e dos fornecedores. Nenhuma delas é obrigatória. O que a norma exige é o resultado: conhecer o contexto.

Desde 2024 há uma novidade nessa cláusula. Uma emenda à norma passou a exigir que a organização determine se a mudança climática é uma questão relevante para o seu sistema de gestão. Atenção ao verbo: determinar se é relevante. Se a conclusão for que não é, nada muda no SGSI. Mas convém manter essa conclusão registrada, para mostrar ao auditor que a análise foi feita.

Na cláusula 4.2, Entendendo as necessidades e expectativas das partes interessadas, a ferramenta típica é a matriz de poder e interesse. Você posiciona cada parte interessada conforme o poder que ela tem sobre a organização e o interesse que tem no SGSI. Quem tem muito poder e muito interesse, como um regulador ou um grande cliente, é gerenciado de perto. Quem tem pouco dos dois é apenas monitorado. Os requisitos dessas partes vêm de quatro fontes: leis e regulamentos, normas, contratos e exigências de mercado, e políticas internas. E a análise dos requisitos legais pede apoio jurídico: não é tarefa só do especialista em segurança.

Chegamos à cláusula 4.3, Determinando o escopo do SGSI. O escopo é delimitado por três tipos de limite. Os limites organizacionais: quais unidades, processos e responsabilidades estão dentro. Os limites dos sistemas de informação: quais redes, aplicações e bases de dados. E os limites físicos: quais prédios e instalações. Três cuidados aqui. Primeiro: o escopo precisa estar disponível como informação documentada, e o que fica de fora deve ser justificado. Segundo: nenhum requisito das cláusulas 4 a 10 pode ser excluído. O que se pode excluir, com justificativa, são controles do Anexo A, na Declaração de Aplicabilidade. Terceiro: o escopo deve fazer sentido para as partes interessadas. Certificar apenas uma área periférica e divulgar a certificação como se ela cobrisse o negócio inteiro engana o cliente.

Por fim, a cláusula 5.2, Política. As políticas costumam se organizar em três níveis. No topo, as políticas gerais da organização. No meio, a política de segurança da informação, aprovada pela alta direção. Na base, as políticas por tema, como controle de acesso, cópias de segurança ou trabalho remoto. Uma boa política responde por quê e o quê. O como fica para os procedimentos. Por isso, a política não cita produtos nem configurações: se citasse, teria de ser aprovada de novo a cada troca de ferramenta. Ela deve ser comunicada de forma acessível, com evidência de que as pessoas tomaram ciência, e revisada em intervalos planejados e sempre que houver mudança significativa.

Duas perguntas para fixar.

Pergunta um: uma organização analisou a mudança climática e concluiu que o tema não é relevante para o seu SGSI. Ela descumpriu a norma? Pense. Não. A exigência é determinar se o tema é relevante, e não tratá-lo como relevante. O recomendável é manter o registro dessa conclusão.

Pergunta dois: a política de segurança de uma empresa determina que todos os computadores portáteis usem um produto específico de criptografia, de um fabricante específico. O que há de errado? Pense. A política desceu ao nível do como. Ela deveria dizer o quê e por quê: os dispositivos portáteis devem ter os dados cifrados, para proteger a confidencialidade. O produto e a configuração pertencem a um procedimento ou a um padrão técnico.

Fechando este capítulo: a análise SWOT, a análise PEST e as Cinco Forças ajudam a entender o contexto. A matriz de poder e interesse prioriza as partes interessadas. O escopo tem limites organizacionais, de sistemas e físicos. E a política diz por quê e o quê, deixando o como para os procedimentos.

---

## Extra 4 — Documentos, treinamento, nuvem e inteligência artificial

Este capítulo extra completa o episódio quatro, sobre suporte e operação, com quatro pontos que rendem questões.

O primeiro são os verbos da norma. Nas normas ISO, cada verbo tem um peso. Shall, traduzido como deve, indica requisito. Should, traduzido como convém, indica recomendação. May indica permissão. E can indica possibilidade ou capacidade. Na versão em português, os dois últimos viram pode. A ISO 27001 é escrita com deve; a 27002, com convém. E cuidado com os seus próprios documentos: se um procedimento interno diz que o gestor deve revisar os acessos todo mês, isso passa a ser um requisito do seu SGSI. Descumprir é não conformidade, mesmo que a norma nunca tenha pedido revisão mensal.

Ainda na cláusula 7.5, Informação documentada: ela pode estar em qualquer formato e mídia. Um registro pode ser uma planilha, um log de sistema, um vídeo. Todo documento tem um ciclo de vida: é criado, classificado, revisado, aprovado, distribuído, usado, arquivado e, por fim, descartado. Duas boas práticas ajudam. Manter uma lista mestra, com todos os documentos e suas versões. E citar papéis em vez de nomes de pessoas, para que o documento não fique desatualizado quando alguém muda de cargo.

O segundo ponto é a cláusula 7.4, Comunicação. Você já sabe que é preciso definir o que comunicar, quando, com quem e como. Acrescente dois detalhes. Um: mensagens preparadas e aprovadas com antecedência, para incidentes e crises, evitam improviso no pior momento. Dois: não comunicar também tem custo, e ele costuma aparecer como dano à reputação.

O terceiro ponto é como avaliar um treinamento. A cláusula 7.2, Competência, exige avaliar a eficácia das ações tomadas para desenvolver competência. O modelo mais citado para isso é o de Kirkpatrick, com quatro níveis. Nível um, reação: os participantes gostaram do treinamento? Nível dois, aprendizado: eles aprenderam? Isso se mede com uma prova. Nível três, comportamento: mudaram a forma de trabalhar? Nível quatro, resultados: a organização melhorou, por exemplo com menos incidentes? Uma pesquisa de satisfação no fim do curso mede apenas o nível um. Uma simulação de phishing, semanas depois, mede o nível três.

O quarto ponto são as tecnologias. Na nuvem, há três modelos de serviço. No IaaS, infraestrutura como serviço, o provedor entrega servidores, rede e armazenamento, e o cliente cuida do sistema operacional para cima. No PaaS, plataforma como serviço, o provedor cuida também do sistema operacional e do ambiente de execução, e o cliente cuida das aplicações e dos dados. No SaaS, software como serviço, o provedor opera tudo, e o cliente apenas usa. Em todos eles vale o modelo de responsabilidade compartilhada: o provedor responde pela segurança da nuvem, e o cliente, pela segurança na nuvem. E, mesmo no SaaS, duas coisas continuam com o cliente: os dados e a gestão de quem tem acesso a eles.

Na inteligência artificial, a IA, vale conhecer as ameaças aos sistemas de aprendizado de máquina. Duas acontecem durante o treinamento: o envenenamento de dados, em que o atacante corrompe os dados usados para treinar, e o backdoor, um gatilho escondido no modelo. Outras acontecem com o modelo já em uso: os exemplos adversariais, que são entradas criadas para enganar o modelo; o roubo do modelo; e a extração dos dados de treinamento.

Duas perguntas para fixar.

Pergunta um: depois de um treinamento de conscientização, a empresa aplica uma pesquisa de satisfação e conclui que o treinamento foi eficaz. A conclusão se sustenta? Pense. Não. A pesquisa mede só a reação, o primeiro nível de Kirkpatrick. Para falar em eficácia, é preciso medir ao menos o aprendizado e, de preferência, a mudança de comportamento.

Pergunta dois: uma empresa usa um sistema de gestão de clientes no modelo SaaS. Um ex-funcionário continua com a conta ativa e copia dados. De quem é a falha? Pense. Da empresa cliente. No SaaS, o provedor opera a aplicação e a infraestrutura, mas a gestão dos acessos dos usuários e os dados são responsabilidade do cliente.

Fechando este capítulo: deve é requisito, convém é recomendação. Documentos têm ciclo de vida e lista mestra. Treinamento se avalia em quatro níveis. E, na nuvem, a responsabilidade é compartilhada, mas os dados são sempre seus.

---

## Extra 5 — Medição, auditoria, certificação e o dia da prova

Este último capítulo extra completa o episódio cinco e termina com o que esperar no dia do exame.

Começando pela cláusula 9.1, Monitoramento, medição, análise e avaliação. Toda medição parte de uma necessidade de informação, ou seja, de uma pergunta que alguém precisa responder. Sem pergunta, o indicador é só um número. Existem dois tipos de medida. A medida de desempenho verifica se o planejado foi feito: por exemplo, o percentual de funcionários treinados. A medida de eficácia verifica se o efeito desejado aconteceu: por exemplo, a queda nos cliques em mensagens de phishing simuladas. Treinar cem por cento das pessoas é desempenho; mudar o comportamento delas é eficácia. E vale a regra de ouro: poucos indicadores, bem escolhidos. Medir demais custa caro e esconde o que importa. A ISO 27004 orienta esse trabalho, mas, como diretriz, não cria requisitos.

Passando à cláusula 9.2, Auditoria interna. Existem três tipos de auditoria. A de primeira parte é a auditoria interna, feita pela própria organização ou em nome dela. A de segunda parte é feita por quem tem interesse na organização, como um cliente que audita o fornecedor. A de terceira parte é feita por um organismo independente, como na certificação. A referência para todas é a ISO 19011, a diretriz de auditoria de sistemas de gestão.

Não confunda programa com plano. O programa de auditoria é o conjunto das auditorias previstas para um período, em geral um ano ou um ciclo de três anos. O plano de auditoria descreve uma auditoria específica: datas, áreas e auditores. E a lógica de qualquer auditoria é uma cadeia. Os critérios são a referência. As evidências são os fatos coletados. A comparação entre os dois gera as constatações, de conformidade ou de não conformidade. E as constatações levam à conclusão. Sobre independência: o auditor interno não audita o próprio trabalho, e uma organização pequena pode contratar auditores externos para fazer a auditoria interna.

Agora, a certificação. O estágio um avalia o desenho do sistema e a documentação, e verifica se a organização está pronta. O estágio dois, realizado nas instalações, avalia se o sistema está implementado e é eficaz. Um detalhe que cai muito: o auditor não concede o certificado. Ele recomenda, e a decisão é do organismo de certificação, tomada por pessoas que não participaram da auditoria. Uma não conformidade maior impede a recomendação favorável até ser resolvida. As menores exigem um plano de ação corretiva. Depois da certificação, vêm as auditorias de supervisão, ao menos uma por ano, que cobrem parte do sistema, e a recertificação, ao fim do ciclo de três anos.

Por fim, o exame de Lead Implementer da PECB. Ele é de múltipla escolha, e parte das questões se apoia em cenários: você lê um caso curto e responde a perguntas sobre ele. O exame é com consulta. Você pode usar a norma, o material do curso e as suas anotações pessoais. Mas não se iluda: o tempo não permite procurar cada resposta. A consulta serve para confirmar um detalhe, não para aprender na hora. Ferramentas de inteligência artificial e gravações de tela são proibidas, e podem anular a prova. Antes de marcar o exame, leia as regras atualizadas no site da PECB, porque elas mudam.

Duas perguntas para fixar.

Pergunta um: uma empresa mede o número de sessões de conscientização realizadas no ano e, com base nisso, afirma que a conscientização é eficaz. O que falta? Pense. Falta uma medida de eficácia. Contar sessões é medir desempenho: mostra que o planejado foi feito. A eficácia exige medir o efeito, como a redução de incidentes causados por erro humano.

Pergunta dois: ao fim do estágio dois, o auditor líder diz que a organização está certificada. Ele pode afirmar isso? Pense. Não pode. O auditor apenas recomenda. A decisão de certificar pertence ao organismo de certificação, e é tomada por quem não participou da auditoria.

Fechando os capítulos extras: desempenho mostra que você fez; eficácia mostra que funcionou. O programa reúne as auditorias; o plano detalha uma delas. O estágio um olha o desenho; o estágio dois, a prática. E o auditor recomenda, mas quem decide é o organismo de certificação. Bons estudos e boa prova.
