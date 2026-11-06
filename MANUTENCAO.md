# Manutenção de privacidade e suporte

## Responsabilidade e limites

Este repositório público mantém as políticas e os guias de ajuda do PapaAnúncio / AdChomper. Responsável pelo produto e conteúdo: Marco.elev. O código da extensão permanece privado.

## Fontes e arquivos gerados

- Editar PRIVACY.md e PRIVACY.en.md de forma equivalente; distinguir a versão publicada de uma candidata.
- Gerar index.html com `python3 scripts/render_privacy.py`; nunca corrigir somente o HTML.
- Manter SUPPORT.md e SUPPORT.en.md coerentes com os controles existentes e o diagnóstico voluntário.
- Preservar URLs e âncoras já usadas pela extensão/loja. Não publicar logs, tokens ou dados pessoais de relatos.

## Verificações

```sh
python3 scripts/render_privacy.py --check
python3 scripts/test_privacy.py
```

A CI também executa scripts/test-browser.cjs com Playwright fixado em 1.56.1: páginas locais, navegação PT/EN, foco, quatro larguras, zoom CSS e capturas. O workflow está em [.github/workflows/validate.yml](.github/workflows/validate.yml). Capturas de teste têm retenção de 14 dias. Não usar CI como certificação jurídica ou substituto de leitor de tela/zoom real.

## Alterar e integrar

1. Criar uma branch curta e PR com o conteúdo proposto.
2. Conferir PT/EN, links e resultados no SHA do PR.
3. Integrar após os testes e a revisão aplicável.
4. Se as fontes de política mudarem, coordenar a atualização da revisão/hash usada no build privado; não trocar cópias à mão sem conferir a origem.
5. Apagar a branch encerrada após confirmar que o conteúdo está na main. Preservar por tag qualquer commit exclusivo antes de remover uma pesquisa.

As pesquisas antigas foram preservadas em tags archive; elas não são políticas vigentes. Para recuperação, criar uma branch a partir da tag correspondente.

## Publicação e recuperação

GitHub Pages está desabilitado na conferência de encerramento da organização. As entradas públicas válidas são [português](PRIVACY.md), [inglês](PRIVACY.en.md) e os guias [PT](SUPPORT.md)/[EN](SUPPORT.en.md) no GitHub. index.html é uma apresentação gerada disponível no repositório, sem hospedagem Pages anunciada.

O workflow valida conteúdo; não publica uma versão da extensão. Em regressão, preparar um revert do commit e rodar os mesmos checks, preservando o histórico e as URLs. Alterações corretivas da política devem refletir o comportamento aplicável e manter rastreabilidade.
