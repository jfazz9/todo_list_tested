from datetime import datetime
class TodoList():
    def __init__(self):
        self.tasks = []
        self.completed = []

    def add_task(self, task, due_date=datetime.today().strftime('%Y-%m-%d')):
        '''add task to the to do list, entry of date should be yyyy-mm-dd'''
        if due_date and not self._validate_due_date(due_date):
            raise ValueError('Invalid due date format')
        self.tasks.append({"task": task, "due-date": due_date})
    
    def _validate_due_date(self, due_date):
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def remove_task(self, task):
        for tasks in self.tasks:
            if tasks['task'] == task:
                self.tasks.remove(tasks)
            else:
                raise ValueError(f'{task} not found in your current tasks')
    
    def show_tasks(self):
        return self.tasks

    def completed_task(self, task):
        for tasks in self.tasks:
            if tasks['task'] == task:
                self.tasks.remove(tasks)
                self.completed.append(tasks)
                return
        raise ValueError(f'{task} not found in your current tasks')
        
    def clear_all_tasks(self):
        self.tasks = []
        self.completed = []