# Modelo: proposta de agenda (`"tipo": "agenda"`)

Use para encontrar um horário numa agenda fornecida (arquivo ou consulta autorizada) e propor um compromisso, sem agendá-lo. A proposta só é útil se mostrar de onde veio a disponibilidade e se não houver conflito.

## Metadados sugeridos

`Agenda consultada` (fonte e identificador), `Lida em` (data e hora da leitura), `Janela permitida`, `Fuso`.

## Seções, nesta ordem

1. **Ocupações encontradas**: tabela `Intervalo`, `Situação` (ocupado ou livre), `Fonte`.
2. **Opções avaliadas**: tabela `Opção`, `Início`, `Fim`, `Duração`, `Resultado` ("rejeitada: sobrepõe B1", "escolhida: primeira janela livre", "alternativa"). Confira com `scripts/conferir.py horarios`.
3. **Proposta**: a opção escolhida e a alternativa, com o motivo.
4. **Tarefa atualizada** (se houver uma lista de tarefas): mesma ID, novo bloco proposto e situação "preparo proposto". Preparar não é concluir.

Feche com `revisao_humana` (confirmar antes de criar o convite) e `fontes`.

## Cuidados

- Proposta não é agendamento: só diga "agendado" se um evento foi salvo e relido no calendário autorizado.
- Prazo externo e meta interna são coisas diferentes; mostre os dois.
- Ao gerar arquivo de calendário (.ics), use status "TENTATIVE", sem convidados e sem alarmes, e diga que ele não foi importado.
