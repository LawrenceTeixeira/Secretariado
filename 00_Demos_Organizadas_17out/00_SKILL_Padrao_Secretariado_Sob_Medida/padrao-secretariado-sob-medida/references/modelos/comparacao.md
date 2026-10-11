# Modelo: comparação de propostas, fornecedores ou viagens (`"tipo": "comparacao"`)

Use para pôr opções lado a lado com os mesmos critérios: locais, fornecedores, voos, hotéis. O agente normaliza as propostas; a pessoa confirma as lacunas e decide.

## Metadados sugeridos

`Objetivo`, `Critérios` (teto, capacidade, horário, acessibilidade), `Fontes`.

## Seções, nesta ordem

1. **Critérios**: cada critério com a fonte (teto de gasto, número de pessoas, horário-limite, margem de deslocamento).
2. **Comparação**: tabela `Opção`, `O que inclui`, `Custo total` (com a conta), `Atende aos critérios?`, `Falta confirmar`, `Fonte`. Some itens cobrados à parte (`scripts/conferir.py soma ... --teto ...`). Para horários, mostre a conta ("pouso às 9h40 + 60 min = pronta às 10h40").
3. **Exclusões**: qual critério eliminou cada opção, em uma frase ("O voo das 13h custa menos, mas chega depois da abertura do evento").
4. **Perguntas ao fornecedor** ou **O que confirmar antes de decidir**: em checklist.
5. **Leitura para decisão**: qual opção atende aos critérios informados, como apoio. A decisão continua humana.

Feche com `revisao_humana` e `fontes`.

## Cuidados

- O menor preço anunciado não é o menor custo completo.
- "Não informado" não é zero nem "não tem".
- Não reserve, não pague e não negocie. Não consulte preços reais se o pedido não autorizou: diga que os valores são os das fontes.
- Não peça nem registre documentos pessoais (CPF, passaporte) numa comparação preliminar.
