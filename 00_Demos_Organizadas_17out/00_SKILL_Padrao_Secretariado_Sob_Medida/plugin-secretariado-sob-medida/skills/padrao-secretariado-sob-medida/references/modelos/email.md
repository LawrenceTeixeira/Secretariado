# Modelo: e-mail ou mensagem de acompanhamento (`"tipo": "email"`)

Use quando o pedido for só a mensagem. Se o e-mail acompanhar uma ata, um briefing ou um plano, ele entra como seção `destaque` do próprio documento.

## Estrutura

- **Assunto**: curto e específico ("Fórum Atlas | pendências e próxima reunião").
- **Saudação**: conforme o Manual (padrão: "Olá, equipe.").
- **Corpo**: decisões primeiro, depois responsáveis e prazos, depois o que falta definir. Até 120 palavras, ou o limite que o Manual ou o pedido indicarem.
- **Fechamento**: deixe claro o que é proposta e o que depende de confirmação ("A agenda só será atualizada após essa validação.").
- **Assinatura**: `[assinatura]` ou conforme o Manual.

No documento: seção "Mensagem" com bloco `destaque` (`titulo` = "Assunto: ...", `texto` = corpo com quebras de linha `\n`). Em `metadados`, registre `Destinatários` como "[lista de participantes]", nunca endereços reais.

## Cuidados

- Conte as palavras do corpo antes de entregar e informe a contagem na conversa.
- Não anuncie nada como feito (convite enviado, reserva confirmada) se não houver evidência.
- Rascunho é rascunho: a faixa de status do documento já diz que nada foi enviado.
