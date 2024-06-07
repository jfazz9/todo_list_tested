
class TodoList():
    def __init__(self):
        self.tasks = []
        self.completed = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self,task):
        self.tasks.remove(task)

    def completed_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed.append(task)
        