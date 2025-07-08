from task import task
from ui import menu, taskselector, statusType

def main():
    tasks = task()
    print("Your's to do List")
    print("_____")
    print("empty")
    print("_____")
    
    print("Please start with adding a task:")
    tasks.addTask(str(input(":  ")))
    print("Very Well")

    while True:
        res = menu(tasks.taskDict())
        match res:
            case 1:
                tasks.addTask(str(input(":  ")))
            case 2:
                tasks.changeStatus(taskselector(tasks.taskDict()),statusType())
            case 3:
                tasks.removeTask(taskselector())
            case 4:
                tasks.editTask(taskselector())
            

if __name__ == "__main__":
    main()

