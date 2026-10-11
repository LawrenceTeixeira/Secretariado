# Comece aqui: demos da palestra "Agentes de IA na prática"

**Secretariado Sob Medida · sábado, 17/10/2026 · Lawrence Teixeira**

Atualizado em 10/10/2026. O PPT original não foi alterado: há uma cópia com os slides 16 a 18 ocultos.

> Os guias (`.md`) abrem no Bloco de Notas ou, formatados, no VS Code (Ctrl+Shift+V) e no painel. Os pedidos, as falas, os anexos e as reservas continuam em `.txt`, para copiar e colar sem símbolos de formatação.

## 1. Suas três demos, na ordem do palco

| Demo | Momento | Slide | Minutos da palestra |
| --- | --- | --- | --- |
| [A1 · ChatGPT](A1_ChatGPT_Briefing_pre-reuniao_slide14/PASSO_A_PASSO.md) | Antes da reunião: o briefing | 14 | 20 a 27 |
| [A2 · Claude](A2_Claude_Ata_e_acompanhamento_slide15/PASSO_A_PASSO.md) | Depois da reunião: a ata e o e-mail | 15 | 27 a 33 |
| [A3 · Jarvis por voz](A3_Jarvis_voz_Reuniao_mudou_slides19-20/PASSO_A_PASSO.md) | Quando a reunião muda, com votação da plateia | 19 e 20 | Slide 19 de 33 a 36; chamada de 36 a 50, com 2 minutos de folga |

- Os slides 16, 17 e 18 (fornecedores, viagem e limites) estão ocultos na cópia **Lawrence Teixeira - Agentes de IA - slides 16 a 18 ocultos.pptx**. Apresente com essa cópia: o PowerPoint pula esses slides (para mostrar um deles, digite o número e tecle Enter).
- Fechamento e perguntas: minutos 50 a 60.
- Os outros exemplos (B1, B2, B3, C1 e C2) não fazem parte desta pasta.

## 2. O que tem em cada pasta

- `PASSO_A_PASSO.md`: o roteiro da demo. Leia no ensaio.
- `ANEXAR_estes_arquivos\`: exatamente o que entra na conversa. Na A2 com a skill, use `ANEXAR_com_skill_estes_arquivos\`. Na A3 não se anexa nada: o caso fica em `COLAR_na_conversa_antes_da_chamada\` (colar o texto antes da chamada).
- `A1_PROMPT_para_copiar.txt` e `A2_PROMPT_para_copiar.txt`: os pedidos originais. O prefixo evita confundir as abas do Bloco de Notas: o da A1 começa com "Prepare um briefing"; o da A2, com "Gere uma ata".
- `A1_PROMPT_com_skill.txt` e `A2_PROMPT_com_skill.txt`: os mesmos pedidos usando a skill.
- `A1_PROMPT_correcao_se_precisar.txt` e `A2_PROMPT_correcao_se_precisar.txt`: a correção curta, uma vez só.
- Na A3: `FALAS_para_copiar\` (falas 0 a 5; a 6 é opcional, com a skill; a X é a correção de horário, sugestão nova).
- `RESERVA_plano_B_nao_anexar\`: resultado preparado. **Nunca anexar.**
- `SAIDAS_salve_aqui_o_resultado\`: guarde aqui o que a IA gerar no ensaio.

## 3. A skill do Secretariado (nova)

- Pasta [00_SKILL_Padrao_Secretariado_Sob_Medida](00_SKILL_Padrao_Secretariado_Sob_Medida/): papel timbrado (logo, cores e rodapé), modelos de documentos e conferência de datas, valores e horários. Leia [COMO_INSTALAR_E_USAR.md](00_SKILL_Padrao_Secretariado_Sob_Medida/COMO_INSTALAR_E_USAR.md).
- Testada em 10/10 nas três tarefas, com e sem a skill, por agentes do Claude num ambiente de teste (não no ChatGPT nem no Jarvis). Com a skill, passou em todas as checagens (12/12, 12/12 e 11/11). Sem a skill, o briefing e a ata acertaram os fatos, mas saíram sem o padrão; no plano do Jarvis, faltou a conta do conflito (40 minutos para uma pauta de 60).
- Claude (A2): instale o ZIP em Customize > Skills e desligue a skill "ata-de-reuniao" para a demo. Com a skill ligada, até o pedido original pode acioná-la.
- ChatGPT (A1): só se a sua conta tiver Skills (em outubro de 2026, estavam em beta). Senão, use o pedido original.
- Jarvis (A3): não se sabe se ele usa skills; a fala 6 é opcional.
- `EXEMPLOS_preparados_no_padrao`: o briefing, a ata e o plano (opção B) já no padrão, em Word e PDF. Servem de reserva visual: diga que são exemplos preparados.
- `COMPARACAO_mesma_ata_sem_e_com_skill`: a mesma ata, gerada em teste sem e com a skill, para mostrar no slide 10.
- Na palestra: mostre a pasta da skill no slide 10 e use-a na A2 ("o procedimento da ata está dentro da skill").

## 4. O painel

- [00_PAINEL_abrir_no_navegador.html](00_PAINEL_abrir_no_navegador.html) funciona sem internet. Tem os pedidos com botão Copiar, os roteiros formatados, as reservas em tela cheia, o checklist do dia, o cronograma e a cola de palco para imprimir.
- Ele serve para preparar e ensaiar. No palco, com o projetor em Duplicar, tudo o que está no notebook aparece no telão. Por isso, monte as conversas antes de a plateia entrar (anexos e pedido colado, sem enviar) e use a cola impressa e os `.txt`.

## 5. Para a plateia sentir a aceleração

- Antes de cada demo, pergunte: "Quanto tempo vocês levam para fazer isso hoje?" (no máximo 1 minuto).
- Cronômetro visível: marque "Volta" quando o texto terminar e pare depois da sua conferência. Use só tempos medidos.
- Caça ao erro, só se as respostas dos slides 14 e 15 aparecerem por clique.
- Feche cada demo com: "o agente preparou; eu conferi; a decisão continua com a executiva".

## 6. Antes do dia 17

- [ ] Áudio do iPhone no som da sala: pergunte já à organização qual entrada existe e compre cabo e adaptador até 13/10 (12/10 é feriado).
- [ ] Jarvis: confira se ele tem Gmail ou agenda reais conectados e desconecte para a demo.
- [ ] Skill: instale e teste no Claude (e no ChatGPT, se a conta tiver) e desligue a "ata-de-reuniao".
- [ ] Ensaio completo, cronometrado e gravado, em 14/10; correções em 15/10; só uma checagem curta em 16/10 (o manual sugeria 16/10 para o ensaio completo).
- [ ] Internet própria e perfil de navegador só para a palestra. Marque a cópia do PPTX (slides 16 a 18 ocultos) como "Sempre manter neste dispositivo" no OneDrive (a pasta de demos já está marcada).

As notas dos slides 1 a 20 têm horários antigos. As dos slides 14, 15, 19 e 20 também têm pedidos antigos e citam "06_resultados_reserva.txt", que não existe. Siga os `PASSO_A_PASSO.md`.

## 7. Decisões suas (resolva no ensaio)

- Votação A ou B: dentro da chamada, com o microfone no mudo durante a contagem (como no manual), ou no slide 19, antes de ligar. Empate: fique com B.
- Se vai usar a correção de horário do Jarvis (`FALAS_para_copiar\X_Correcao_se_errar_horario.txt`), que é sugestão nova.
- Como o texto do Jarvis vai aparecer no Windows (por exemplo, a conversa aberta no navegador).
- Se vai usar a skill na A1 (depende do ChatGPT) e na A3 (depende do Jarvis).
- Se vai pôr animação por clique nos slides 14 e 15. Sem ela, não faça a caça ao erro.
