# TODO-LIST

API RESTFUL de uma lista de tarefas (todo-list).

Nesta lista de tarefas o usuário grava:

* chave (key);
  * Uma chave única para a tarefa. Não pode conter espaços;
* tarefa (task);
  * A tarefa;
* status;
  * O status da tarefa pode ser pendente (pending) ou concluído (completed);
* detalhes (details);
  * Detalhes da tarefa. Não é obrigatório;
* Data e hora do cadastro;
  * O sistema grava automaticamente a data e hora em que a tarefa foi gravada na todo-list.
  

## Rodar a aplicação

Para instalar as bibliotecas python necessárias para a aplicação:

```bash
$ pip install flask-cors flask_swagger_ui connexion connexion[swagger-ui] appmetrics unittest2 py-healthcheck psycopg2-binary
# pode ser necessário colocar a versão do pip para rodar, como no exemplo abaixo:
$ pip3 install flask-cors flask_swagger_ui connexion connexion[swagger-ui] appmetrics unittest2 py-healthcheck psycopg2-binary
```


Para rodar os testes unitários:

```bash
$ python -m unittest test -v
# pode ser necessário colocar a versão do python para rodar, como no exemplo abaixo:
$ python3 -m unittest test -v
```

![Resultado dos testes](resources/images/img_test.png)


Para rodar a aplicação python:

```bash
$ python server.py
# pode ser necessário colocar a versão do python para rodar, como no exemplo abaixo:
$ python3 server.py
```

## Documentações da aplicação

Com a aplicação rodando, é possível visualiar a documentação swagger, healthcheck e métricas.

*Obs: `<url da aplicação>` -> se a aplicação estiver localmente é `localhost:5000`*



Para visualização da documentação swagger:
`<url da aplicação>/ui/`

![Swagger da API](resources/images/img_swagger.png)

Para a visualização do healthcheck:
`<url da aplicação>/healthcheck`

![Healthcheck da API](resources/images/img_healthcheck.png)

Para a visualização de todas as métricas:
`<url da aplicação>/metrics`

![Métricas da API](resources/images/img_metrics.png)

Para visualização das metrícas conforme a operação:
* `<url da aplicação>/metrics/create`
* `<url da aplicação>/metrics/read_all`
* `<url da aplicação>/metrics/read_one`
* `<url da aplicação>/metrics/update`
* `<url da aplicação>/metrics/delete`


## Banco de dados

Este projeto está utilizando um banco de dados postgresql.

Os dados do banco estão localizados no arquivo [resources/database.ini](resources/database.ini), para utilizar outro banco bassta modificar este arquivo.

Este projeto está configurado para utilizar um banco de dados criado na plataforma do [heroku](https://heroku.com) para testes públicos.


[Documentação do Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql)


Para criar a tabela que o projeto está utilizando, basta rodar o arquivo [resources/migration.sql](resources/migration.sql)
