# Modelo: plano ou reagendamento de reunião (`"tipo": "plano"`)

Use quando uma reunião precisa ser reorganizada (atraso, compromisso fixo, prazo de decisão) ou planejada em blocos. O plano mostra as concessões com clareza e devolve a escolha às pessoas: a IA organiza as opções, e a pessoa decide e autoriza.

## Metadados sugeridos

`Reunião`, `Data`, `Versão` (1, 2...), `Opção escolhida` (só se alguém informou a escolha), `Prazo de decisão`.

## Seções, nesta ordem

1. **Situação e restrições**: itens com origem: quem está disponível a partir de quando, compromissos fixos, prazos e sala.
2. **Conflito identificado**: a conta que mostra o problema ("Entre 10h10 e 11h cabem 50 minutos; a pauta tem 90").
3. **Escolha humana**: a opção que a pessoa informou. Se ainda não houve escolha, apresente as opções e pergunte; não presuma.
4. **Agenda proposta**: tabela `Bloco`, `Início`, `Fim`, `Duração`, `Finalidade`, `Situação` ("proposto"). Confira com `scripts/conferir.py horarios ... --fixo ... --limite ...` e registre o resultado numa frase simples ("Conferido: nenhum bloco sobrepõe o compromisso fixo").
5. **Compromissos preservados**: o que não pode ser tocado e foi mantido.
6. **O que validar**: checklist (duração suficiente para deliberar, presença, sala). Inclua sempre a concordância das pessoas com o formato escolhido.
7. **Mensagem para a equipe**: bloco `destaque`, em forma de proposta até a confirmação (até 90 palavras, se o pedido indicar).
8. **Checklist de execução futura**: o que fazer só depois da autorização (atualizar convite, avisar participantes, conferir o evento salvo).

### Nova versão (quando uma condição muda)

Use `"codigo": "Versão 2"` e acrescente, antes da agenda, a seção **O que mudou**: tabela `Item`, `Antes`, `Depois`, `Motivo`. Altere só o necessário. Se a versão anterior já atendia à nova condição, mantenha os horários e registre por quê.

## Cuidados

- Compromisso fixo nunca é sobreposto nem movido.
- Decisão e registro são coisas diferentes: se a decisão precisa acontecer até 10h45, o bloco de decisão termina até 10h45, e o registro pode vir depois.
- Presença não confirmada fica como pendência, não como fato.
- Nada é agendado: os blocos são "propostos".
- Use os metadados só para reunião, data, versão e opção escolhida; os fatos ficam em "Situação e restrições", sem repetir.
