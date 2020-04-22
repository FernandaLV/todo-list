from bd.model import *
from flask import make_response, abort
from appmetrics import metrics

@metrics.with_histogram("read_all")
def readAll():

    todoList = selectAll()

    todoListR = []

    for todoTask in todoList:

        key = todoTask[1].strip()
        timestampCreate = todoTask[2]
        task = todoTask[3].strip()
        details = todoTask[4]
        status = todoTask[5].strip()

        todoListT = {}

        todoListT["key"] = key
        todoListT["timestampCreate"] = timestampCreate
        todoListT["task"] = task
        todoListT["details"] = details
        todoListT["status"] = status

        todoListR.append(todoListT)

    return todoListR

@metrics.with_histogram("read_one")
def readOne(key):

    todoListOne = selectOne(key)

    if todoListOne is None:
        abort(
            404, "Not found"
        )

    todoListOneR = {
        "key": todoListOne[0].strip(),
        "timestampCreate": todoListOne[1],
        "task": todoListOne[2].strip(),
        "details": todoListOne[3].strip(),
        "status": todoListOne[4].strip()
    }

    return todoListOneR

@metrics.with_histogram("create")
def create(data):
    
    key = data["key"]
    task = data["task"]
    status = data["status"]

    try:
        details = data["details"]
    except KeyError:
        details = None
    
    if (' ' in key):
        abort(
            400,
            "Invalid key. Cannot have spaces",
        )

    if (key == ''):
        abort(
            400,
            "Invalid key. Cannot be empty",
        )
    
    if (status != 'pending' and status != 'completed'):
        abort(
            400,
            "Status must be pending or completed",
        )
    
    idTask = insertTask(key, task, details, status)

    if idTask is not None:
        return make_response(
            "{key} created".format(key=key), 201
        )
    else:
        abort(
            406,
            "{key} error".format(key=key),
        )

@metrics.with_histogram("update")
def update(key, data):
    
    task = data["task"]
    status = data["status"]

    try:
        details = data["details"]
    except KeyError:
        details = None

    if (status != 'pending' and status != 'completed'):
        abort(
            400,
            "Status must be pending or completed",
        )
    
    idTask = updaeteTask(key, task, details, status)

    if idTask is not None:
        return make_response(
            "{key} updated".format(key=key), 200
        )
    else:
        abort(
            404, "{key} not found".format(key=key)
        )

@metrics.with_histogram("delete")
def delete(key):

    idTask = deleteTask(key)

    if idTask is not None:
        return make_response(
            "{key} deleted".format(key=key), 200
        )
    else:
        abort(
            404, "{key} not found".format(key=key)
        )