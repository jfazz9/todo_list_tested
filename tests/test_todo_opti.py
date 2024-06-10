
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
    
    def test_show_task_name(self):
        self.todo.add_task('play tennis')
        self.todo.add_task('code')
        self.todo.add_task('read')
        self.assertIn('play tennis', self.todo.show_task_name())

    def test_show_task_info(self):
        expected_tasks = [
            Task("gym", "2024-06-10", 1, None),
            Task("swim", "2024-06-10", 1,None),
            Task("encapsulation", '2024-06-09', 3, None)
        ]
        self.todo.add_task('gym')
        self.todo.add_task('swim')
        self.todo.add_task('encapsulation', '2024-06-09', 3)
        self.assertEqual(expected_tasks, self.todo.show_tasks_info())

    def test_add_dependency(self):
        task1 = Task('eat', priority=2)
        task2 = Task('sleep', priority=5)
        self.todo.add_task(task1.description, priority=task2.priority)
        self.todo.add_task(task2.description, priority=task2.priority, dependencies=[task1])
        task2.add_dependency(task1)
        self.assertIn(task2, self.todo.tasks)
        self.assertIn(task1, task2.dependencies)

    def test_completed_tasks(self):
        completed_tasks = [
            Task('compose music')
        ]
        self.todo.add_task('compose music')
        self.todo.completed_task('compose music')
        self.assertEqual(completed_tasks, self.todo.completed)
    
    def test_clear_tasks(self):
        self.todo.add_task('read')
        self.todo.add_task('tennis')
        self.todo.clear_all_tasks()
        self.assertEqual([], self.todo.tasks)

if __name__=='__main__':
    unittest.main()
