import unittest
from todo_list.todo import TodoList

class TestTodoList(unittest.TestCase):
    def test_add_task(self):
        todo = TodoList()
        todo.add_task('Buy stocks')
        self.assertIn('Buy stocks', todo.tasks)

    def test_remove_task(self):
        todo = TodoList()
        todo.add_task('meditate')
        todo.remove_task('meditate')
        self.assertNotIn('meditate',todo.tasks)

    def test_list_tasks(self):
        todo = TodoList()
        todo.add_task('gym time')
        todo.add_task('read')
        todo.add_task('play sport')
        self.assertEqual(['gym time', 'read', 'play sport'], todo.tasks)
    
    def test_completed_tasks(self):
        todo = TodoList()
        todo.add_task('study')
        todo.add_task('code')
        todo.completed_task('code')
        self.assertIn('code', todo.completed)
        self.assertNotIn('code', todo.tasks)
