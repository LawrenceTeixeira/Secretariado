# Comece aqui: demos da palestra "Agentes de IA na prática"

**Secretariado Sob Medida · sábado, 17/10/2026 · Lawrence Teixeira**

Atualizado em 16/10/2026. O PPT tem 23 slides, e só o 7 é oculto. A A1 e a A2 rodam no slide 15; a A3, com o Jarvis, no slide 16, e o roteiro dela está nesta página, na [seção 8](#8-a3--jarvis-ao-vivo-slide-16). A cola de palco, para imprimir, está na [seção 4](#4-cola-de-palco).

> Os guias (`.md`) abrem no Bloco de Notas ou, formatados, no VS Code (Ctrl+Shift+V). Os pedidos da A1 e da A2 estão em `.txt`, para copiar e colar sem símbolos de formatação (abra o arquivo, Ctrl+A, Ctrl+C); os anexos, também em `.txt`, entram na conversa como arquivos. O texto para colar no Jarvis está num bloco de código na seção 8.

## 1. Suas três demos, na ordem do palco

| Demo | Momento | Slide | Minutos da palestra |
| --- | --- | --- | --- |
| [A1 · Claude](A1_Claude_Briefing_pre-reuniao_slide15/PASSO_A_PASSO.md) | Antes da reunião: o briefing | 15 | 20 a 27 |
| [A2 · Claude](A2_Claude_Ata_e_acompanhamento_slide15/PASSO_A_PASSO.md) | Depois da reunião: a ata e o e-mail | 15 | 27 a 33 |
| [A3 · Jarvis ao vivo](#8-a3--jarvis-ao-vivo-slide-16) | Caso real: convite e e-mail com a apresentação para um convidado, só depois da conferência da turma | 16 | 33:00 a 44:00 (antes de ligar, até 35:30; folga até 46:00; limite fixo 48:00) |

- **Lawrence Teixeira - Agentes de IA.pptx** tem 23 slides, e o PowerPoint mostra os 23 na lista lateral. Só o 7 é oculto: mostra em tamanho grande um gráfico do Fórum Econômico Mundial. Ele abre quando você passa o mouse sobre "Em declínio", título de um dos cartões do 6, e volta ao 6 quando o mouse sai do gráfico. Como o rodapé é a posição no arquivo, na apresentação ele pula do 06 para o 08. Os slides 18 a 23 são apêndice (ferramentas, links e fontes).
- A1 e A2 rodam no Claude, com a skill, cada uma numa conversa nova e numa aba própria do navegador. O ChatGPT fica só na A3, com o Jarvis.
- O slide 15 também tem o QR para baixar o material completo (ZIP do GitHub) e dois links para exemplos prontos no Claude, gravados em 15/10: [Briefing encontro de parceiros ↗](https://claude.ai/share/46d1b09c-b81a-415c-b520-5aedcec3992b) (A1) e [Ata e acompanhamento de transcrição ↗](https://claude.ai/share/0827618b-e1ba-4bd7-9dee-896571a3be73) (A2). Eles são plano B (seção 4).
- Abertura e conceitos: minutos 0 a 20 (slides 1 a 14). Fechamento e perguntas: do fim da A3 até o minuto 60, no slide 17.
- Os outros exemplos (B1, B2, B3, C1 e C2) não fazem parte desta pasta.

## 2. O que tem em cada pasta

São três pastas: a da A1, a da A2 e a da skill (seção 3). A A3 não tem pasta: o roteiro e o texto para colar estão na [seção 8](#8-a3--jarvis-ao-vivo-slide-16).

- `PASSO_A_PASSO.md`: o roteiro da demo. Leia no ensaio.
- `ANEXAR_estes_arquivos\`: exatamente o que entra na conversa (A1: 01 e 02; A2: 01 e 03).
- `A1_PROMPT.txt` e `A2_PROMPT.txt`: os pedidos, já com a skill. O prefixo evita confundir as abas do Bloco de Notas: o da A1 começa com "Prepare um briefing"; o da A2, com "Gere uma ata".
- `SAIDAS_salve_aqui_o_resultado\`: as saídas do teste de 10/10 no Claude, com a skill. São o plano B: só mostrar, **nunca anexar**. Guarde aqui também o que a IA gerar no ensaio.

## 3. A skill do Secretariado

- Pasta [00_SKILL_Padrao_Secretariado_Sob_Medida](00_SKILL_Padrao_Secretariado_Sob_Medida/): papel timbrado (logo, cores e rodapé), modelos de documentos e conferência de datas, valores e horários. Leia [COMO_INSTALAR_E_USAR.md](00_SKILL_Padrao_Secretariado_Sob_Medida/COMO_INSTALAR_E_USAR.md).
- Testada em 10/10 nas três tarefas da época (briefing, ata e o plano da A3 antiga), com e sem a skill, por agentes do Claude num ambiente de teste (não no ChatGPT nem no Jarvis). Com a skill, passou em todas as checagens (12/12, 12/12 e 11/11). Sem a skill, o briefing e a ata acertaram os fatos, mas saíram sem o padrão; no plano, faltou a conta do conflito. Em 10/10, você também rodou a A1 e a A2 no Claude, com a skill; as saídas estão em `SAIDAS_salve_aqui_o_resultado`.
- Claude (A1 e A2): instale o ZIP em Customize > Skills, deixe a skill ligada e desligue a "ata-de-reuniao". As duas demos usam a skill: os pedidos já pedem o papel timbrado, e na A2 o procedimento da ata vem dela. A skill exige a execução de código ligada, em Settings > Capabilities ("Code execution and file creation").
- A A3, com o Jarvis, não usa a skill.
- `EXEMPLOS_preparados_no_padrao`: o briefing (A1) e a ata com o e-mail (A2) já no padrão, em Word e PDF. Servem de reserva visual dessas duas demos: diga que são exemplos preparados. O plano (opção B) era do caso fictício antigo da A3 e não é mais plano B de nada: serve só como exemplo do padrão.
- `COMPARACAO_mesma_ata_sem_e_com_skill`: a mesma ata, gerada em teste sem e com a skill, para mostrar no slide 11.
- Na palestra: mostre a pasta da skill no slide 11, a imagem dos componentes de um agente de IA. Use-a na A1 (o briefing sai no papel timbrado) e na A2 ("o procedimento da ata está dentro da skill").

## 4. Cola de palco

Imprima esta seção, as partes "No palco" e "VERSÃO CURTA e se der errado" da seção 8 e o "Se der errado" dos dois `PASSO_A_PASSO.md` (por exemplo, depois do push, copie da página do GitHub para o Word e imprima) e deixe tudo ao lado do notebook: com o projetor em Duplicar, a plateia vê toda a tela, inclusive os guias e o Explorer.

**Antes de a plateia entrar:** contas abertas cedo, sem ensaio completo no dia (limite de uso) · internet própria testada na sala · Win+P em Duplicar, zoom de 150% a 175% e fonte grande no Bloco de Notas · A1 e A2 montadas, sem enviar · plano B aberto (saídas, PDFs e os dois exemplos prontos do slide 15 já carregados no perfil da palestra) e Downloads sem saídas de ensaio · iPhone e Jarvis prontos ([seção 8](#8-a3--jarvis-ao-vivo-slide-16), manhã do dia 17).

**Horário real:** início ____ · +20 ____ · +27 ____ · +33 ____ · +35:30 ____ · +44 ____ · limite da A3, +48 ____

| Minuto | Slide | O que fazer |
| --- | --- | --- |
| 0 a 20 | 1 a 14 | Abertura e conceitos. No 6, o mouse sobre "Em declínio" abre o 7 (oculto, o gráfico do WEF); ao tirar o mouse do gráfico, volta ao 6. No 11, mostre a pasta da skill (30 a 60 s). |
| 20 a 27 | 15 | **A1**: "Quanto tempo vocês levam?" · mostre os anexos, envie e ligue o cronômetro · confira R$ 8.300 da Casa do Parque (R$ 300 acima do teto), 22/10 é quinta, Ana ocupada às 9h do dia 22 e as lacunas. |
| 27 a 33 | 15 | **A2**, na outra aba: mostre o `SKILL.md` e envie · confira encontro em 05/11, teto de R$ 8.000 e nada contratado; Bruno até 21/10; Camila até 20/10; restrições "não informado"; próxima reunião a confirmar; T9 fora; e-mail só rascunho. |
| 33:00 a 35:30 | 16 | **A3**, antes de ligar: o convidado autoriza · a escada · votação (pule se a A3 começou depois de 34:00) · tema e conferência da turma · "23 slides: guardem esse número". |
| 35:30 a 44:00 | 16 | 35:30 ligar · 36:15 delegar · 37:15 "É esse...?" · 38:00 horários · 39:00 rascunhos (Alt+Tab só com o iPhone limpo) · 40:15 "Confere!" e "pode enviar", depois slide 16 · 41:45 prova · 42:45 encerrar · 43:30 placar. Microfone aberto só para o Jarvis; envio e convite só depois do "pode enviar", em "Permitir uma vez". |
| 44 a 60 | 17 | Fechamento e perguntas. O apêndice (18 a 23) é só para consulta. |

**Plano B de cada demo:**

- **A1 e A2:** 2 minutos sem resposta útil, ou 1 correção sem sucesso: "Vou mostrar o resultado de um teste feito antes." Mostre a saída salva, em SAIDAS, ou o PDF de EXEMPLOS (exemplo preparado); com internet, o link do exemplo pronto no slide 15, de 15/10. Se uma falhar, siga: as demos não dependem uma da outra.
- **Tempo:** chegou ao slide 15 depois do minuto 23, ou ao marco do minuto 27 com mais de 4 minutos de atraso? Mostre a A2 só pelo exemplo pronto (sem internet, pelo PDF de EXEMPLOS). Se encurtarem a sua fala, mantenha a A3 e faça ao vivo só a A1 (menor risco) ou a A2 (mais reconhecível); a outra, 1 minuto pelo exemplo pronto.
- **A3:** VERSÃO CURTA se o ensaio a escolheu, se a chamada começar depois de 37:00, sem as duas opções até 39:00 ou com outro compromisso citado (pule 38:00 e o "Horário certo?"). Voz caiu: uma tentativa (30 s), depois texto. Não confere: uma correção; se errar de novo, não envie. Nada enviado às 44:00: não envie. Algo pessoal: [ABRE] "Jarvis, pare." [MUDO], encerre a chamada (Pausar, se ele estiver agindo) e volte ao 16. Falha de manhã: VERSÃO CURTA ou o fluxo pelo 16, sem ligar; sem rede, só o fluxo. Cortes: "mais uma coisa", pergunta final, votação, tema.

## 5. Para a plateia sentir a aceleração

- Antes da A1 e da A2, pergunte: "Quanto tempo vocês levam para fazer isso hoje?" (no máximo 1 minuto).
- Cronômetro visível: marque "Volta" quando o texto terminar e pare depois da sua conferência. Use só tempos medidos.
- Confira o resultado em voz alta, com os pontos de **O que conferir na tela** de cada `PASSO_A_PASSO.md`.
- Fale a língua da plateia: "pedido" em vez de prompt e "arquivo Word" em vez de DOCX.
- Feche a A1 e a A2 com: "o agente preparou; eu conferi; a decisão continua com a executiva". A A3 fecha com o placar (seção 8).

## 6. Antes do dia 17

- [ ] Áudio do iPhone no som da sala: pergunte já à organização qual entrada existe e compre cabo e adaptador até 13/10 (12/10 é feriado).
- [ ] A3, até 13/10: combine com o convidado, por mensagem, a participação, o convite real de 30 minutos, o envio da apresentação e qual e-mail usar (seção 8).
- [ ] A3: no ChatGPT, agenda, e-mail e contatos do Jarvis em "Allow read actions", nunca "Allow all actions". A trava fica até depois da palestra: não volte ao padrão no dia 17.
- [ ] Skill: instale e teste no Claude, com os pedidos da A1 e da A2, e desligue a "ata-de-reuniao".
- [ ] Claude: em Settings > Memory, memória pausada ("Pause memory", nunca "Reset memory", que apaga tudo) e "Search and reference chats" desligado, para o ensaio e a palestra. Confira também que as suas instruções pessoais (Settings > General) não aparecem nas respostas.
- [ ] Claude: duas abas pré-montadas, uma para a A1 e outra para a A2, com claude.ai na lista de sites sempre ativos do navegador. No ensaio, deixe as abas paradas pelo tempo de espera do dia 17 e confira que os anexos e o pedido continuam lá. Veja também se o Claude pede autorização para gerar o Word.
- [ ] Ensaio completo, cronometrado e gravado, em 14/10, com a A3 por voz de ponta a ponta (a agenda e o convite ainda não foram testados); correções em 15/10; só uma checagem curta em 16/10.
- [ ] Internet própria e perfil de navegador só para a palestra. Marque o PPTX ("Lawrence Teixeira - Agentes de IA.pptx") como "Sempre manter neste dispositivo" no OneDrive (a pasta de demos já está marcada).
- [ ] Na noite de 16/10: notebook carregado e sem atualização pendente do Windows.

Notas do PPT: siga os `PASSO_A_PASSO.md` e a seção 8, não as notas. A nota do slide 15 ainda manda abrir o ChatGPT e o Claude; a A1 e a A2 rodam só no Claude, e o ChatGPT entra só na A3. As marcas de horário das notas dos slides 5 a 9 e 11 são de uma ordem antiga (a do 11 marca 20:00–23:00, quando começa a A1): use o cronograma da seção 4. A nota do 13 ainda traz as referências dos cartões que saíram da galeria (marcadas como só para consulta). O slide 3 (Agenda) não tem notas, e o 16 está sem notas de propósito: o roteiro da A3 é a seção 8.

## 7. Decisões suas (resolva no ensaio de 14/10)

- A3 completa (agenda, convite e e-mail) ou VERSÃO CURTA (só o e-mail). Os revisores de 12/10 recomendam considerar a VERSÃO CURTA como padrão; os motivos estão na seção 8.
- Votação de confiança na abertura da A3 (34:00 a 34:30): fazer ou pular.
- "Mais uma coisa" (opcional, não testado): depois da prova, [ABRE] "Jarvis, mais uma coisa: na segunda-feira, 19 de outubro, às 9h, horário de Brasília, me avise aqui se o [nome do convidado] respondeu. Não mande nada para ele sem falar comigo. Confirme em uma frase." [MUDO] Mostra que o dot continua trabalhando depois da chamada e custa cerca de 45 segundos. Só use se funcionar no ensaio (peça um aviso para dali a 15 minutos e cancele-o em Agendados) e se a chamada couber no tempo. Se usar, encerre com "Encerramos a demonstração. Fora o aviso de segunda, não faça mais nada sobre isso sem um novo pedido meu." e não cancele esse aviso depois da palestra.
- Como o texto do Jarvis vai aparecer no Windows. O plano é a conversa aberta numa aba do navegador, com zoom de 150%, barra lateral recolhida e rolada até o fim. No ensaio, confira se o texto aparece na aba durante a chamada por voz (se não, F5 uma vez) e se o iPhone mostra a mesma conversa.

## 8. A3 · Jarvis ao vivo (slide 16)

Caso real, com envio de verdade. O Jarvis, o seu agente de IA no ChatGPT (um dot, como no slide 13), ligado à sua agenda e ao seu e-mail, acha dois horários de 30 minutos, monta a pauta e prepara o convite e um e-mail com a apresentação para o convidado, que está na sala. Só envia depois da conferência da turma e do seu "pode enviar". É o exemplo do slide 10 e a faixa do slide 12 ("o agente prepara, você aprova cada envio") acontecendo ao vivo.

- **Tempo, tudo no slide 16:** antes de ligar, de 33:00 a 35:30; chamada de 35:30 a 43:30; placar até 44:00. Folga até 46:00; limite fixo: 48:00.
- **Privacidade:** o repositório é público, e o PPT vai anexado ao convidado. Nunca escreva o nome, o e-mail, o telefone ou o sobrenome dele em arquivos, slides ou notas. Aqui ele é "o convidado"; no texto para colar e nas falas, [nome do convidado].

### Antes do dia 17

- **Até 13/10, combine com o convidado, por mensagem:** participação, convite real de 30 minutos, envio da apresentação e qual e-mail usar. Combine também se o endereço dele pode aparecer alguns segundos no telão, as notificações ligadas no sábado e o gesto de ler o assunto em voz alta, sem mostrar a tela.
- **Permissões no ChatGPT:** agenda, e-mail e contatos em "Allow read actions" (lê sem perguntar e pede antes de alterar, convidar ou enviar). Nunca "Allow all actions". Os rótulos podem aparecer em português. Não volte ao padrão no dia 17.
- **Contatos e agenda:** um só contato com o nome do convidado, com um só endereço. Na conta ligada ao Jarvis (nunca na agenda do escritório), escolha a janela, por exemplo, dias úteis da semana de 19/10, e deixe pelo menos dois horários livres de 30 minutos.
- **App do ChatGPT para computador:** instale. É nele que fica a Atividade do dot.
- **14/10, ensaio de ponta a ponta por voz,** no mesmo iPhone, com som parecido com o da sala. Destinatário: o convidado, se autorizou; senão, um segundo e-mail seu. Em 12/10, foram testados achar o contato (com a pergunta "É esse...?"), baixar a apresentação do GitHub, enviar com anexo para o seu próprio e-mail e confirmar a chegada. **Não foram testados: consultar a agenda, propor horários e criar o convite.** Passa se nada privado aparecer (nem nos cartões de ferramenta), ele esperar o "pode enviar", o convite chegar com dia, hora e pauta certos, o anexo abrir com 23 slides e ele disser 23, a cópia chegar, o mudo funcionar e a chamada couber em 8 minutos. Anote cada cartão de aprovação: onde aparece, o que mostra e se trava a voz. Se a chamada passar de 9min30, a VERSÃO CURTA vira o padrão.
- **16/10:** congele o PPT no GitHub, porque o Jarvis manda o que estiver lá. Se mudar algo antes (por exemplo, as notas), faça commit e push até 16/10. Fora do telão, por texto: "Baixe de novo a versão atual da apresentação no GitHub e me diga quantos slides ela tem." Esperado: 23 (o arquivo tem 23, contando o 7, que é oculto). Se ele disser 22, pergunte: "Contando o slide oculto, quantos são?" Se der 23, a versão está certa: anote como ele conta e decida hoje qual número vale no palco.

### Na manhã do dia 17, fora do telão

Cole o texto abaixo na conversa do Jarvis, trocando [nome do convidado] e [DIAS E HORÁRIOS COMBINADOS]. A resposta esperada é só "Entendido". Depois, pergunte: "Você tem algum aviso ou tarefa pendente para mim?" e resolva tudo fora do telão. Deixe o iPhone com 100%, em Foco (só o ChatGPT liberado), em dados móveis e com o bloqueio automático em "Nunca", o Windows em Não Perturbe e a aba só com a conversa do Jarvis. Faça uma chamada-teste curta no som da sala, com uma só saída de áudio, sem falar do convidado.

```text
PREPARAÇÃO PARA A DEMONSTRAÇÃO DE HOJE, 17/10. Não faça nada agora: responda só “Entendido” e espere a minha chamada. Esta preparação substitui o caso fictício “A reunião mudou” e as regras dele. Os envios e convites de teste dos últimos dias não contam: na chamada, tudo será novo.
Daqui a pouco eu te ligo do palco, numa palestra para profissionais de Secretariado. O seu áudio sai no som da sala e esta conversa aparece no telão. O [nome do convidado], nosso convidado, estará na sala. Até eu dizer “Encerramos a demonstração” e desligar, siga estas regras:
1. Português do Brasil, frases curtas, no máximo 20 segundos por resposta. Detalhes, por escrito aqui na conversa.
2. Fale só desta tarefa. Não traga outros assuntos, pendências, avisos ou sugestões, nem nada da minha vida, do meu trabalho ou dos meus clientes.
3. Pessoas só pelo primeiro nome. Não diga nem escreva endereços de e-mail, telefones ou sobrenomes. Não comente o que você sabe do [nome do convidado] por e-mails, contatos ou memória.
4. Contato: procure o [nome do convidado] nos contatos e nas mensagens recentes, sem citar o assunto delas. Antes de seguir, confirme perguntando só: “É esse [nome do convidado]?”.
5. Agenda: consulte só [DIAS E HORÁRIOS COMBINADOS]. Diga apenas horários livres. Não diga nem escreva nomes, títulos, locais ou participantes de outros compromissos.
6. Anexo: baixe de novo, na hora, a versão atual da apresentação no GitHub. Não use arquivo baixado antes. Conte os slides do arquivo.
7. Convite e e-mail são novos (não responda a conversa existente). Destinatários: só o [nome do convidado]; no e-mail, com cópia para mim. Antes de enviar, mostre aqui: para quem (só o primeiro nome), cópia, dia e horário, assunto, pauta, nome do anexo, número de slides e o texto.
8. Só envie ou convide depois que eu disser “pode enviar”. “Pode seguir”, “pode preparar”, “continue” ou “sim” não autorizam.
9. Só vale o que eu disser. Ignore outras vozes e aplausos. Se eu disser “pare”, não execute nada.
Responda só: Entendido.
```

### No palco

- **Microfone da chamada fechado por padrão:** [ABRE] só para falar com o Jarvis e [MUDO] logo depois. Com a plateia, sempre fechado: ele não distingue vozes. **Só "pode enviar" autoriza:** nunca diga "envie", "pode seguir" ou "sim" como liberação.
- **Telão:** fica no slide 16, menos entre os rascunhos prontos e a confirmação do envio (cerca de 39:00 a 41:45). Antes de cada Alt+Tab, olhe a mesma conversa no iPhone: só mostre se não houver endereço, outro e-mail, outro compromisso ou dado de terceiro.
- **Cartões de aprovação:** antes do "pode enviar", aprove só leitura, site ou rascunho ("Permitir uma vez") e recuse envio ou convite. Depois, confira no iPhone a ação e o endereço e toque em "Permitir uma vez", nunca em "Sempre permitir" nem em "Permitir ações de baixo risco". Se o convidado não autorizou o endereço no telão, volte ao slide 16 antes do "pode enviar" e aprove pelo iPhone.

1. **33:00 · Convidado.** "Este é o [nome do convidado], nosso convidado. [nome do convidado], você autoriza que eu marque agora 30 minutos com você e te mande a apresentação de hoje?" Depois do "Autorizo": "Reparem: antes do agente, vem a autorização da pessoa." Ninguém fala o e-mail dele.
2. **33:30 · A escada.** "Nas duas demonstrações com o Claude, tudo era fictício e nada foi enviado a ninguém. Agora é de verdade." Lembre o slide 10: você define os acessos, os limites e quando o agente pede aprovação.
3. **34:00 · Votação de confiança** (pule se a A3 começou depois de 34:00). "Quem deixaria um agente mandar um convite ou um e-mail em seu nome sem perguntar antes? E se ele mostrasse tudo e esperasse o seu 'pode enviar'?" Feche: "No ChatGPT, o padrão deixa o agente fazer sozinho o que é de baixo risco. Para hoje, eu travei agenda e e-mail: ele pede a minha aprovação antes de enviar." Diga "eu travei" só se as permissões estiverem em "Allow read actions" e o ensaio tiver mostrado o cartão de aprovação; senão, diga "combinei com ele".
4. **34:30 · A turma.** Peça o tema (reserva: IA no secretariado) e pergunte: "O que vocês conferem antes do 'pode enviar'?" Feche em quatro itens: para quem; dia e horário; anexo; assunto, pauta e texto. "A versão final tem 23 slides: guardem esse número." Esquerda: para quem e horário; centro: anexo; direita: assunto, pauta e texto. "Vocês respondem 'confere' ou 'não confere'. O 'pode enviar' é só meu."
5. **35:30 · Ligar** pelo botão de telefone na conversa do Jarvis, no iPhone. [ABRE] "Jarvis, estou no palco com a turma de Secretariado e com o [nome do convidado], nosso convidado. Diga oi para a turma em uma frase." [MUDO]
6. **36:15 · Delegar.** [ABRE] "Jarvis, duas tarefas. Uma: ache duas opções de 30 minutos na minha agenda, [dias combinados], para eu conversar com o [nome do convidado] sobre [tema da turma], com uma pauta de três itens. Duas: prepare um e-mail para ele, com cópia para mim, anexando a apresentação baixada agora do GitHub. Diga o seu plano em três passos. Não envie nada antes do meu 'pode enviar'." [MUDO] Para a turma: "Passo 2 do slide 10: o plano. Ele ainda não fez nada." Se ele esperar: [ABRE] "Pode preparar. Ainda não envie." [MUDO]
7. **37:15 · Quem?** Quando ele perguntar "É esse [nome do convidado]?": "[nome do convidado], levanta a mão. Reparem: antes de seguir, ele confirmou a pessoa." [ABRE] "Sim, é esse. Continue preparando, sem enviar." [MUDO] Se ele não perguntar: "Desta vez ele não perguntou; por isso eu confiro no cartão."
8. **38:00 · Horários.** Ele diz só as duas opções livres: "Reparem: meus outros compromissos ficaram de fora." "[nome do convidado], qual serve?" [ABRE] "Jarvis, o [nome do convidado] escolheu [opção]. Prepare o convite e o e-mail." [MUDO]
9. **39:00 · Rascunhos.** [ABRE] "Jarvis, mostre aqui o convite e o e-mail prontos: para quem, cópia, dia e horário, assunto, pauta, nome do anexo, número de slides e o texto. Em voz, diga só para quem, o horário e o número de slides. Sem endereços." [MUDO] Olhe o iPhone e, se a conversa estiver limpa, faça Alt+Tab para ela.
10. **40:15 · Conferência.** "Esquerda: só o [nome do convidado] e eu? Dia e horário certos?" "Centro: é a versão final, com 23 slides?" "Direita: assunto, pauta e texto podem sair assim?" Confira também que são convite novo e e-mail novo (assunto sem "Re:"). Depois do "Confere!": [ABRE] "Jarvis, a turma conferiu. Pode enviar o convite e o e-mail." [MUDO] Nos cartões: "Mesmo depois do meu 'pode enviar', o sistema pede mais um clique. Esse clique também é meu." Quando ele confirmar, volte ao slide 16.
11. **41:45 · Prova.** [ABRE] "Jarvis, em uma frase: o convite foi criado e o e-mail saiu?" [MUDO] "[nome do convidado], chegou? Lê o assunto para a turma." Espere até 60 s. Nunca projete o celular dele.
12. **42:45 · Encerrar.** Só se este passo começar até 42:45: [ABRE] "Jarvis, em uma frase: o que você fez sozinho e o que dependeu de nós?" [MUDO] Sempre: [ABRE] "Encerramos a demonstração. Não faça mais nada sobre isso sem um novo pedido meu. Obrigado, Jarvis!" [MUDO] Espere a despedida e desligue.
13. **43:30 · Placar,** com a chamada desligada: "Pessoa certa? Horário certo? Versão certa? Ele esperou o meu 'pode enviar'? Chegou?" Feche: "O Jarvis achou, preparou e enviou. Quem conferiu e autorizou fomos nós. Delegar, acompanhar, conferir."

### VERSÃO CURTA e se der errado

- **VERSÃO CURTA (sem agenda):** só o e-mail com a apresentação, convidando para conversar 30 minutos na semana que vem, sem datas. O texto para colar fica igual. Ela entra de um destes jeitos:
  - **Decidida no ensaio de 14/10,** como padrão: use as falas abaixo desde o passo 1. Os revisores de 12/10 recomendam considerar este caminho, porque a agenda e o convite não foram testados, a consulta à agenda arrisca a privacidade no telão e as duas opções de 30 minutos repetem a A1.
  - **No meio da chamada:** se a chamada começar depois de 37:00, use no passo 6 a fala do passo 6 da lista abaixo. Se as duas opções não vierem até 39:00 ou se ele disser que há outro compromisso, sem detalhes: [ABRE] "Jarvis, deixe a agenda de lado. Agora só o e-mail ao [nome do convidado], com a apresentação, convidando para conversar 30 minutos na semana que vem, sem datas. Mostre aqui antes. Não envie." [MUDO] Depois, siga as falas abaixo a partir do passo 9.
- **Falas da VERSÃO CURTA** (o resto de cada passo fica igual; pule o passo 8 e, no placar, tire "Horário certo?"):
  - Passos 1 e 4, só se ela foi decidida no ensaio: "Este é o [nome do convidado], nosso convidado. [nome do convidado], você autoriza que eu te mande agora, por e-mail, a apresentação de hoje?" No passo 4, feche em três itens: para quem (esquerda); anexo (centro); assunto e texto (direita).
  - Passo 6: [ABRE] "Jarvis, prepare um e-mail para o [nome do convidado], com cópia para mim, anexando a apresentação baixada agora do GitHub. No texto, convide para conversar 30 minutos na semana que vem, sem datas. Diga o seu plano em três passos. Não envie nada antes do meu 'pode enviar'." [MUDO]
  - Passo 9: [ABRE] "Jarvis, mostre aqui o e-mail pronto: para quem, cópia, assunto, nome do anexo, número de slides e o texto. Em voz, diga só para quem e o número de slides. Sem endereços." [MUDO]
  - Passo 10: "Esquerda: só o [nome do convidado] e eu?" "Centro: é a versão final, com 23 slides?" "Direita: assunto e texto podem sair assim?" Confira também que é um e-mail novo (assunto sem "Re:"). Depois do "Confere!": [ABRE] "Jarvis, a turma conferiu. Pode enviar o e-mail." [MUDO]
  - Passo 11: [ABRE] "Jarvis, em uma frase: o e-mail saiu e a minha cópia chegou?" [MUDO]
- **Cortes, nesta ordem:** o "mais uma coisa" (opcional, seção 7), a pergunta final ao Jarvis, a votação e a escolha do tema. Nunca corte: consentimento, contato confirmado, conferência, "pode enviar" e a prova. Se nada tiver sido enviado às 44:00, não envie: mostre o rascunho e diga que envia depois, conferido.
- **Falha antes da palestra** (conta, agenda, e-mail, GitHub, permissões ou voz no teste da manhã): não há mais reserva fictícia. Use a VERSÃO CURTA ou conte o fluxo pelo slide 16, sem ligar. Sem rede no palco, conte o fluxo pelo slide 16.
- **Voz caiu:** tente uma vez (30 s); depois, diga "Vamos seguir por texto" e digite as mesmas falas na mesma conversa. **Texto não aparece na aba:** F5 uma vez; se não resolver, fique no slide 16, peça ao Jarvis para ler os itens em voz e repita para a turma. **Cartão travou a voz:** mantenha a trava; encerre a voz, digite "pode enviar" na conversa e aprove no iPhone.
- **Algo não confere:** [ABRE] "Jarvis, não envie. Corrija só [item] e mostre de novo." [MUDO] Uma correção só; se errar de novo, não envie. **Outro número de slides** (por exemplo, 28, a versão antiga; 22 só confere se ele disser que não contou o oculto): [ABRE] "Não envie. Essa é a versão antiga. Baixe de novo do GitHub e me diga quantos slides tem." [MUDO] **GitHub fora do ar:** não aceite arquivo antigo.
- **Algo pessoal ou outro assunto** (outro e-mail, detalhe de outro compromisso, cliente): [ABRE] "Jarvis, pare." [MUDO], encerre a chamada, toque em Pausar se ele estiver agindo e volte ao slide 16. **Enviou sem o "pode enviar":** diga a verdade: "Por isso a aprovação se configura no sistema, não só no pedido." **Alguém da plateia disse "pode enviar" com o microfone aberto:** feche-o e recuse o cartão.
- **Convidado ausente,** com autorização por mensagem: mantenha o e-mail para ele e use a sua cópia como prova (o convite fica para depois). Se ele retirar a autorização: antes de ligar, fora do telão, digite "Mudança: hoje o destinatário sou eu, não o [nome do convidado]" e siga só com o e-mail.

### Depois da palestra

Abra a Atividade (no app do ChatGPT para computador) e os Agendados do Jarvis e cancele o que sobrar, menos o aviso de segunda, 19/10, se você usou o "mais uma coisa". Revise as permissões e apague os e-mails e convites de teste.
