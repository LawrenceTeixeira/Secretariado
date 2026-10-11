# Comece aqui: demos da palestra "Agentes de IA na prática"

**Secretariado Sob Medida · sábado, 17/10/2026 · Lawrence Teixeira**

Atualizado em 11/10/2026. A A1 passou do ChatGPT para o Claude. A A1 e a A2 usam a skill, com um pedido só cada uma. As reservas saíram: o plano B agora é a saída salva em `SAIDAS_salve_aqui_o_resultado` ou o exemplo em PDF. O PPT com os slides 16 a 18 ocultos agora se chama "Lawrence Teixeira - Agentes de IA.pptx"; o original, com todos os slides visíveis, ficou no histórico do Git (commit d0163f4).

> Os guias (`.md`) abrem no Bloco de Notas ou, formatados, no VS Code (Ctrl+Shift+V) e no painel. Os pedidos, as falas e os anexos continuam em `.txt`, para copiar e colar sem símbolos de formatação.

## 1. Suas três demos, na ordem do palco

| Demo | Momento | Slide | Minutos da palestra |
| --- | --- | --- | --- |
| [A1 · Claude](A1_Claude_Briefing_pre-reuniao_slide14/PASSO_A_PASSO.md) | Antes da reunião: o briefing | 14 | 20 a 27 |
| [A2 · Claude](A2_Claude_Ata_e_acompanhamento_slide15/PASSO_A_PASSO.md) | Depois da reunião: a ata e o e-mail | 15 | 27 a 33 |
| [A3 · Jarvis por voz](A3_Jarvis_voz_Reuniao_mudou_slides19-20/PASSO_A_PASSO.md) | Quando a reunião muda, com votação da plateia | 19 e 20 | Slide 19 de 33 a 36; chamada de 36 a 50, com 2 minutos de folga |

- Os slides 16, 17 e 18 (fornecedores, viagem e limites) estão ocultos em **Lawrence Teixeira - Agentes de IA.pptx**: o PowerPoint pula esses slides (para mostrar um deles, digite o número e tecle Enter).
- A1 e A2 rodam no Claude, com a skill, cada uma numa conversa nova e numa aba própria do navegador. O ChatGPT fica só na A3, com o Jarvis.
- Fechamento e perguntas: minutos 50 a 60.
- Os outros exemplos (B1, B2, B3, C1 e C2) não fazem parte desta pasta.

## 2. O que tem em cada pasta

- `PASSO_A_PASSO.md`: o roteiro da demo. Leia no ensaio.
- `ANEXAR_estes_arquivos\`: exatamente o que entra na conversa (A1: 01 e 02; A2: 01 e 03). Na A3 não se anexa nada: o caso fica em `COLAR_na_conversa_antes_da_chamada\` (colar o texto antes da chamada).
- `A1_PROMPT.txt` e `A2_PROMPT.txt`: os pedidos, já com a skill. O prefixo evita confundir as abas do Bloco de Notas: o da A1 começa com "Prepare um briefing"; o da A2, com "Gere uma ata".
- Na A3: `FALAS_para_copiar\` (falas 0 a 5; a 6 é opcional, com a skill; a X é a correção de horário, sugestão nova).
- `SAIDAS_salve_aqui_o_resultado\`: na A1 e na A2, as saídas do teste de 10/10 no Claude, com a skill. São o plano B: só mostrar, **nunca anexar**. Guarde aqui também o que a IA gerar no ensaio.
- Em 11/10, saíram os pedidos sem skill e de correção, o `04_procedimento_ata.txt`, a pasta `ANEXAR_com_skill_estes_arquivos` e as pastas `RESERVA_plano_B_nao_anexar` das três demos. Eles continuam no histórico do Git.

## 3. A skill do Secretariado (nova)

- Pasta [00_SKILL_Padrao_Secretariado_Sob_Medida](00_SKILL_Padrao_Secretariado_Sob_Medida/): papel timbrado (logo, cores e rodapé), modelos de documentos e conferência de datas, valores e horários. Leia [COMO_INSTALAR_E_USAR.md](00_SKILL_Padrao_Secretariado_Sob_Medida/COMO_INSTALAR_E_USAR.md).
- Testada em 10/10 nas três tarefas, com e sem a skill, por agentes do Claude num ambiente de teste (não no ChatGPT nem no Jarvis). Com a skill, passou em todas as checagens (12/12, 12/12 e 11/11). Sem a skill, o briefing e a ata acertaram os fatos, mas saíram sem o padrão; no plano do Jarvis, faltou a conta do conflito (40 minutos para uma pauta de 60). Em 10/10, você também rodou a A1 e a A2 no Claude, com a skill; as saídas estão em `SAIDAS_salve_aqui_o_resultado`.
- Claude (A1 e A2): instale o ZIP em Customize > Skills, deixe a skill ligada e desligue a "ata-de-reuniao". As duas demos usam a skill: os pedidos já pedem o papel timbrado, e na A2 o procedimento da ata vem dela. A skill exige a execução de código ligada, em Settings > Capabilities ("Code execution and file creation").
- Jarvis (A3): não se sabe se ele usa skills; a fala 6 é opcional.
- `EXEMPLOS_preparados_no_padrao`: o briefing, a ata e o plano (opção B) já no padrão, em Word e PDF. Servem de reserva visual: diga que são exemplos preparados.
- `COMPARACAO_mesma_ata_sem_e_com_skill`: a mesma ata, gerada em teste sem e com a skill, para mostrar no slide 10.
- Na palestra: mostre a pasta da skill no slide 10. Use-a na A1 (o briefing sai no papel timbrado) e na A2 ("o procedimento da ata está dentro da skill").

## 4. O painel

- [00_PAINEL_abrir_no_navegador.html](00_PAINEL_abrir_no_navegador.html) funciona sem internet. Tem os pedidos com botão Copiar, os roteiros formatados, os links para o plano B, o checklist do dia, o cronograma e a cola de palco para imprimir.
- Ele serve para preparar e ensaiar. No palco, com o projetor em Duplicar, tudo o que está no notebook aparece no telão. Por isso, monte as conversas antes de a plateia entrar (anexos e pedido colado, sem enviar) e use a cola impressa e os `.txt`.

## 5. Para a plateia sentir a aceleração

- Antes de cada demo, pergunte: "Quanto tempo vocês levam para fazer isso hoje?" (no máximo 1 minuto).
- Cronômetro visível: marque "Volta" quando o texto terminar e pare depois da sua conferência. Use só tempos medidos.
- Caça ao erro, só se as respostas dos slides 14 e 15 aparecerem por clique.
- Feche cada demo com: "o agente preparou; eu conferi; a decisão continua com a executiva".

## 6. Antes do dia 17

- [ ] Áudio do iPhone no som da sala: pergunte já à organização qual entrada existe e compre cabo e adaptador até 13/10 (12/10 é feriado).
- [ ] Jarvis: confira se ele tem Gmail ou agenda reais conectados e desconecte para a demo.
- [ ] Skill: instale e teste no Claude, com os pedidos da A1 e da A2, e desligue a "ata-de-reuniao".
- [ ] Claude: em Settings > Memory, memória pausada ("Pause memory", nunca "Reset memory", que apaga tudo) e "Search and reference chats" desligado, para o ensaio e a palestra. Confira também que as suas instruções pessoais (Settings > General) não aparecem nas respostas.
- [ ] Claude: duas abas pré-montadas, uma para a A1 e outra para a A2, com claude.ai na lista de sites sempre ativos do navegador. No ensaio, deixe as abas paradas pelo tempo de espera do dia 17 e confira que os anexos e o pedido continuam lá. Veja também se o Claude pede autorização para gerar o Word.
- [ ] Ensaio completo, cronometrado e gravado, em 14/10; correções em 15/10; só uma checagem curta em 16/10 (o manual sugeria 16/10 para o ensaio completo).
- [ ] Internet própria e perfil de navegador só para a palestra. Marque o PPTX ("Lawrence Teixeira - Agentes de IA.pptx") como "Sempre manter neste dispositivo" no OneDrive (a pasta de demos já está marcada).

As notas dos slides 1 a 20 têm horários antigos. As dos slides 14 e 15 também têm pedidos antigos, e a do 20, falas antigas da A3; a do 14 cita "06_resultados_reserva.txt", que não existe, e a do 15 ainda lista o procedimento da ata entre os anexos, mas agora ele vem da skill. A nota do slide 13 ainda manda abrir o ChatGPT e o Claude; agora a A1 e a A2 usam só o Claude. Siga os `PASSO_A_PASSO.md`.

## 7. Decisões suas (resolva no ensaio)

- Votação A ou B: dentro da chamada, com o microfone no mudo durante a contagem (como no manual), ou no slide 19, antes de ligar. Empate: fique com B.
- Se vai usar a correção de horário do Jarvis (`FALAS_para_copiar\X_Correcao_se_errar_horario.txt`), que é sugestão nova.
- Como o texto do Jarvis vai aparecer no Windows (por exemplo, a conversa aberta no navegador).
- Na A3, se vai usar a fala 6, com a skill (depende do Jarvis).
- Se vai pôr animação por clique nos slides 14 e 15. Sem ela, não faça a caça ao erro.
