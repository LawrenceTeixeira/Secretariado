# A2 · Claude · Ata e acompanhamento da reunião

**Slide 15** · Tempo de palco: 6 minutos (minutos 27 a 33 da palestra) · Origem: Kit_Ensaio_Secretariado

Todos os dados são fictícios. Nada é enviado, agendado, reservado ou pago.

> **Mudanças de 12/10/2026:** saíram o slide 7 (superinteligência) e os slides ocultos; entrou o slide 11 (agentes de trabalho). O deck tem 23 slides: esta demo passou do slide 16 para o 15 (a A1 está no 14), e a pasta foi renomeada.
>
> **Mudanças de 11/10/2026:** esta demo usa a skill padrao-secretariado-sob-medida, que traz o procedimento da ata. Por isso, entram só 2 anexos (01 e 03), e ficou um pedido só, `A2_PROMPT.txt`. Saíram o `04_procedimento_ata.txt`, o pedido sem skill, o de correção e a pasta de reserva; o plano B agora é a ata salva em `SAIDAS_salve_aqui_o_resultado` ou o exemplo em PDF. A nota desta demo (hoje, slide 15) ainda manda anexar e mostrar o 04; vale este roteiro. À tarde, com o slide novo 7 (superinteligência), esta demo passou do slide 15 para o 16 e a pasta foi renomeada.

## Tarefa do dia a dia

Depois da reunião, transformar a transcrição em ata curta, lista de tarefas com responsável, prazo e origem, e rascunho de e-mail de acompanhamento, tudo para revisar antes de enviar.

## Entra na conversa

- Anexe só os 2 arquivos da pasta [ANEXAR_estes_arquivos](ANEXAR_estes_arquivos/): `01_manual_executivo.txt` e `03_transcricao_reuniao.txt`.
- Cole o texto de [A2_PROMPT.txt](A2_PROMPT.txt). Copie o texto; não anexe o arquivo.
- O procedimento da ata não vai anexado: ele está dentro da skill, em `references\modelos\ata.md`. Diga o que foi usado de verdade: a skill instalada.

> **Nunca anexe:** as fontes e a agenda da demo A1 (a ata recebe só 01 e 03), a pasta inteira, este `PASSO_A_PASSO.md`, o arquivo `A2_PROMPT.txt` (cole o texto), nada de `SAIDAS_salve_aqui_o_resultado`.

## Antes de subir ao palco

- Use o deck "Lawrence Teixeira - Agentes de IA.pptx". Desde 12/10/2026, ele tem 23 slides, nenhum oculto. Esta demo entra no slide 15.
- Entre na conta do Claude antes de projetar. Feche e-mail, agenda e abas pessoais. Desative as notificações no Windows e no iPhone. Confira que a projeção não mostra dados pessoais.
- **Skill:** a padrao-secretariado-sob-medida precisa estar ligada no Claude, em Customize > Skills, e a "ata-de-reuniao" da sua conta, desligada: as duas disputariam o mesmo pedido de ata. A skill exige a execução de código ligada, em Settings > Capabilities ("Code execution and file creation"). Instale só `padrao-secretariado-sob-medida.zip`, não o plugin: a skill não é plugin nem conector e não dá acesso a contas (slide 10).
- Deixe aberto no Bloco de Notas o [SKILL.md](../00_SKILL_Padrao_Secretariado_Sob_Medida/padrao-secretariado-sob-medida/SKILL.md) da skill (para o passo 3). Abra o `A2_PROMPT.txt` só depois de fechar os .txt da A1. Em outras janelas, deixe abertos os dois arquivos do plano B: `SAIDAS_salve_aqui_o_resultado\Ata_reuniao_15-10-2026.docx` (saída do teste de 10/10) e o [A2_Ata_e_email_exemplo_preparado.pdf](../00_SKILL_Padrao_Secretariado_Sob_Medida/EXEMPLOS_preparados_no_padrao/A2_Ata_e_email_exemplo_preparado.pdf).
- No ensaio, aprenda a abrir conversa nova, anexar TXT e abrir a resposta no Claude. Os nomes dos controles podem variar. Confira se o Word sai no papel timbrado e se o Claude pede autorização antes de gerá-lo. Não instale plugins nem conecte contas.
- Ensaie a conferência de Bruno, Camila, restrições alimentares e a data aberta. Se o ensaio gerar uma saída melhor, guarde-a em `SAIDAS_salve_aqui_o_resultado`.
- No ensaio, teste o plano B com a rede desligada: abra a ata salva e o PDF de exemplo e localize as tarefas e o rascunho de e-mail. Religue a rede depois.
- Recomendação nova (fora do kit): pré-monte a conversa antes de a plateia entrar. Abra uma conversa nova no Claude, anexe os 2 arquivos e cole o pedido, sem enviar. No palco, mostre os anexos, faça o passo 3 e envie. A A1 também roda no Claude: deixe a A2 numa aba própria do navegador e não recarregue as abas.
- Recomendação nova: abra os .txt de uma demo por vez. Os pedidos começam diferente: o da A1 com "Prepare um briefing", o da A2 com "Gere uma ata". Confira o começo antes de enviar.
- Recomendação nova: pause a memória do Claude para o ensaio e para a palestra, como no roteiro da A1 ("Pause memory", nunca "Reset memory", e "Search and reference chats" desligado). A A1 e a A2 contam a mesma história, e a memória pode trazer para a ata dados dos ensaios ou da A1, como horários da agenda, que aqui não podem aparecer.

## No palco, passo a passo

1. Abra uma conversa nova no Claude. Não reutilize a conversa do briefing.
2. Anexe somente os 2 arquivos de `ANEXAR_estes_arquivos`: `01_manual_executivo.txt` e `03_transcricao_reuniao.txt`.
3. Mostre o `SKILL.md` por alguns segundos (o passo a passo da ata fica em `references\modelos\ata.md`). Diga: "Reparem que não anexei o procedimento da ata: ele está dentro da skill instalada. É o como fazer do slide 10."
4. Abra `A2_PROMPT.txt` no Bloco de Notas, Ctrl+A, Ctrl+C, cole na conversa e envie.
5. Quando a resposta chegar, mostre as tarefas. Abra `ANEXAR_estes_arquivos\03_transcricao_reuniao.txt` e confira T3, T5 e T6.
6. Mostre o rascunho do e-mail. Abra o Word se estiver pronto e mostre o papel timbrado. Encerre e volte ao deck.

**Fechamento:** "A ata organiza o que foi dito. Quem revisa precisa conferir responsáveis, prazos e o que ficou em aberto."

## O que conferir na tela

- **Decisões:** encontro mantido em 05/11/2026, teto de R$ 8.000 e nenhuma contratação naquela reunião [T1 e T3].
- **Bruno:** confirmar capacidade para 34 pessoas e cancelamento da Horizonte até 21/10/2026 [T3 e T4]. **Camila:** revisar a lista até 20/10/2026 [T5].
- **Restrições alimentares:** responsável e prazo "não informado" [T6]. A terceira proposta também segue pendente, sem responsável atual ou prazo definidos em T4.
- **Próxima reunião:** data a confirmar, sem horários livres inventados, porque a agenda não entra nesta conversa. "Sexta-feira, dia 22" é contraditório.
- O comentário pessoal de T9 fica de fora. O e-mail continua como rascunho, com assunto e até 120 palavras.
- **Word no padrão:** logo no cabeçalho, faixa "Rascunho para revisão", seção "O que depende de revisão humana" e rodapé com a marca, com os mesmos fatos acima.
- A tabela do slide 15 é um exemplo preparado com as mesmas três tarefas. A resposta ao vivo pode usar outras palavras; o que vale são estes fatos.

## Se der errado

- Erro em responsável, prazo ou horário: peça uma única correção, por exemplo: "Confira T3, T5 e T6. Corrija responsáveis e prazos usando apenas esses trechos. Remova horários sem fonte e mantenha a próxima reunião como data a confirmar."
- Após 2 minutos sem resposta útil, ou uma correção sem sucesso, pare. Diga: "Vou mostrar o resultado de um teste feito antes, para continuarmos a conferência."
- Abra `SAIDAS_salve_aqui_o_resultado\Ata_reuniao_15-10-2026.docx`, a ata do teste de 10/10 no Claude, com a skill. Diga que é de um teste anterior. Na revisão humana, ela pede para conferir a data da reunião (15/10), posterior à data de preparo (10/10). Se perguntarem, diga que foi a IA que notou a data. Ela tem 4 tarefas, e não 3 como o slide 15: a quarta vem de T8 (verificar a data e a agenda de Ana). O e-mail fica na página 2. Mostre os mesmos pontos e volte ao deck no horário previsto. Se o Word não abrir, mostre o [A2_Ata_e_email_exemplo_preparado.pdf](../00_SKILL_Padrao_Secretariado_Sob_Medida/EXEMPLOS_preparados_no_padrao/A2_Ata_e_email_exemplo_preparado.pdf) e diga que é um exemplo preparado.
- Skill que não carrega ou Word atrasado: siga com o texto da conversa. Não troque de pedido nem mexa na skill no palco.
- Com a skill, o texto completo pode chegar só depois do Word: o `SKILL.md` manda gerar o arquivo antes de entregar a resposta. No ensaio, cronometre o tempo até o texto completo e ajuste por ele o limite de 2 minutos.
- Atenção: os horários da agenda F4 pertencem à demo A1. Aqui eles não podem aparecer como disponibilidade confirmada.

## Arquivos desta pasta

- `PASSO_A_PASSO.md`: este roteiro. Nunca anexar.
- [`ANEXAR_estes_arquivos\01_manual_executivo.txt`](ANEXAR_estes_arquivos/01_manual_executivo.txt): regras da executiva Ana (estilo, e-mail de até 120 palavras, "não informado"). **Anexar.**
- [`ANEXAR_estes_arquivos\03_transcricao_reuniao.txt`](ANEXAR_estes_arquivos/03_transcricao_reuniao.txt): transcrição fictícia da reunião de 15/10/2026, trechos T1 a T10. **Anexar.**
- [`A2_PROMPT.txt`](A2_PROMPT.txt): pedido da demo, já com a skill. Colar o texto.
- [`SAIDAS_salve_aqui_o_resultado\Ata_reuniao_15-10-2026.docx`](SAIDAS_salve_aqui_o_resultado/Ata_reuniao_15-10-2026.docx): ata e e-mail do teste de 10/10 no Claude, com a skill. Plano B: só mostrar, nunca anexar. Guarde nesta pasta também o que a IA gerar no ensaio.

## Sugestões para a plateia sentir a aceleração

Novas e opcionais; não estão no kit.

- Frase de entrada: "Depois da reunião: mesmo manual da executiva, outra tarefa."
- Limite a participação da plateia a 1 minuto no total.
- Antes de enviar, pergunte: "Quanto tempo vocês levam para fazer uma ata como esta e o e-mail de acompanhamento?"
- Cronômetro visível ao enviar, como na A1: clique em "Volta" quando o texto terminar e pare depois da conferência. Diga os dois tempos medidos.
- Enquanto o Claude trabalha, pergunte: "Quem lembra do problema do dia 22? Vejam se ele volta." e "O que não deveria entrar numa ata?" (o comentário pessoal de T9).
- Essa caça ao erro só funciona se a tabela do slide 15 e a frase sobre a data da próxima reunião entrarem por clique. Hoje o PPT não tem animação. Sem isso, mostre o slide 15 só depois da resposta ou pule as perguntas.
- Na fala, chame o procedimento da ata, que está dentro da skill, de "procedimento padrão, como um POP": é o tipo de instrução que vira uma skill. Diga "pedido" em vez de prompt.
