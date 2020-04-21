import unittest
from bd.model import *
import random

class TestModelMethods(unittest.TestCase):

    def test_insert(self):
        r1 = random.randint(10,99)
        r2 = random.randint(10,99)
        
        key = 'unit-test-%s-%s' % (r1, r2)
        task = 'Task from unit test - model'
        details = 'Automatic test insert with random key %s-%s' % (r1, r2)
        status = 'pending'

        idTask = insertTask(key, task, details, status)
        
        self.assertIsNotNone(idTask)

    def test_all(self):
        
        todoList = selectAll()

        self.assertIsNotNone(todoList)

    def test_one(self):

        # insert a task to read after
        r1 = random.randint(10,99)
        r2 = random.randint(10,99)
        
        key = 'unit-test-%s-%s' % (r1, r2)
        task = 'Task from unit test - model'
        details = 'Automatic test select one with random key %s-%s' % (r1, r2)
        status = 'pending'

        idTask = insertTask(key, task, details, status)

        self.assertIsNotNone(idTask)

        todoListOne = selectOne(key)

        self.assertIsNotNone(todoListOne)