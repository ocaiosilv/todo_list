import os

def emptyDict(taskDict):
    if not taskDict:
        print("Your to do list is empty")
        return False
    else:
        return True
    
def taskselector(taskDict):
    if emptyDict(taskDict) == True:
        base = "_" * (len(max(taskDict, key=len)))
        print(base)
        for k, i in enumerate(taskDict):
            print(k+1,"° - ",i," -> ", taskDict[i])
        print(base)
        while True:
            print("Please the number of the task: ")
            a = input(":  ")
            try:
                intA = int(a)
                for k,i in enumerate(taskDict):
                    if  intA == k+1:
                        return i
                print("Please, an valid number")
            except ValueError:
                print("Please, type an number")
    else:
        return None

def menu(taskDict): ##The basic menu
    print("Your toDo List")
    if taskDict:
        base = "_" * (len(max(taskDict, key=len)))
        print(base)
        for k, i in enumerate(taskDict):
            print(k+1,"° - ",i," -> ", taskDict[i])
        print(base)
    else:
        print("_____")
        print("empty")
        print("_____")
    print("Please choose an option:")
    print("1 - Add a new Task")
    print("2 - Update Task status")
    print("3 - Remove a Task")
    print("4 - Edit a Task")
    print("5 - Stop the program")
    while True:
        a = input(":  ")
        try:
            intA = int(a)
            if intA in [1,2,3,4,5]:
                break
            else:
               print("Please, type the number of one of the options")
        except ValueError: ## type error
            print("Please, type a number")
    return intA

def statusType(taskDict):
    if emptyDict(taskDict) == True:
        print("Select the number of the wanted status:")
        print("1- Work in progress")
        print("2- Pending")
        print("3- Done")
        while True:
            a = input(":  ")
            try:
                intA = int(a)
                if intA in [1,2,3]:
                    match intA:
                        case 1:
                            return "Work in progress"
                        case 2:
                            return "Pending"
                        case 3:
                            return "Done"
                else:
                    print("Please, type an valid status number")
            except ValueError:
                print("Please, type an number")
    