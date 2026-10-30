# Política de privacidade — PapaAnúncio

Português | [English](PRIVACY.en.md)

Atualizada em 30 de outubro de 2026.

Esta política descreve a versão 0.9.3 preparada para envio à loja; isso não confirma submissão ou publicação na loja. A captura de cabeçalhos e a reescrita de tokens da Twitch ficam desligadas por padrão. Confira a versão instalada em edge://extensions ou chrome://extensions.

Informações públicas do PapaAnúncio estão em https://github.com/xdbixcoito-hub/ad-block-privacy. Sua finalidade é bloquear anúncios e rastreadores e permitir que o usuário pause a proteção por site. Não exige conta própria e não contém telemetria, ferramentas de análise, publicidade própria ou servidor do desenvolvedor.

PapaAnúncio também usa os nomes locais AdChomper, ZampaAnuncios, 广告吞吞 e ऐडखाऊ. O idioma da interface segue o navegador via chrome.i18n, sem serviço de tradução, envio de textos ou nova preferência salva. O diagnóstico mostra o nome localizado. Esta política continua disponível em português e inglês.

## Dados usados no navegador

A extensão acessa o domínio e a URL da página/frame atual para decidir quais regras e seletores aplicar. O popup consulta a aba ativa e o total de ações de regras fornecido pelo navegador. Não mantém um histórico das páginas visitadas.

As preferências de sites pausados (disabledSites) e os totais/estado de ativação das regras (ruleStatus e ruleStatusErrors) são guardados em chrome.storage.local, no perfil do navegador. Erros de ativação de regras podem incluir a mensagem da API do navegador. Esses dados não são sincronizados por esta extensão nem enviados ao desenvolvedor.

Nos sites compatíveis, scripts locais leem e adaptam elementos da página e respostas do player para tentar remover publicidade. A lógica da extensão e as listas usadas na navegação estão incluídas no pacote instalado. O download das listas ocorre apenas no build do projeto pelo desenvolvedor.

## CSS cosmético e mensagens locais

O script cosmético coleta tokens de IDs, classes, nomes de tags e nomes de atributos presentes no DOM. Envia esses tokens apenas por chrome.runtime.sendMessage ao service worker local da própria extensão, que seleciona os filtros empacotados e aplica as exceções do domínio. Essas mensagens não fazem pedidos de rede. Os tokens recebidos não são registrados em logs nem gravados em storage; há conjuntos transitórios de tokens já processados no script da página para evitar trabalho repetido, descartados ao destruir o contexto. O worker também consulta a URL/frame para validar o documento e inserir o CSS específico; isso não cria histórico de navegação.

O debug cosmético, solicitado manualmente no console da extensão, mostra por frame a origem da página, o arquivo específico e os seletores carregados, mantidos transitoriamente no contexto da aba. Isso não confirma que um seletor encontrou um elemento. Não há envio automático ou registro persistente desses resultados; o usuário pode ver/copiar o resultado localmente. Esse debug é separado da prévia de diagnóstico do popup descrita abaixo.

## Diagnóstico opcional

O popup oferece uma prévia local de diagnóstico que só é preparada ao expandir o painel. Ela contém versão, disponibilidade de APIs e contagens de regras, usando campos explícitos. Não inclui sites, histórico, URLs, mensagens de erro, cabeçalhos, tokens ou dados da sessão. Nada é enviado automaticamente. Ao clicar em Copiar diagnóstico, o texto substitui o conteúdo da área de transferência; você escolhe se e onde compartilhar. Se a cópia automática não estiver disponível, pode copiar o texto selecionado manualmente. O diagnóstico não é salvo no storage da extensão.

## Página de inicialização

A página de boas-vindas consulta uma vez ruleStatus/globalPaused e, se a API existir, o estado de fixação do ícone. A sequência digitada apresenta configuração local; não faz varredura de segurança nem ativa regras. Imagem, fontes do sistema e efeitos são locais.

## Módulo experimental da Twitch

O módulo pode fazer pedidos adicionais diretamente à Twitch para obter tokens e playlists de reprodução sem anúncios. No modo anônimo padrão, os pedidos auxiliares de token usam credentials: omit e não enviam cookies, Authorization ou Client-Integrity. Podem reutilizar o Client-ID público observado da aplicação; a captura de identificadores de sessão/dispositivo está desligada por padrão. Isso não torna a conexão anônima para a Twitch: ela ainda recebe o IP e os dados necessários ao pedido.

Se a captura for habilitada manualmente, com allowSessionHeaders: false o wrapper de fetch captura somente client-id, client-session-id, client-version e x-device-id quando disponíveis. Authorization e Client-Integrity não são lidos pela captura, não entram no cache da extensão, não são encaminhados pelo BroadcastChannel nem armazenados pelo worker. Os pedidos auxiliares de token usam credentials: omit. Se o token anônimo falhar, o módulo não tenta o modo completo; sem backup seguro, preserva a playlist original. Isso se refere aos pedidos auxiliares, separados dos pedidos normais da página descritos abaixo.

Na 0.9.3, headerCapture, adMute e tokenRewrite vêm desligados; workerFilter, backup, playlistFilter e adMetrics vêm ligados. O módulo lê transitoriamente playlists HLS recebidas via fetch e XHR na página/Worker para retirar segmentos e metadados classificados como anúncio, preservando o original quando a mídia restante não é segura. Pode pedir um backup de até 480p diretamente à Twitch durante anúncios e volta à variante original depois. URLs de mídia e tokens de backup necessários ficam apenas em memória; não são gravados no storage nem enviados ao desenvolvedor. Os pedidos normais da página preservam seus headers e credentials: Authorization/Client-Integrity não são extraídos pelo filtro, mas podem continuar sendo enviados pelo navegador à própria Twitch conforme o pedido da página. A antiga reescrita de token permanece no fonte como opção manual desligada.

A observação GQL (observePlayback=true) lê somente o Client-ID público da aplicação e a assinatura da resposta live nativa para associar o canal ao master Usher. A chamada e sua resposta originais são preservadas. Esses campos ficam em um Map privado de até 32 entradas por contexto, com validade de 60 s; vencidos são descartados no próximo acesso/observação ou ao fechar o contexto. Não ficam em globais, sessionStorage, chrome.storage, logs ou BroadcastChannel. O valor do token nativo não é guardado. Quando a assinatura corresponde à URL Usher do mesmo canal, o Client-ID pode ser reutilizado em pedidos auxiliares anônimos à própria Twitch. Não se lê Authorization/Client-Integrity nessa observação; headerCapture continua desligado. Não há compartilhamento desse contexto entre frames/workers. Se a observação faltar, falhar ou expirar, usa-se o Client-ID público configurado. Isso não torna os pedidos anônimos perante a Twitch.

Operações GQL isoladas chamadas VideoAdTrack/AdReport podem receber resposta JSON vazia local, sem enviar esses pedidos à Twitch. Lotes mistos, formatos não suportados e outras métricas podem continuar sendo enviados. Isso não garante impedir detecção ou todos os rastreadores. Não se registra o corpo dessas métricas. A filtragem e os eventos XHR sintéticos podem ser detectados pelo site. Não há proxy público; a eficácia, qualidade e reprodução não são garantidas.

A flag allowSessionHeaders existe somente no código-fonte para desenvolvimento, vem desligada e não tem interface ou leitura de chrome.storage. Alterá-la manualmente para true, habilitar também headerCapture para capturar cabeçalhos e recarregar permite capturar esses cabeçalhos e tentar o modo completo com credentials: same-origin (ou diretamente completo se backupAnonymous estiver false). Nesse modo de desenvolvimento, valores e tokens permanecem em memória e podem ser enviados nos pedidos auxiliares à própria Twitch, não ao desenvolvedor. Playlists e segmentos continuam sendo solicitados à Twitch e aos endereços de mídia que ela retorna. A política de privacidade da Twitch se aplica a essas conexões; não há proxy de terceiros.

O debug da Twitch fica desligado por padrão. Quando ativado manualmente pelo usuário, registra no console local diagnósticos como nome do canal, tipo de player, contagens de segmentos e duração dos pedidos. No padrão sem sessão, o diagnóstico GQL registra apenas status, sem corpo da resposta ou mensagens de errors. No modo de desenvolvimento com sessão, o código mantém a ocultação de tokens e valores conhecidos de cabeçalhos no diagnóstico. Os logs não são enviados automaticamente.

## Pausa global, contadores e atividades

A pausa geral grava globalPaused (estado) e pausedUntil (horário de retomada ou null) em chrome.storage.local. A permissão alarms agenda a retomada mesmo com o popup fechado; o navegador pode atrasar o alarme enquanto está suspenso. Ao iniciar, a extensão confere pausas vencidas. A lista disabledSites é independente da pausa geral.

counters guarda total, today e day (data local). São ações de regras observadas nas consultas ao abrir o popup; não são um total completo de anúncios ou requisições únicas. Reaberturas são deduplicadas por marcadores transitórios de aba/regra/horário em storage.session (matchWatermarks, até 1.000 abas). Eventos não consultados, limites da API, empates de timestamp e reinícios podem afetar a contagem. O valor de hoje reinicia pela data local; o acumulado permanece no perfil.

storage.session também guarda activity: somente as três últimas ações confirmadas de pausa/retomada, com código da ação e horário, sem domínio ou URL. Os dados de sessão são descartados pelo navegador ao encerrar a sessão; não há envio ao desenvolvedor. O diagnóstico voluntário continua exportando apenas seus campos explicitamente permitidos.

A pausa altera as regras de rede imediatamente e remove registros para próximas navegações. Scripts/CSS já presentes em outras abas precisam de novo carregamento; a ação do popup recarrega somente a aba atual. A retomada por alarme tenta recarregar apenas a aba ativa HTTP/HTTPS.

## Atualização visual e notificações locais

O título “Ameaças neutralizadas” é um nome visual para ações de regras observadas, não uma avaliação de segurança. Não há varredura de malware ou confirmação de ameaças. Na instalação sem compactação, quando o navegador disponibiliza onRuleMatchedDebug, o worker confere regras block locais e envia à própria interface somente tabId e contagem. O código não lê a URL ou cabeçalhos desse evento. tabLiveCounts e liveRequestKeys são transitórios em storage.session, limitados às últimas 128 abas e até 256 chaves de requisição/regra por aba; são limpos ao fechar a aba ou ao encerrar a sessão. Esses IDs são gerados pelo navegador, não são credenciais da Twitch.

Em instalações da loja o evento imediato não é disponibilizado; o popup consulta getMatchedRules ao abrir e a cada 35 segundos enquanto está visível, respeitando recuo em erros/cotas. Essas consultas também atualizam Hoje/Total. Não há consulta periódica com o popup fechado nem envio para servidores do desenvolvedor. O bloqueio de rede funciona mesmo sem o contador aberto.

## Recursos anti-adblock locais — 0.9.3

A versão inclui stubs próprios e mínimos de APIs publicitárias/analytics e respostas vazias empacotadas. Quando habilitados para um domínio validado, regras de redirecionamento do navegador substituem os scripts/pedidos GET de teste configurados por arquivos locais, sem enviar esses pedidos aos servidores de anúncios. O perfil GPT/IMA foi ativado para www.xfilme.net e subsbr.net após confirmação do responsável, incluindo cinco sites de controle sem problemas. Em www.baixetorrentshd.org, um perfil substitui o script/sondas adsbygoogle configurados e mantém somente iscas específicas fora da tela, com dimensões mínimas e opacidade 1; anúncios reais fora desses seletores não são reexibidos. O responsável confirmou a resolução do aviso e a navegação. Os redirects são restritos aos recursos e domínios configurados; isso não representa cobertura geral de sites. Pedidos não correspondentes continuam sujeitos às outras regras e ao comportamento normal do navegador.

Os arquivos de stub declarados em web_accessible_resources usam use_dynamic_url: true e ficam restritos às origens declaradas no manifest (origens locais de teste, www.xfilme.net, subsbr.net e www.baixetorrentshd.org). URLs dinâmicas não garantem ocultar a extensão: sites autorizados podem, em teoria, sondar ou observar recursos acessíveis e efeitos das substituições. O schema Chromium 111 aceita essa opção; seu funcionamento efetivo não foi verificado aqui no Chrome/Edge mínimos. Não há tentativa de contornar a Proteção de Rastreamento do Edge ou verificação de bloqueador no servidor.

Perfis locais por domínio podem aplicar CSS fora da tela para seletores-isca simples e específicos, validados por perfil, flags constantes, interrupção de leitura/escrita de propriedades, supressão de timers por texto literal e respostas locais a fetch configurados. São intervenções específicas: stubs não implementam SDKs completos e podem ser incompatíveis com sites não validados. Não afetam os módulos YouTube/Twitch. Falhas de instalação do perfil não devem interromper a página; interrupções de propriedades, quando explicitamente configuradas, são intencionais e podem interromper o código detector que as acessa.

O debug anti-adblock é solicitado manualmente no console do service worker com antiAdblockDebug(tabId). Consulta os frames naquele momento, mostra stubs reportados, efeitos de iscas, ações de scriptlets e tempo de preparação, sem storage ou envio pela rede. Relatos do mundo MAIN podem ser forjados pela página; o debug não é prova de segurança. O estado transitório termina ao recarregar/fechar o documento. Não há código remoto, coleta para o desenvolvedor, nova dependência ou nova permissão de API.

## Compartilhamento e controle

Não vendemos dados nem os compartilhamos com anunciantes ou serviços de análise. Os pedidos à Twitch descritos acima servem exclusivamente à reprodução do vídeo. O acesso ao GitHub por links de ajuda/privacidade só acontece quando você abre esses links; a política desse site se aplica à visita.

Você pode pausar a proteção pelo popup. A aba atual recarrega para aplicar a mudança; recarregue também outras abas abertas desse site para remover scripts que já estejam em execução. Desinstalar a extensão remove seu armazenamento local do perfil. Se você ativou o debug manualmente, remova a chave com localStorage.removeItem('bloqueioPessoal_twitchDebug') no console da Twitch; essa chave fica no armazenamento do site, fora do armazenamento da extensão.

As atualizações instaladas pela loja são distribuídas pelo Microsoft Edge Add-ons e estão sujeitas às políticas da Microsoft. A extensão não possui um atualizador remoto próprio.

## Contato

Dúvidas ou pedidos relacionados à privacidade: https://github.com/xdbixcoito-hub/ad-block-privacy/issues. As issues são públicas; não publique tokens, senhas, URLs privadas ou dados pessoais.
