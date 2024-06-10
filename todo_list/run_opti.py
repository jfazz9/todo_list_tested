from todo_opti import TodoList

if __name__=='__main__':
    todo = TodoList()
    todo.add_task(999)
    print(todo.show_tasks_info())