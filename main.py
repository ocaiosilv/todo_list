from task import TaskManager
from ui import menu, taskselector, statusType
from storage import loadToDOList, saveToDoList
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    tasks = TaskManager()
    print("Your toDo List")
    print("_____")
    print("empty")
    print("_____")
    
    print("Please start with adding a task:")
    tasks.addTask(str(input(":  ")))
    print("Very Well")
    name = None

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        taskDict = tasks.taskDict()
        res = menu(taskDict)
        match res:
            case 1:
                print("Please, type the task content: ")
                tasks.addTask(str(input(":  ")))
            case 2:
                tasks.changeStatus(taskselector(taskDict), statusType(taskDict))
            case 3:
                tasks.removeTask(taskselector(taskDict))
            case 4:
                tasks.editTask(taskselector(taskDict))
            case 5:
                name = saveToDoList(taskDict, name)
            case 6:
                loadedList, name_loaded  = loadToDOList()
                if loadedList is not None:
                    tasks.loadTasks(loadedList)
                    name = name_loaded
                else:
                    pass
            case 7:
                tasks.clearDict()
                name = None
            case 8:
                print("Stopping...")
                break
            

if __name__ == "__main__":
    main()

