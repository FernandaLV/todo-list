import json
from bd.model import insertTask, selectAll
from flask import jsonify, make_response, abort
from django.core.serializers.json import DjangoJSONEncoder
import datetime


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


def read_all():

    todoList = selectAll()

    todoListR = {}

    for todoTask in todoList:

        idTask = todoTask[0]
        key = todoTask[1].strip()
        timestampCreate = todoTask[2]
        task = todoTask[3].strip()
        details = todoTask[4]
        status = todoTask[5].strip()

        todoListR[idTask] = {}

        todoListR[idTask]["key"] = key
        todoListR[idTask]["timestampCreate"] = timestampCreate
        todoListR[idTask]["task"] = task
        todoListR[idTask]["details"] = details
        todoListR[idTask]["status"] = status

    return todoListR

# def read_one(key):
#     if key in TODO:
#         task = TODO.get(key)
#     else:
#         abort(
#             404, "Not found"
#         )
#     return task


def create(data):
    
    key = data["key"]
    task = data["task"]
    details = data["details"]
    status = data["status"]
    
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


# def update(key, task):
#     if key in TODO:
#         TODO[key]["task"] = task.get("description")
#         TODO[key]["details"] = task.get("details")
#         TODO[key]["status"] = task.get("status")
        
#         return TODO[key]
#     else:
#         abort(
#             404, "{key} not found".format(key=key)
#         )

# def delete(key):
#     if key in TODO:
#         del TODO[key]
#         return make_response(
#             "{key} deleted".format(key=key), 200
#         )
#     else:
#         abort(
#             404, "{key} not found".format(key=key)
#         )
