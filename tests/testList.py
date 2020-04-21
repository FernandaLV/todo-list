import unittest
from todolist import *
import random
import connexion
from flask_cors import CORS
import json


class TestListMethods(unittest.TestCase):

    def setUp(self):
        app = connexion.App(__name__, specification_dir='../resources/')
        app.add_api('swagger.yml')
        self.app =  app.app.test_client()

    def test_create(self):

        r1 = random.randint(10,99)
        r2 = random.randint(10,99)
        
        key = 'unit-test-list-%s-%s' % (r1, r2)
        task = 'Task from unit test - list'
        details = 'Automatic test create with random key %s-%s' % (r1, r2)
        status = 'pending'

        data = {
            "key": key,
            "task": task,
            "details": details,
            "status": status
        }

        header = {"content-type": "application/json"}

        response = self.app.post("/api/todo-list",data=json.dumps(data), headers=header)

        dataReturn = '%s created' % (key)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, dataReturn.encode())

    def test_read_all(self):
        # read all todo list
        response = self.app.get(
            "/api/todo-list",
            headers=header
        )

        self.assertEqual(response.status_code, 200)

    def test_read_one(self):

        # insert a task to read after
        r1 = random.randint(10,99)
        r2 = random.randint(10,99)
        
        key = 'unit-test-list-%s-%s' % (r1, r2)
        task = 'Task from unit test - list'
        details = 'Automatic test read one with random key %s-%s' % (r1, r2)
        status = 'pending'

        data = {
            "key": key,
            "task": task,
            "details": details,
            "status": status
        }

        header = {"content-type": "application/json"}

        response = self.app.post(
            "/api/todo-list",
            data=json.dumps(data),
            headers=header
        )

        dataReturn = '%s created' % (key)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, dataReturn.encode())

        # read the task
        response = self.app.get(
            "/api/todo-list/%s" % key,
            headers=header
        )

        returnData = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(returnData["key"], key)

    def test_update(self):

        # insert a task to read after
        r1 = random.randint(10,99)
        r2 = random.randint(10,99)
        
        key = 'unit-test-list-%s-%s' % (r1, r2)
        task = 'Task from unit test - list'
        details = 'Automatic test one with random key %s-%s' % (r1, r2)
        status = 'pending'

        data = {
            "key": key,
            "task": task,
            "details": details,
            "status": status
        }

        header = {"content-type": "application/json"}

        response = self.app.post(
            "/api/todo-list",
            data=json.dumps(data),
            headers=header
        )

        dataReturn = '%s created' % (key)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, dataReturn.encode())

        # update the task
        task = 'Task from unit test - model'
        details = 'Automatic test update with random key %s-%s' % (r1, r2)
        status = 'completed'

        data = {
            "task": task,
            "details": details,
            "status": status
        }

        response = self.app.put(
            "/api/todo-list/%s" % key,
            data=json.dumps(data), 
            headers=header
        )

        dataReturn = '%s updated' % (key)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, dataReturn.encode())

    def test_delete(self):

        # insert a task to delete after
        r1 = random.randint(10,99)
        r2 = random.randint(10,99)
        
        key = 'unit-test-list-%s-%s' % (r1, r2)
        task = 'Task from unit test - list'
        details = 'Automatic test delete with random key %s-%s' % (r1, r2)
        status = 'pending'

        data = {
            "key": key,
            "task": task,
            "details": details,
            "status": status
        }

        header = {"content-type": "application/json"}

        response = self.app.post(
            "/api/todo-list",
            data=json.dumps(data),
            headers=header
        )

        dataReturn = '%s created' % (key)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, dataReturn.encode())

        # delete the task
        response = self.app.delete(
            "/api/todo-list/%s" % key,
            headers=header
        )

        dataReturn = '%s deleted' % (key)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, dataReturn.encode())
