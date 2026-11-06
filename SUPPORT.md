# Ajuda — PapaAnúncio

[English](SUPPORT.en.md) · [Página inicial](README.md) · [Privacidade](PRIVACY.md)

## Instalar e conferir a versão

1. Instale pela [página oficial do Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/papaan%C3%BAncio/dkhdokbphfkndloeabmdpniaedpmnahl).
2. Abra o menu de extensões do Edge e selecione PapaAnúncio. O nome em inglês é AdChomper.
3. Confira a versão em `edge://extensions`. Esse endereço deve ser digitado na barra do navegador. Se houver uma atualização disponível, use os controles do Edge.

A versão publicada informada pelo responsável é 0.9.14. A candidata 0.9.16 está em testes; sua existência no projeto não significa que esteja na loja. Este guia descreve os controles comuns da linha publicada, sem exigir a candidata ou instalação de código de terceiros.

## Pausar e retomar

- **Site atual:** abra o popup na aba desejada e use o botão circular de energia. Confira o domínio e o estado exibidos. Para retomar, use o mesmo botão.
- **Todos os sites:** selecione **Pausar tudo** e escolha 15 minutos, 1 hora ou até retomar manualmente. Para reativar antes do prazo, use **Retomar tudo**.
- Uma pausa global prevalece sobre o controle por site. Confira ambos os estados se a proteção não voltar.
- Recarregue a página após mudar a proteção para testar o novo estado. Páginas internas do navegador, a loja e outras páginas restritas podem não permitir a atuação da extensão.

## Um site parou de funcionar ou detectou o bloqueador

1. Anote o domínio, a versão da extensão e do Edge e o que você estava tentando fazer.
2. Pause a proteção somente nesse site e recarregue a página. Compare o resultado. Retome a proteção depois do teste se desejar.
3. Se continuar falhando, confira a conexão e teste se outra extensão de bloqueio ou privacidade interfere. Altere uma coisa por vez e restaure suas preferências depois.
4. Envie um relato com os passos e o resultado da comparação. Uma mensagem de detecção não garante que a causa seja esta extensão.

Limpar todos os dados do navegador não é um procedimento padrão: isso pode encerrar sessões e apagar preferências. Não forneça senhas nem desative proteções do navegador para obter suporte.

## YouTube e Twitch

Se aparecer anúncio, tela preta, travamento ou queda de qualidade, informe se aconteceu ao abrir o vídeo/transmissão, durante a reprodução ou após trocar de vídeo/canal. Na Twitch, informe o canal público e o horário aproximado com fuso, quando possível. Descreva se o anúncio desapareceu sozinho e se pausar a proteção mudou o comportamento.

O bloqueio depende de mudanças nos serviços e não remove necessariamente todos os anúncios. O módulo Twitch é experimental e pode reduzir temporariamente a qualidade. Não há garantia de evitar detecção do bloqueador.

## Entender a contagem

O número no popup representa ações de regras observadas pelo navegador. Uma regra pode atuar várias vezes; o número não equivale ao total exato de anúncios ou ameaças. A contagem da aba e os totais do dia/geral têm escopos diferentes. Um indicador de carregamento ou indisponibilidade não significa que a proteção esteja desligada; confira também o estado da proteção.

## Reportar com privacidade

1. Abra **Reportar Problema** no popup da aba afetada.
2. Confira o campo do site. Ele envia somente o domínio; você pode corrigir ou apagar esse campo. Não coloque URLs privadas no texto do relato.
3. Descreva passos, resultado esperado e observado, versão e navegador. Um relato pode ser enviado sem anexar diagnóstico.
4. Se optar por anexar diagnóstico, abra **Revisar dados de diagnóstico** e examine o conteúdo. Pode incluir informações técnicas e até 50 registros recentes da extensão. Os filtros não garantem remover todo dado sensível. Se houver algo que não deseja compartilhar, desmarque o anexo e descreva o problema sem esses dados.
5. Ao clicar em **Enviar Relato**, o conteúdo selecionado é enviado pelo Web3Forms para entrega ao desenvolvedor. Se ocorrer falha de envio, confira a conexão e tente novamente; não há necessidade de publicar os logs.

Os registros são temporários e capturados durante a sessão; não recuperam retroativamente todo o console do site. Consulte a [política de privacidade](PRIVACY.md) antes de enviar.

Você também pode abrir uma [issue pública](https://github.com/BIXCOIT0/ad-block-privacy/issues). **Tudo que postar ali será público.** Use apenas domínio público, dados fictícios e passos mínimos; não anexe diagnósticos, cookies, tokens, senhas, cabeçalhos de autenticação, dados pessoais ou capturas com informações privadas. Se não tiver certeza, use o formulário sem anexo.

## Vulnerabilidades de segurança

Envie suspeitas de vulnerabilidade em privado para **marcoantonioarantes02@gmail.com**. Não publique detalhes de uma falha ainda não corrigida. Inclua versão, impacto e passos mínimos com dados fictícios, sem credenciais ou dados de outras pessoas. O contato não estabelece prazo de resposta ou programa de recompensa.

## Apoio opcional

A [página de apoio Pix](https://bixcoit0.github.io/apoio-AD-BLOCK/) é voluntária. A extensão não exige pagamento para funcionar ou receber relatos. Confira o beneficiário no aplicativo do banco antes de confirmar qualquer transferência.
