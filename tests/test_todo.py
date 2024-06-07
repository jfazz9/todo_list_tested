import unittest
from datetime import datetime
from todo_list.todo import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList()

    def test_add_task(self):
        self.todo.add_task('Buy GME', '2023-01-02')
        self.assertEqual([{'task':'Buy GME', 'due-date': '2023-01-02'}], self.todo.tasks)

    def test_due_date_format(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("Buy groceries", due_date="invalid date")

    def test_remove_task(self):
        self.todo.add_task('meditate', '2023-01-09')
        self.todo.remove_task('meditate')
        self.assertNotIn([{'task': 'meditate', 'due-date': datetime.today().strftime('%Y-%m-%d')}], self.todo.tasks)
        
    def test_show_tasks(self):
        self.todo.add_task('gym time', '2023-01-09')
        self.todo.add_task('read', '2023-01-09')
        self.todo.add_task('play sport', '2023-01-09')
        self.assertEqual([{'task':'gym time', 'due-date': '2023-01-09'},
                          {'task': 'read', 'due-date': '2023-01-09'},
                           {'task': 'play sport', 'due-date': '2023-01-09'}], self.todo.show_tasks())

    
    def test_completed_tasks(self):
        self.todo.add_task('study')
        self.todo.add_task('code')
        self.todo.completed_task('code')
        self.assertIn({'task': ' code', 'due-date': datetime.today().strftime('%Y-%m-%d')}, self.todo.completed)
        self.assertNotIn({'task': ' code', 'due-date': datetime.today().strftime('%Y-%m-%d')}, self.todo.tasks)
    ''' 
    def test_clear_tasks(self):
        todo = TodoList()
        todo.add_task('meeting')
        todo.add_task('network')
        todo.clear_all_tasks()
        self.assertEqual([], todo.tasks)
'''
if __name__=='__main__':
    unittest.main()