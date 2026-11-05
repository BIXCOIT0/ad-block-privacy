# PapaAnúncio — privacidade e suporte

Extensão gratuita para reduzir anúncios e rastreadores no Microsoft Edge, com controles locais por site e pausa global. Em inglês, AdChomper. Desenvolvido por [Marco.elev](https://www.instagram.com/marco.elev/).

[Instalar pela página oficial do Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/papaan%C3%BAncio/dkhdokbphfkndloeabmdpniaedpmnahl)

## Começar e obter ajuda

Use o popup para pausar a proteção no site atual ou em todos os sites. Depois de uma alteração, outras abas já abertas podem precisar ser recarregadas. A contagem indica ações de regras observadas, não uma avaliação de segurança nem um número exato de anúncios.

Para relatar um problema, informe o domínio e o que aconteceu, incluindo versão instalada e navegador. Na extensão, o diagnóstico é opcional e pode ser revisado antes do envio. Não publique senhas, tokens, URLs privadas ou logs com dados pessoais nas [issues públicas](https://github.com/BIXCOIT0/ad-block-privacy/issues).

Não há garantia de bloquear todos os anúncios. O comportamento de YouTube e Twitch pode mudar com os serviços; o módulo Twitch é experimental.

## Privacidade

- [Política em português](PRIVACY.md)
- [Privacy policy in English](PRIVACY.en.md)
- [Página de leitura](index.html)

As políticas integradas na main descrevem a linha 0.9.14 e identifica separadamente mudanças da candidata 0.9.16. Referências históricas não indicam a versão atual da loja. Consulte a versão instalada em edge://extensions e a ficha oficial. A versão publicada informada pelo responsável é 0.9.14; alterações de candidatas não significam publicação.

Relatos pelo formulário usam Web3Forms somente por ação explícita. Diagnósticos podem conter dados sensíveis apesar dos filtros. Leia a política e revise o conteúdo.

## Apoio voluntário

[Página Pix](https://bixcoit0.github.io/apoio-AD-BLOCK/). Abrir a página não confirma um pagamento.

## Manutenção

Este repositório público mantém políticas e suporte. O código da extensão é privado e não deve ser copiado para cá. Preservar os caminhos PRIVACY.md e PRIVACY.en.md: são usados pela extensão e pela loja. Alterações legais devem conferir comportamento da versão aplicável; não basta substituir números.

A organização em andamento preserva esses links e prepara uma fonte única de políticas com HTML semântico e testes. A integração deste repositório não confirma publicação de uma nova versão da extensão.

## Gerar e validar a página

PRIVACY.md e PRIVACY.en.md são as fontes editáveis. Execute `python3 scripts/render_privacy.py` depois de alterá-las. Não editar index.html à mão. `python3 scripts/render_privacy.py --check` detecta divergências e `python3 scripts/test_privacy.py` valida estrutura, links internos e escapes. O renderizador usa um subconjunto explícito de Markdown e não executa HTML ou scripts da fonte.

O workflow de validação não publica Pages. Testes de Chromium usam páginas locais, quatro larguras e zoom CSS 1x/2x, navegação PT/EN e skip link, com capturas de alto contraste. Zoom real e leitor de tela precisam de avaliação manual. Checagem de tópicos PT/EN não substitui revisão humana de equivalência.

## Estado da publicação deste repositório

Políticas PT/EN e página HTML gerada foram integradas pelo PR #1, com CI aprovada. GitHub Pages não está habilitado neste repositório no inventário de 05/11/2026; os links públicos PRIVACY.md e PRIVACY.en.md no GitHub continuam sendo as entradas de privacidade. O HTML pode ser servido por hospedagem estática quando essa configuração for autorizada/disponível. Isso não impede ler as políticas no GitHub nem publica a candidata 0.9.16 da extensão.
