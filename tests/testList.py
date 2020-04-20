import unittest
from todolist import create
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
        task = 'Task from unit test'
        details = 'Automatic test with random key %s-%s' % (r1, r2)
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

