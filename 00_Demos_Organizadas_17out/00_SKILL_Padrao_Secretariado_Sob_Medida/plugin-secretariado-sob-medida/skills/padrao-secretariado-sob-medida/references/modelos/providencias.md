# Modelo: quadro de providências (`"tipo": "providencias"`)

Use para transformar um comunicado, e-mail ou mensagem de grupo numa lista verificável do que fazer. O valor está em separar o que é obrigatório do que é opcional e em não inventar o que o texto não diz (horário, canal, responsável).

## Metadados sugeridos

`Origem` (mensagem e data de recebimento), `Relógio do cenário` (quando houver), `Preparado por`.

## Seções, nesta ordem

1. **Fatos do evento ou assunto**: tabela `Item`, `Informação`, `Fonte` (data, horário de início, local; "não informado" para o que faltar, como o horário de término).
2. **Providências**: tabela `ID`, `Ação`, `Responsável`, `Prazo`, `Hora`, `Condição`, `Situação`, `Fonte`. Agrupe assuntos semelhantes (no máximo quatro providências, salvo pedido diferente). Mantenha IDs estáveis (T01, T02...) para que versões futuras atualizem a mesma linha.
3. **Lacunas**: o que precisa ser perguntado (canal de envio, formato, horário-limite).
4. **O que não aconteceu**: o que o comunicado não comprova ("Não há evidência de inscrição no jantar nem de confirmação de presença").

Feche com `revisao_humana` e `fontes`.

## Cuidados

- Opcional continua opcional ("somente se desejar participar do jantar").
- Prazo sem hora fica sem hora; "Hora" = "não informado".
- Situação é um estado real ("aguarda decisão", "a verificar", "informação pendente"), nunca "concluído" sem prova.
- Links privados, endereços e telefones do comunicado não entram no documento.
