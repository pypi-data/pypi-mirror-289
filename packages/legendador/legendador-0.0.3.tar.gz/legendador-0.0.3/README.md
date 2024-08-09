# Legendador

## Sintaxe
Usage: legendador [OPTIONS] URL

Options:
  -l, --language TEXT  linguagem falada no video
  -t, --to TEXT        linguagem da legenda
  -m, --mobile TEXT    faz o video na horizontal com um fundo dado como
                       parametro
  --help               Show this message and exit.


## Exemplo de Execução

legendador -l pt -t en https://www.youtube.com/shorts/yTk8i1CYvmg


## Possiveis erros

Erro no google translator : AttributeError: 'NoneType' object has no attribute 'group'

Veja o seguinte link para resolver o problema

https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group