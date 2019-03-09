# Descubra os alunos com as melhores notas do ENEM 2016.

Utilizando Python, Pandas e a base de dados do ENEM 2016, você deverá descobrir quem são as pessoas com maior desempenho nesta edição da prova.

## Tópicos

Neste desafio você aprenderá:

- Python
- Pandas

## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

Linux/macos

    pip3 install virtualenv
    virtualenv ../venv -p python3
    source ../venv/bin/activate 
    pip install -r requirements.txt

Windows

    pip3 install virtualenv
    virtualenv ..\venv -p python3
    ..\venv\Scripts\activate
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

## Detalhes

O contexto do desafio gira em torno dos resultados do ENEM 2016 (disponíveis no arquivo train.csv). Este arquivo, e apenas ele, deve ser utilizado para todos os desafios. Qualquer dúvida a respeito das colunas, consulte o [Dicionário dos Microdados do Enem 2016](https://s3-us-west-1.amazonaws.com/acceleration-assets-highway/data-science/dicionario-de-dados.zip).


Muitas universidades brasileiras utilizam o ENEM para selecionar seus futuros alunos e alunas. Isto é feito com uma média ponderada das notas das provas de matemática, ciências da natureza, linguagens e códigos, ciências humanas e redação. Determine os 20 melhores colocados, por ordem, para os pesos abaixo:

- matemática: 3
- ciências da natureza: 2
- linguagens e códigos: 1.5
- ciências humanas: 1
- redação: 3

Salve sua resposta em um arquivo chamado answer.csv com duas colunas: `NU_INSCRICAO` e `NOTA_FINAL`. A ordem das linhas ditará o rankeamento de quem fez a prova.
