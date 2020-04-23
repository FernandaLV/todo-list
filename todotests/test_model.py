import unittest
from bd.model import *
import random

class TestModelMethods(unittest.TestCase):

    def test_insert(self):
        r1 = random.randint(100,999)
        r2 = random.randint(100,999)
        
        key = 'unit-test-%s-%s' % (r1, r2)
        task = 'Task from unit test - model'
        details = 'Automatic test insert with random key %s-%s' % (r1, r2)
        status = 'pending'

        idTaskInsert = insertTask(key, task, details, status)
        
        self.assertIsNotNone(idTaskInsert)

    def test_select_all(self):
        
        todoList = selectAll()

        self.assertIsNotNone(todoList)

    def test_select_one(self):

        # insert a task to read after
        r1 = random.randint(100,999)
        r2 = random.randint(100,999)
        
        key = 'unit-test-%s-%s' % (r1, r2)
        task = 'Task from unit test - model'
        details = 'Automatic test select one with random key %s-%s' % (r1, r2)
        status = 'pending'

        idTaskInsert = insertTask(key, task, details, status)

        self.assertIsNotNone(idTaskInsert)

        # read the task
        todoListOne = selectOne(key)

        self.assertIsNotNone(todoListOne)

    def test_update(self):

        # insert a task to update after
        r1 = random.randint(100,999)
        r2 = random.randint(100,999)
        
        key = 'unit-test-%s-%s' % (r1, r2)
        task = 'Task from unit test - model'
        details = 'Automatic test with random key %s-%s' % (r1, r2)
        status = 'pending'

        idTaskInsert = insertTask(key, task, details, status)

        self.assertIsNotNone(idTaskInsert)

        # update the task
        task = 'Task from unit test - model'
        details = 'Automatic test update with random key %s-%s' % (r1, r2)
        status = 'completed'

        idTaskUpdate = updaeteTask(key, task, details, status)

        self.assertIsNotNone(idTaskUpdate)

    def test_delete(self):

        # insert a task to delete after
        r1 = random.randint(100,999)
        r2 = random.randint(100,999)
        
        key = 'unit-test-%s-%s' % (r1, r2)
        task = 'Task from unit test - model'
        details = 'Automatic test delete with random key %s-%s' % (r1, r2)
        status = 'pending'

        idTaskInsert = insertTask(key, task, details, status)

        self.assertIsNotNone(idTaskInsert)

        # delete the task
        idTaskDelete = deleteTask(key)

        self.assertIsNotNone(idTaskDelete)
