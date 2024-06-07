
class TodoList():
    def __init__(self):
        self.tasks = []
        self.completed = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            raise ValueError(f'{task} not found in your current tasks')
    
    def show_tasks(self):
        return self.tasks

    def completed_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed.append(task)
        else:
            raise ValueError(f'{task} not found in your current tasks')
        
    def clear_all_tasks(self):
        self.tasks = []