# Skill "Padrão Secretariado Sob Medida": como instalar, testar e mostrar

Criada em 10/10/2026 para a palestra de 17/10/2026. Os dados das demos são fictícios.

## O que é

- Uma skill é um procedimento empacotado: instruções (`SKILL.md`), materiais de apoio (modelos, logo, papel timbrado) e pequenos programas (scripts). Você instala uma vez e, enquanto ela estiver ligada, toda conversa que pedir um documento de secretariado a usa.
- Esta skill é o "papel timbrado + manual de redação + conferência" do Secretariado Sob Medida:
  - **Papel timbrado:** logo, cores vinho (`#532832`) e sálvia (`#C8C59A`), títulos em Georgia e texto em Calibri, cabeçalho e rodapé com a assinatura do site ("Formação, Networking e Transformação Profissional").
  - **Modelos:** briefing, ata e acompanhamento, e-mail, plano de reunião, quadro de providências, proposta de agenda e comparação de propostas.
  - **Conferência:** dia da semana, somas e tetos, sobreposição de horários (`scripts\conferir.py`).
  - **Gerador do Word:** `scripts\gerar_documento.py`.
- Os exemplos internos da skill usam outro caso fictício (Fórum Atlas). Assim, a skill não "conhece" as respostas das demos: quem acha o R$ 8.300 e a quinta-feira é o agente, lendo as fontes ao vivo.

## O que tem nesta pasta

- [padrao-secretariado-sob-medida](padrao-secretariado-sob-medida/): a skill aberta, para mostrar na palestra.
- [padrao-secretariado-sob-medida.zip](padrao-secretariado-sob-medida.zip): o arquivo para instalar.
- [plugin-secretariado-sob-medida](plugin-secretariado-sob-medida/) e `plugin-secretariado-sob-medida.zip`: o mesmo conteúdo como plugin (opcional, para o Claude Code).
- [EXEMPLOS_preparados_no_padrao](EXEMPLOS_preparados_no_padrao/): briefing (A1), ata e e-mail (A2) e plano v2 (A3), em Word e PDF, gerados com a skill a partir dos resultados preparados dos kits. Mostram como fica e servem de reserva visual (diga que é exemplo preparado).
- [papel_timbrado.docx](padrao-secretariado-sob-medida/assets/papel_timbrado.docx): papel timbrado em branco, para uso manual no Word.
- [COMPARACAO_mesma_ata_sem_e_com_skill](COMPARACAO_mesma_ata_sem_e_com_skill/): a mesma ata gerada em teste sem e com a skill, em PDF, para mostrar no slide 10.

## Instalar no Claude (demos A1 e A2)

1. No claude.ai ou no app: Customize > Skills (claude.ai/customize/skills). Envie `padrao-secretariado-sob-medida.zip` e ligue a skill.
2. Requisito: a execução de código ligada, em Settings > Capabilities ("Code execution and file creation"). Ela vem ligada nos planos Free, Pro e Max; no Team e no Enterprise, depende do administrador. Em outubro de 2026, a ajuda do Claude listava as skills em todos os planos, inclusive o gratuito.
3. Sua conta já tem a skill "ata-de-reuniao". Desligue-a para as demos: as duas disputariam o mesmo pedido de ata, e ela usa "[confirmar]" onde a demo espera "não informado". Religue depois, se quiser.
4. Teste numa conversa nova: "Use a skill padrao-secretariado-sob-medida e gere um documento de teste com o título Teste do papel timbrado". Confira se o Claude carrega a skill e se o Word abre com logo e rodapé.
5. A A1 e a A2 usam a skill: `A1_PROMPT.txt` e `A2_PROMPT.txt` já pedem o papel timbrado, e na A2 o procedimento da ata vem dela. A skill vale para a conta inteira: deixe-a ligada para as duas demos e não mexa nela no palco.

## ChatGPT (opcional)

Desde 11/10/2026, a A1 roda no Claude. O ChatGPT fica só na A3, com o Jarvis, e a skill no ChatGPT só importa se você for testar a fala 6 do Jarvis.

1. As skills do ChatGPT seguem o mesmo padrão aberto (`SKILL.md`). Saíram do beta em 9/7/2026 e, em outubro de 2026, estavam disponíveis nas contas de empresa e de ensino (planos Business, Enterprise, Healthcare e Edu). Nelas, quem libera é o administrador.
2. Para enviar, abra o ChatGPT no computador, clique em Plugins, na barra lateral, e abra a aba Skills. Clique em Create > Upload from your computer e envie o mesmo ZIP. Os nomes dos menus mudam com frequência.

## Jarvis (A3)

- Não se sabe se o dot do Jarvis usa skills. No ensaio, teste a fala opcional `A3_Jarvis_voz_Reuniao_mudou_slides19-20\FALAS_para_copiar\6_Opcional_documento_no_padrao.txt`. Se não funcionar, pule: a demo do Jarvis não depende disso.

## Teste antes do evento (com os arquivos das demos)

- **A1, no Claude:** `A1_PROMPT.txt`, com os 2 arquivos de `ANEXAR_estes_arquivos` (01 e 02).
- **A2, no Claude:** `A2_PROMPT.txt`, com os 2 arquivos de `ANEXAR_estes_arquivos` (01 e 03). O procedimento da ata está dentro da skill.
- Confira os mesmos pontos de sempre (`PASSO_A_PASSO.md` de cada demo). Confira também logo, rodapé, a faixa "Rascunho para revisão" e a seção "O que depende de revisão humana".
- Se a skill não carregar ou o arquivo não sair, siga com o texto da conversa e, como plano B, mostre a saída salva em `SAIDAS_salve_aqui_o_resultado` ou o exemplo em PDF. Não troque de pedido nem mexa na skill no palco.
- As saídas do teste de 10/10 estão em `SAIDAS_salve_aqui_o_resultado`, na pasta de cada demo.

## Como mostrar na palestra (slide 10, de 30 a 60 segundos)

1. Abra a pasta `padrao-secretariado-sob-medida` e mostre: `SKILL.md` (as instruções), `references\modelos` (os modelos), `assets` (logo e papel timbrado) e `scripts` (o gerador e a conferência).
2. Diga: "Uma skill é o jeito da casa empacotado. Montei uma vez o padrão de documentos do Secretariado; agora qualquer agente da equipe entrega no mesmo formato e com as mesmas conferências."
3. Na A2, antes de enviar: "Reparem que não anexei o procedimento da ata: ele está dentro da skill."
4. Plugin (opcional): "O plugin é a caixa que junta skills e, no futuro, os conectores da agenda e do e-mail, com permissão da TI." Mostre a pasta `plugin-secretariado-sob-medida`.
5. Opcional: abra lado a lado os dois PDFs de `COMPARACAO_mesma_ata_sem_e_com_skill` e diga: "Mesma tarefa, mesma transcrição. Sem a skill, cada agente faz de um jeito; com a skill, sai no padrão da casa." Diga que são resultados de teste.
6. Lembre o limite do slide 10: a skill não dá acesso a contas nem a sistemas (quem dá acesso é o conector, com permissão); ela ensina como fazer.

## Cuidados

- O nome, o logo e a assinatura pertencem ao Secretariado Sob Medida e foram usados com autorização nesta palestra. Eles não estão cobertos pela licença MIT (veja `padrao-secretariado-sob-medida\LICENSE.txt`).
- Os documentos saem com "Preparado com apoio de agente de IA" e "rascunho para revisão humana" no rodapé. Nas demos, saem também com "dados fictícios".
- Não coloque senhas, dados pessoais ou informações reais de clientes dentro de uma skill: quem a recebe recebe todos os arquivos.
- Instale só skills de fontes confiáveis: elas podem trazer scripts que o agente executa.
- Para mudar cores, fontes ou rodapé, altere as constantes no início de `scripts\gerar_documento.py` e gere o ZIP de novo (botão direito na pasta da skill > Compactar para arquivo ZIP).
