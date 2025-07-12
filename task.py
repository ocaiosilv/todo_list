from InquirerPy import prompt


class TaskManager:
    def __init__(self):
        self.__tasks = {}
        self.__wipTask = None
        self.__wip = False

    def loadTasks(self, toLoad):
        self.clearDict() 
        self.__tasks = toLoad

    def taskDict(self):
        return self.__tasks
    
    def clearDict(self):
        if self.__tasks:
            self.__tasks.clear()
        
    def addTask(self, task):
        if task in self.__tasks:
            print("This task is already in your's toDo list")
        else:
            self.__tasks.update({task: "Pending"})

    def changeStatus(self, task, status):
        if task != None:
            if status == "Work in progress" and self.__wip == False:
                self.__wip = True
                self.__wipTask = task
                self.__tasks[task] = status
            elif status == "Work in progress" and self.__wip == True:
                print(f"There's already a work in progress task: {self.__wipTask}")
                print("Do you wish to switch the WIP task?")
                yesOrNo = [
                    {"type": "confirm", "message": "Confirm?"},
                ]
                result = prompt(yesOrNo)
                choice = result[0]
                if choice == True:
                    self.__tasks[self.__wipTask] = "Pending" 
                    self.__wipTask = task
                    self.__tasks[task] = status
                    print(f"WIP task switched to: {task}")
                elif choice == False:
                    print(f"Keeping current WIP task: {self.__wipTask}")
            else:
                if status != self.__tasks[task]:
                    self.__tasks[task] = status
                else:
                    print(f"The task in already {status}")

    def editTask(self, oldTask):
        if oldTask != None:
            status = self.__tasks[oldTask]
            print(f"The old task: {oldTask}")
            self.__tasks.pop(oldTask)
            print("Please, type the eddited task")
            newTaskContent = str(input(":  "))
            self.addTask(newTaskContent)
            if newTaskContent in self.__tasks:
                self.__tasks[newTaskContent] = status

    def removeTask(self, task):
        if task == self.__wipTask:
            self.__wipTask = None
            self.__wip = False
        if task != None:
            self.__tasks.pop(task)
        