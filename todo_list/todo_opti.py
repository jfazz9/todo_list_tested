from datetime import datetime

class Validator:
    @staticmethod
    def _validate_due_date(due_date):
        '''validate the input date'''
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    @staticmethod
    def _validate_priority(priority):
        '''validate priority level'''
        if isinstance (priority, int) and (int(priority) >= 1 and int(priority) <=5):
            return True
        raise ValueError('enter a number between 1 and 5')

class Task:
    def __init__(self, description, due_date=None, priority=1):
         # Ensure due_date is a string or None
        if due_date is not None and not isinstance(due_date, str):
            raise TypeError("due_date must be a string in 'yyyy-mm-dd' format or None")
        self.description = description
        self.due_date = due_date if due_date and Validator._validate_due_date(due_date) else datetime.today().strftime('%Y-%m-%d')
        self.priority = priority if priority and Validator._validate_priority(priority) else 1

    def __repr__(self):
        return f'Task (description={self.description}, Due-date={self.due_date}, Priority={self.priority})'
    
    def __eq__(self, other):
        if isinstance(other, Task):
            return self.description == other.description and self.due_date == other.due_date
        return False

class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed = []

    def add_task(self, description, due_date=None, priority=1):
        '''add task to the to do list, entry of date should be yyyy-mm-dd'''
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def remove_task(self, task_name):
        task_to_remove = next(task for task in self.tasks if task.description == task_name)
        if task_to_remove:
            self.tasks.remove(task_to_remove)
        else:
            raise ValueError('task not in current list')

    def show_task_name(self):
        current_task = []
        for task in self.tasks:
            current_task.append(task.description)
        return current_task

    def show_tasks_info(self):
        tasks = []
        for task in self.tasks:
            tasks.append(task)
        return tasks

    def completed_task(self, task):
        for tasks in self.tasks:
            if tasks.description == task:
                self.completed.append(tasks)
                self.tasks.remove(tasks)
                return
        raise ValueError(f'{task} not found in your current tasks')
        
    def clear_all_tasks(self):
        self.tasks = []
        self.completed = []
