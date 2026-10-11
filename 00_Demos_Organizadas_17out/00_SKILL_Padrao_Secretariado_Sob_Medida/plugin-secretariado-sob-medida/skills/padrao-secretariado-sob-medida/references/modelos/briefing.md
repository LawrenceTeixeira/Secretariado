# Modelo: briefing antes da reunião (`"tipo": "briefing"`)

Use para preparar a executiva para decidir: juntar pauta anterior, e-mails, propostas e agenda num documento de uma página. O valor do briefing está em entregar a decisão pronta para ser tomada, com custos conferidos, conflitos à vista e opções viáveis.

## Metadados sugeridos

`Para` (quem decide), `Assunto`, `Preparado em`, `Fontes` (identificadores).

## Seções, nesta ordem

1. **Objetivo**: o que precisa ser decidido, em uma ou duas frases, com fonte.
2. **Situação atual**: fatos essenciais em itens, cada um com origem. Inclua o que já foi decidido e o que ainda não foi feito (ex.: "Nenhum fornecedor foi contratado [F1]").
3. **Comparação** (quando houver opções): tabela com opção, o que inclui, custo total com a conta, posição em relação ao teto (folga ou excesso), o que falta confirmar e fonte. O menor preço anunciado nem sempre é o menor custo completo.
4. **Pendências e lacunas**: o que está "não informado" ou aguardando resposta.
5. **Contradições a resolver**: cada conflito entre fontes, com as versões e a pergunta a fazer. Exemplo: "O e-mail diz 'segunda-feira, dia 09/03/2027' [F3], mas 09/03/2027 é terça-feira."
6. **Opções de horário** (quando o pedido envolver reunião): tabela com data, dia da semana conferido, horário, duração e fonte da disponibilidade. Apresente opções; não escolha pela executiva.
7. **Decisões que dependem de [nome]**: lista curta e direta. Esta seção é obrigatória: é a razão de ser do briefing. Para caber em uma página, encurte a situação, as legendas ou as fontes, mas não retire esta seção nem a junte ao Objetivo.

Mantenha as seções na ordem. Não junte pendências com contradições, e não leve as decisões da executiva para a revisão humana: elas ficam em "Decisões que dependem de [nome]".

Feche com `revisao_humana` e `fontes`.

## Cuidados

- Uma página: use `"compacto": true` no JSON e corte o que não ajuda a decidir, mas mantenha a seção de decisões. Não escreva código próprio para ajustar o espaçamento.
- Use somente os horários que a agenda fornecida mostra como livres, respeitando as regras do Manual (ex.: nada antes das 9h, reuniões de 30 minutos).
- Se uma proposta não informa um item (acessibilidade, capacidade, cancelamento), isso vai para "Falta confirmar", não vira "não tem".
