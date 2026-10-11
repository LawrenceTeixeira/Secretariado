# Modelo: ata e lista de acompanhamento (`"tipo": "ata"`)

Use ao receber transcrição ou anotações de reunião. A ata registra com fidelidade o que foi decidido e quem faz o quê até quando, e deixa à vista o que ficou em aberto. Ela não é um resumo criativo: cada linha precisa estar ancorada no que foi dito.

## Procedimento (padrão da equipe)

1. Identifique data e participantes apenas quando estiverem informados.
2. Separe **decisão**, **tarefa**, **sugestão** e **dúvida**. Uma proposta não vira decisão sem evidência.
3. Para cada tarefa, registre ação, responsável, prazo e origem (trecho T). Escreva "não informado" nos campos ausentes.
4. Verifique a coerência entre data e dia da semana (`scripts/conferir.py dia`). Aponte conflitos sem corrigi-los em silêncio.
5. Confira os cálculos citados na reunião (`scripts/conferir.py soma`).
6. Omita comentários pessoais irrelevantes. Não acrescente inferências sobre pessoas.
7. Produza uma ata curta e uma lista de acompanhamento.
8. Redija um e-mail de acompanhamento com até 120 palavras (ou o limite do Manual), no tom do Manual.
9. Não envie, não agende e não altere sistemas. Entregue rascunhos para revisão.
10. Encerre listando as dúvidas e as verificações humanas pendentes.

## Metadados sugeridos

`Reunião`, `Data` (se informada), `Participantes mencionados`, `Condução` (se informada), `Preparado por` ("Agente de IA, para revisão do secretariado").

## Seções, nesta ordem

1. **Decisões**: itens objetivos com origem ("Manter o fórum em 18/03/2027 [T2]").
2. **Tarefas e acompanhamento**: tabela `#`, `Ação`, `Responsável`, `Prazo`, `Origem`. Campos sem informação ficam "não informado".
3. **Sugestões**: o que foi proposto mas não decidido (por exemplo, uma data sugerida para a próxima reunião).
4. **Dúvidas e pendências**: o que ficou em aberto, incluindo contradições de data ("'segunda-feira, dia 9' contém conflito: 09/03/2027 é terça-feira").
5. **Próxima reunião**: data e horário só se tiverem sido definidos; caso contrário, "a confirmar". Se a agenda não foi fornecida, não sugira horários livres.
6. **Conferências feitas**: datas e valores que você verificou e o resultado.
7. **Rascunho de e-mail**: bloco `destaque` com `"titulo": "Assunto: ..."` e o texto. Sem destinatários reais; assine como `[assinatura]` ou conforme o Manual.

Se omitir um comentário pessoal, registre isso como `nota` em "Dúvidas e pendências": "Comentário pessoal omitido por não contribuir para a decisão", sem detalhar. Não use caixa de seleção para isso: `revisao_humana` lista só o que alguém precisa conferir, decidir ou fazer. Feche com `revisao_humana` e `fontes`.

## Cuidados

- Escreva no pretérito e na terceira pessoa ("Marina decidiu manter...").
- "Alguém precisa validar" não tem responsável: "não informado".
- Valor ou fato corrigido na própria reunião: registre só o valor final e a origem.
- Se o Manual do Executivo definir outro marcador para dado ausente, use o do Manual.
- Não invente nome nem objetivo da reunião: se não estiverem nas fontes, use "Ata da reunião de [data]" e "Objetivo: não informado".
- Se houver data em conflito, o e-mail pergunta diretamente a quem propôs qual é a data certa.
- Citações entre aspas são literais ("às nove" continua "às nove").
- Se a fala citar só o dia ("dia 9"), use o mês da reunião e diga que o mês foi deduzido; se a data da reunião não estiver nas fontes, escreva "não informado".
