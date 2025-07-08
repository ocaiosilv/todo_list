class TaskManager:
    def __init__(self):
        self._tasks = {}
        self._wipTask = None
        self._wip = False

    def taskDict(self):
        return self._tasks
    
    def clearDict(self):
        self._tasks.clear()
        
    def addTask(self, task):
        if task in self._tasks:
            print("This task is already in your's toDo list")
        else:
            self._tasks.update({task: "Pending"})

    def changeStatus(self, task, status):
        if task != None:
            if status == "Work in progress" and self._wip == False:
                self._wip = True
                self._wipTask = task
                self._tasks[task] = status
            elif status == "Work in progress" and self._wip == True:
                print(f"There's already a work in progress task: {self._wipTask}")
                print("Do you wish to switch the WIP task?")
                print("1 - Yes")
                print("2 - No")
                while True:
                    try:
                        choice = int(input("Choose an option (1 or 2): ").strip())
                        if choice == 1:
                            self._tasks[self._wipTask] = "Pending" 
                            self._wipTask = task
                            self._tasks[task] = status
                            print(f"WIP task switched to: {task}")
                            break
                        elif choice == 2:
                            print(f"Keeping current WIP task: {self._wipTask}")
                            break
                        else:
                            print("Invalid option. Please enter 1 or 2.")
                    except ValueError:
                        print("Invalid input. Please enter a number (1 or 2).")
            else:
                if status != self._tasks[task]:
                    self._tasks[task] = status
                else:
                    print(f"The task in already {status}")

    def editTask(self, oldTask):
        if oldTask != None:
            status = self._tasks[oldTask]
            print(f"The old task: {oldTask}")
            self._tasks.pop(oldTask)
            print("Please, type the eddited task")
            TaskManager.addTask(self, str(input(":  ")))

    def removeTask(self, task):
        if task == self._wipTask:
            self._wipTask = None
            self._wip = False
        if task != None:
            self._tasks.pop(task)
        