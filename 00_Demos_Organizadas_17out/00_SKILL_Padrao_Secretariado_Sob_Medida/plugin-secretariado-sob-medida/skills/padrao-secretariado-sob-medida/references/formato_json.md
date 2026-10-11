# Formato do conteúdo (JSON) para `scripts/gerar_documento.py`

O script recebe um JSON com o conteúdo e cuida de todo o visual. Escreva só o conteúdo.

## Campos

| Campo | Obrigatório | O que é |
|---|---|---|
| `tipo` | sim | `briefing`, `ata`, `email`, `plano`, `providencias`, `agenda`, `comparacao` ou `livre`. Define o rótulo do cabeçalho. |
| `titulo` | sim | Título do documento. |
| `subtitulo` | não | Linha abaixo do título (data, reunião, versão). |
| `rotulo` | não | Substitui o rótulo do cabeçalho (padrão: derivado do `tipo`). |
| `codigo` | não | Linha pequena abaixo do rótulo (ex.: "Versão 2"). |
| `status` | não | Faixa de status. Padrão: "Rascunho para revisão — nada foi enviado, agendado ou contratado." |
| `metadados` | não | Lista de pares `["Rótulo", "Valor"]` (data, participantes, para quem, preparado por). |
| `secoes` | sim | Lista de seções, na ordem do modelo. |
| `revisao_humana` | sim | Lista do que uma pessoa precisa conferir, decidir ou autorizar. Vira a seção final com caixas de seleção. |
| `fontes` | sim | Arquivos e trechos usados (ex.: "02_fontes_pre_reuniao.txt, seções F1 a F4"). Vira a seção "Fontes consultadas". |
| `ficticio` | não | `true` quando as fontes forem fictícias ou de demonstração. Coloca o aviso no rodapé. |
| `compacto` | não | `true` para o mesmo visual com menos espaço vertical. Use quando o documento precisar caber em uma página (ex.: briefing). Não ajuste o espaçamento à mão. |

## Seções

Cada seção tem `titulo` e um ou mais blocos. Há dois jeitos de escrever os blocos.

**Atalho:** os blocos aparecem sempre nesta ordem: texto, itens, tabela, checklist, destaque, nota.

```json
{"titulo": "Decisões", "texto": "Parágrafo curto.", "itens": ["Item 1 [T1]", "Item 2 [T3]"]}
```

**Ordem livre:** use quando precisar, por exemplo, de um texto depois da tabela.

```json
{"titulo": "Comparação", "conteudo": [
  {"texto": "As duas propostas cobrem 18/03/2027 [F2]."},
  {"tabela": {"colunas": ["Local", "Total"], "linhas": [["Hotel Mirante", "R$ 4.800"]]}},
  {"nota": "Valores conferidos."}
]}
```

| Bloco | Formato | Uso |
|---|---|---|
| `texto` | texto ou lista de textos | Parágrafos. |
| `itens` | lista de textos | Lista com marcadores. |
| `checklist` | lista de textos | Lista com caixas de seleção (☐). |
| `tabela` | `{"colunas": [...], "linhas": [[...]], "legenda": "opcional"}` | Cabeçalho vinho e linhas alternadas. |
| `destaque` | `{"titulo": "...", "texto": "linha 1\nlinha 2"}` | Caixa com filete vinho: e-mails, mensagens, recados. |
| `nota` | texto | Observação pequena em cinza. |

Em qualquer texto, `**trecho**` sai em negrito. Use pouco: só para o que a pessoa precisa ver primeiro (ex.: **R$ 150 acima do teto**).

## Exemplo completo

```json
{
  "tipo": "briefing",
  "titulo": "Briefing: próximos passos do Fórum de Gestão Atlas",
  "subtitulo": "Para decisão de Marina Souza",
  "metadados": [["Para", "Marina Souza, diretora"], ["Preparado em", "dd/mm/aaaa"], ["Fontes", "F1 a F4"]],
  "secoes": [
    {"titulo": "Objetivo", "texto": "Definir os próximos passos do fórum de 18/03/2027 [F1]."},
    {"titulo": "Comparação dos locais", "tabela": {
      "colunas": ["Local", "Inclui", "Total", "Teto R$ 5.000", "Falta confirmar", "Fonte"],
      "linhas": [
        ["Hotel Mirante", "Sala, café e projetor", "R$ 4.800", "Folga de R$ 200", "Estacionamento", "F2"],
        ["Centro Ponte Alta", "Sala e café; projetor à parte", "R$ 4.200 + R$ 950 = **R$ 5.150**", "**R$ 150 acima**", "Rampa de acesso", "F2"]
      ]}},
    {"titulo": "Mensagem sugerida", "destaque": {"titulo": "Assunto: ...", "texto": "Olá, equipe.\n..."}}
  ],
  "revisao_humana": ["Confirmar a data da próxima reunião: o e-mail diz segunda-feira, dia 09/03/2027, mas essa data é terça-feira."],
  "fontes": ["manual_da_diretoria.txt", "fontes_forum.txt (F1 a F4)"],
  "ficticio": true
}
```

Rode `python scripts/gerar_documento.py --exemplo` para ver outro exemplo.
