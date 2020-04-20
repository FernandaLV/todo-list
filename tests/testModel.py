import unittest
from bd.model import insertTask, selectAll
import random

class TestModelMethods(unittest.TestCase):

    def test_insert(self):
        r1 = random.randint(1,99)
        r2 = random.randint(1,99)
        
        key = 'unit-test-%s-%s' % (r1, r2)
        task = 'Task from unit test'
        details = 'Automatic test with random key %s-%s' % (r1, r2)
        status = 'pending'

        idTask = insertTask(key, task, details, status)
        
        self.assertIsNotNone(idTask)

    def test_all(self):
        
        todoList = selectAll()

        self.assertIsNotNone(todoList)
