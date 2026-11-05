# Trabalho neste repositório público

Este repositório contém políticas e suporte. Não incluir runtime privado da extensão, logs pessoais ou credenciais.

- Preservar URLs de PRIVACY.md e PRIVACY.en.md; index.html é gerado por scripts/render_privacy.py a partir das fontes PT/EN.
- Distinguir versão publicada de candidata. Conferir comportamento antes de mudar a política; não substituir apenas o número da versão.
- Políticas PT/EN devem permanecer equivalentes; não inventar traduções jurídicas para outros idiomas.
- Issues são públicas: orientar remoção de tokens e URLs privadas. Vulnerabilidades não devem ser detalhadas publicamente.
- Prévia estática: python3 -m http.server 8000; abrir localhost:8000. CI de conteúdo e navegador em .github/workflows/validate.yml; verificar resultado do SHA em revisão. Execute python3 scripts/render_privacy.py --check e python3 scripts/test_privacy.py.
- Antes de mudança visual, testar links, títulos/idioma, teclado, viewport 320px e zoom 200%. Não declarar esses testes executados sem evidência.
- Mudanças em Pages podem publicar conteúdo após merge; preparar PR e conferir origem de publicação.
- Ajustes reversíveis seguem a autorização da tarefa. Não exigir aprovação extra por rotina documental.
