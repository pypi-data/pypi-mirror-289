# SPED para python

Biblioteca para visualização de um arquivo sped em estrutura de tabelas do Pandas.
Utiliza o relacionamento hierarquico típico da estrutura do SPED FISCAL (EFD, ECD e entre outros)

A ideia seria visualizar em formato de tabela todas as informações de um registro e seus registros pais, por exemplo:

0000    NOME        DT_INI      DT_FIN      CNPJ                C100    COD_PART    SER NUM_DOC VLR_DOC C170    COD_ITEM    VLR_ITEM
0000    EMPRESAX    01/01/2024  31/01/2024  11.111.111/0001-91  C100    PART1       001 1111    1000,00 C170    PRODA       800,00 
0000    EMPRESAX    01/01/2024  31/01/2024  11.111.111/0001-91  C100    PART1       001 1111    1000,00 C170    PRODB       200,00 
0000    EMPRESAX    01/01/2024  31/01/2024  11.111.111/0001-91  C100    PART1       001 1112    300,00  C170    PRODC       300,00 


## Requisitos

- xsdata
- spedpy
- pandas

## Como instalar

    $ pip install spedpyutils