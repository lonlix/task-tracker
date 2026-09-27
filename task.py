import json
class Task:
    def __init__(self, name, deadline, done=False):
        self.name = name
        self.deadline = deadline
        self.done= done
    def __str__(self):
        return f"Task - {self.name}, Deadline: {self.deadline}, Done: {self.done}"
    def to_dict(self):
        return {
            "name": self.name,
            "deadline": self.deadline,
            "done": self.done
        }
    def mark_done(self):
            self.done = True
#   def __repr__(self): - допишу когда откладка нужнеа будет
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for index,task in enumerate(self.tasks, start=1):
            print(f'{index}. {task}')

    def get_task(self,number):
        if not isinstance(number, int):
            raise TypeError("Должно быть число")
        elif number > len(self.tasks) or number < 1:
            raise ValueError("Некоректное значение")
        else:
            return self.tasks[number - 1]

    def task_done(self, number):
        task = self.get_task(number)
        task.mark_done()



    
