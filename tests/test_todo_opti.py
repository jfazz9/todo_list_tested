
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from todo_list.todo import TodoList
import unittest
from datetime import datetime
from todo_list.todo_opti import Task, TodoList


class TestToDo(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()
        
    def test_adding_task(self):
        self.todo.add_task('play tennis',"2024-06-08", 2)
        self.assertIn(Task('play tennis', "2024-06-08", 2), self.todo.tasks)

    def test_remove_task(self):
        self.todo.add_task('play tennis')
        descriptions = [task.description for task in self.todo.tasks]
        self.assertIn('play tennis', descriptions)
        self.todo.remove_task('play tennis')
        descriptions = [task.description for task in self.todo.tasks]
        self.assertNotIn('play tennis', descriptions)
        


if __name__=='__main__':
    unittest.main()