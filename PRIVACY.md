# Política de privacidade — PapaAnúncio

Português | [English](PRIVACY.en.md)

Atualizada em 29 de outubro de 2026.

Esta política descreve a versão 0.8.7 preparada para submissão; isso não confirma publicação na loja. Na versão 0.7.1 anteriormente publicada, a falha do token anônimo podia acionar uma tentativa com cabeçalhos completos da sessão (incluindo Authorization e Client-Integrity quando disponíveis), mantidos em memória e enviados somente à própria Twitch. Essa tentativa fica desligada por padrão na 0.7.3. Confira a versão instalada em edge://extensions ou chrome://extensions.

Informações públicas do PapaAnúncio estão em https://github.com/xdbixcoito-hub/ad-block-privacy. Sua finalidade é bloquear anúncios e rastreadores e permitir que o usuário pause a proteção por site. Não exige conta própria e não contém telemetria, ferramentas de análise, publicidade própria ou servidor do desenvolvedor.

## Dados usados no navegador

A extensão acessa o domínio e a URL da página/frame atual para decidir quais regras e seletores aplicar. O popup consulta a aba ativa e o total de ações de regras fornecido pelo navegador. Não mantém um histórico das páginas visitadas.

As preferências de sites pausados (disabledSites) e os totais/estado de ativação das regras (ruleStatus e ruleStatusErrors) são guardados em chrome.storage.local, no perfil do navegador. Erros de ativação de regras podem incluir a mensagem da API do navegador. Esses dados não são sincronizados por esta extensão nem enviados ao desenvolvedor.

Nos sites compatíveis, scripts locais leem e adaptam elementos da página e respostas do player para tentar remover publicidade. A lógica da extensão e as listas usadas na navegação estão incluídas no pacote instalado. O download das listas ocorre apenas no build do projeto pelo desenvolvedor.

## Diagnóstico opcional — a partir da 0.7.4

O popup oferece uma prévia local de diagnóstico que só é preparada ao expandir o painel. Ela contém versão, disponibilidade de APIs e contagens de regras, usando campos explícitos. Não inclui sites, histórico, URLs, mensagens de erro, cabeçalhos, tokens ou dados da sessão. Nada é enviado automaticamente. Ao clicar em Copiar diagnóstico, o texto substitui o conteúdo da área de transferência; você escolhe se e onde compartilhar. Se a cópia automática não estiver disponível, pode copiar o texto selecionado manualmente. O diagnóstico não é salvo no storage da extensão.

## Página de inicialização

A página de boas-vindas consulta uma vez ruleStatus/globalPaused e, se a API existir, o estado de fixação do ícone. A sequência digitada apresenta configuração local; não faz varredura de segurança nem ativa regras. Imagem, fontes do sistema e efeitos são locais.

## Módulo experimental da Twitch

O módulo pode fazer pedidos adicionais diretamente à Twitch para obter tokens e playlists de reprodução sem anúncios. No modo anônimo padrão, os pedidos de token omitem cookies, Authorization e Client-Integrity; podem reutilizar Client-ID e identificadores de sessão/dispositivo da própria Twitch. Isso não torna a conexão anônima para a Twitch: ela ainda recebe o IP e os dados necessários ao pedido.

Na configuração distribuída (allowSessionHeaders: false), o wrapper de fetch captura somente client-id, client-session-id, client-version e x-device-id quando disponíveis. Authorization e Client-Integrity não são lidos pela captura, não entram no cache da extensão, não são encaminhados pelo BroadcastChannel nem armazenados pelo worker. Os pedidos auxiliares de token usam credentials: omit. Se o token anônimo falhar, o módulo não tenta o modo completo; sem backup seguro, preserva a playlist original. Isso não altera os pedidos autenticados que a própria página Twitch normalmente faz.

A flag allowSessionHeaders existe somente no código-fonte para desenvolvimento, vem desligada e não tem interface ou leitura de chrome.storage. Alterá-la manualmente para true e recarregar permite novamente capturar esses cabeçalhos e tentar o modo completo com credentials: same-origin (ou diretamente completo se backupAnonymous estiver false). Nesse modo de desenvolvimento, valores e tokens permanecem em memória e podem ser enviados nos pedidos auxiliares à própria Twitch, não ao desenvolvedor. Playlists e segmentos continuam sendo solicitados à Twitch e aos endereços de mídia que ela retorna. A política de privacidade da Twitch se aplica a essas conexões; não há proxy de terceiros.

O debug da Twitch fica desligado por padrão. Quando ativado manualmente pelo usuário, registra no console local diagnósticos como nome do canal, tipo de player, contagens de segmentos e duração dos pedidos. No padrão sem sessão, o diagnóstico GQL registra apenas status, sem corpo da resposta ou mensagens de errors. No modo de desenvolvimento com sessão, o código mantém a ocultação de tokens e valores conhecidos de cabeçalhos no diagnóstico. Os logs não são enviados automaticamente.

## Pausa global, contadores e atividades — 0.8.0

A pausa geral grava globalPaused (estado) e pausedUntil (horário de retomada ou null) em chrome.storage.local. A permissão alarms agenda a retomada mesmo com o popup fechado; o navegador pode atrasar o alarme enquanto está suspenso. Ao iniciar, a extensão confere pausas vencidas. A lista disabledSites é independente da pausa geral.

counters guarda total, today e day (data local). São ações de regras observadas nas consultas ao abrir o popup; não são um total completo de anúncios ou requisições únicas. Reaberturas são deduplicadas por marcadores transitórios de aba/regra/horário em storage.session (matchWatermarks, até 1.000 abas). Eventos não consultados, limites da API, empates de timestamp e reinícios podem afetar a contagem. O valor de hoje reinicia pela data local; o acumulado permanece no perfil.

storage.session também guarda activity: somente as três últimas ações confirmadas de pausa/retomada, com código da ação e horário, sem domínio ou URL. Os dados de sessão são descartados pelo navegador ao encerrar a sessão; não há envio ao desenvolvedor. O diagnóstico voluntário continua exportando apenas seus campos explicitamente permitidos.

A pausa altera as regras de rede imediatamente e remove registros para próximas navegações. Scripts/CSS já presentes em outras abas precisam de novo carregamento; a ação do popup recarrega somente a aba atual. A retomada por alarme tenta recarregar apenas a aba ativa HTTP/HTTPS.

## Atualização visual e notificações locais — 0.8.6

O título “Ameaças neutralizadas” é um nome visual para ações de regras observadas, não uma avaliação de segurança. Não há varredura de malware ou confirmação de ameaças. Na instalação sem compactação, quando o navegador disponibiliza onRuleMatchedDebug, o worker confere regras block locais e envia à própria interface somente tabId e contagem. O código não lê a URL ou cabeçalhos desse evento. tabLiveCounts e liveRequestKeys são transitórios em storage.session, limitados às últimas 128 abas e até 256 chaves de requisição/regra por aba; são limpos ao fechar a aba ou ao encerrar a sessão. Esses IDs são gerados pelo navegador, não são credenciais da Twitch.

Em instalações da loja o evento imediato não é disponibilizado; o popup consulta getMatchedRules ao abrir e a cada 35 segundos enquanto está visível, respeitando recuo em erros/cotas. Essas consultas também atualizam Hoje/Total. Não há consulta periódica com o popup fechado nem envio para servidores do desenvolvedor. O bloqueio de rede funciona mesmo sem o contador aberto.

## Compartilhamento e controle

Não vendemos dados nem os compartilhamos com anunciantes ou serviços de análise. Os pedidos à Twitch descritos acima servem exclusivamente à reprodução do vídeo. O acesso ao GitHub por links de ajuda/privacidade só acontece quando você abre esses links; a política desse site se aplica à visita.

Você pode pausar a proteção pelo popup. A aba atual recarrega para aplicar a mudança; recarregue também outras abas abertas desse site para remover scripts que já estejam em execução. Desinstalar a extensão remove seu armazenamento local do perfil. Se você ativou o debug manualmente, remova a chave com localStorage.removeItem('bloqueioPessoal_twitchDebug') no console da Twitch; essa chave fica no armazenamento do site, fora do armazenamento da extensão.

As atualizações instaladas pela loja são distribuídas pelo Microsoft Edge Add-ons e estão sujeitas às políticas da Microsoft. A extensão não possui um atualizador remoto próprio.

## Contato

Dúvidas ou pedidos relacionados à privacidade: https://github.com/xdbixcoito-hub/ad-block-privacy/issues. As issues são públicas; não publique tokens, senhas, URLs privadas ou dados pessoais.
