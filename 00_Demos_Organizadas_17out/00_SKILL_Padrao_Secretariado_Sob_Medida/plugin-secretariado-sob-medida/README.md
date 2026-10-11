# Plugin Secretariado Sob Medida

Um plugin é um pacote. Ele pode reunir várias skills (o "como fazer") e conectores (o acesso a outros aplicativos).

Este pacote traz uma skill:

- `skills/padrao-secretariado-sob-medida`: papel timbrado, modelos de documentos de secretariado (briefing, ata, e-mail, plano de reunião, quadro de providências, proposta de agenda, comparação) e conferência de datas, valores e horários.

Ainda não há conectores. Numa empresa, o próximo passo seria acrescentar, com aprovação da TI, o conector da agenda ou do e-mail corporativo. Assim, a mesma skill passaria a consultar dados reais, com permissões controladas.

## Uso

- **Claude Code:** `claude --plugin-dir plugin-secretariado-sob-medida` (a pasta ou o `.zip`).
- **claude.ai e ChatGPT:** não usam este pacote. Instale só a skill, com o arquivo `padrao-secretariado-sob-medida.zip` da pasta acima. Não envie o ZIP do plugin em Customize > Skills: ele não tem o `SKILL.md` no topo e não funciona como skill.
- Instale a skill ou o plugin, não os dois.

Licença: veja `LICENSE.txt` (MIT, exceto nome, logo e assinatura do Secretariado Sob Medida).
