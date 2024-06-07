import unittest
from todo_list.todo import TodoList

class TestTodoList(unittest.TestCase):
    def test_add_task(self):
        todo = TodoList()
        todo.add_task('Buy GME', '2023-01-02')
        self.assertEqual([{'task':'Buy GME', 'due-date': '2023-01-02'}], todo.tasks)

    def test_due_date_format(self):
        todo = TodoList()
        with self.assertRaises(ValueError):
            todo.add_task("Buy groceries", due_date="invalid date")



    def test_remove_task(self):
        todo = TodoList()
        todo.add_task('meditate', '2023-01-09')
        todo.remove_task('meditate')
        
        # self.assertDictContainsSubset('meditate',todo.tasks)
        
'''
    def test_show_tasks(self):
        todo = TodoList()
        todo.add_task('gym time')
        todo.add_task('read')
        todo.add_task('play sport')
        self.assertEqual(['gym time', 'read', 'play sport'], todo.show_tasks())
    
    def test_completed_tasks(self):
        todo = TodoList()
        todo.add_task('study')
        todo.add_task('code')
        todo.completed_task('code')
        self.assertIn('code', todo.completed)
        self.assertNotIn('code', todo.tasks)
    
    def test_clear_tasks(self):
        todo = TodoList()
        todo.add_task('meeting')
        todo.add_task('network')
        todo.clear_all_tasks()
        self.assertEqual([], todo.tasks)
'''
if __name__=='__main__':
    unittest.main()