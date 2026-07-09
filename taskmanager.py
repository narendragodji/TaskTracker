import datetime as dt

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.task_id = 1

    def add_task(self,task):
        self.tasks[self.task_id] ={
            "description": task,
            "status": "todo",
            "createdAt": str(dt.datetime.now()),
            "updatedAt": str(dt.datetime.now())
        }
        print(f"Task added successfully (ID: {self.task_id})")
        self.task_id +=1

    def task_update(self,task,task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["description"] = task
            self.tasks[task_id]["updatedAt"] = str(dt.datetime.now())
            print(f"Task Updated sucessfully")

        else:
            print("Task does not exist")

    def delete(self,task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted")

    def task_list(self,status):
        if status:
            for id,dic in self.tasks.items():
                 for i,j in dic.items():
                   

        else:
            for id,dic in self.tasks.items():
                print(f"{id} : {dic}")


