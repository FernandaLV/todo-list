# TODO-LIST

API RESTFUL de uma lista de tarefas.

# Rodar a aplicação

Para instalar as bibliotecas python necessárias para a aplicação:

```bash
$ pip install flask-cors flask_swagger_ui connexion connexion[swagger-ui] appmetrics unittest json
# pode ser necessário colocar a versão do pip para rodar, como no exemplo abaixo:
$ pip3 install flask-cors flask_swagger_ui connexion connexion[swagger-ui] appmetrics unittest json
```


Para rodar os tests unitários:

```bash
$ python -m unittest test
# pode ser necessário colocar a versão do python para rodar, como no exemplo abaixo:
$ python3 -m unittest test
```


Para rodar a aplicação python:

```bash
$ python server.py
# pode ser necessário colocar a versão do python para rodar, como no exemplo abaixo:
$ python3 server.py
```

## Documentações da aplicação

Com a aplicação rodando, é possível visualiar a documentação swaager, healthcheck e métricas.

Obs: `<url da aplicação>` -> se a aplicação estiver localmente é `localhost:5000`


Para visualização da documentação swagger:
`<url da aplicação>`/ui/

Para a visualização do healthcheck:
`<url da aplicação>`/healthcheck

Para a visualização das métricas:
`<url da aplicação>`/metrics


# Banco de dados

Este projeto está utilizando um banco de dados postgresql.

Os dados do banco estão localizados no arquivo [resources/databese.ini](resources/databese.ini), para utilizar outro banco bassta modificar este arquivo.

Este projeto está configurado para utilizar um banco de dados criado na plataforma do [heroku](https://heroku.com) para testes publicos.


[Documentação do Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql)


Para criar a tabela que o projeto está utilizando, basta rodar o arquivo [resources/migration.sql](resources/migration.sql)