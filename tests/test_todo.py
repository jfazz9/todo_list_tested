import unittest
from todo_list.todo import TodoList

class TestTodoList(unittest.TestCase):
    def test_add_task(self):
        todo = TodoList()
        todo.add_task('Buy socks')
        self.assertIn('Buy socks', todo.tasks)

    def test_remove_task(self):
        todo = TodoList()
        todo.add_task('Celery')
        todo.remove_task('Celery')
        self.assertNotIn('Celery',todo.tasks)
    
    