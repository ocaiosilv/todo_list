def taskselector(taskDict):
    while True:
        try:
            intA = input(":  ")
            if intA in [1,2,3,4]:
                for k,i in enumerate(taskDict):
                    if taskNumber == k+1:
                        return i
            else:
                print("Please, type the number of one of the tasks")
        except ValueError:
            print("Please, type an number")

def menu(taskDict): ##The basic menu
    print("Your's to do List")
    base = "_" * (len(max(taskDict, key=len)))
    print(base)
    for k, i in enumerate(taskDict):
        print(k+1,"° - ",i," -> ", taskDict[i])
    print(base)
    print("Please choose an option:")
    print("1 - Add a new Task")
    print("2 - Update Task status")
    print("3 - Remove a Task")
    print("4 - Edit a Task")
    while True:
        a = input(":  ")
        try:
            intA = int(a)
            if intA in [1,2,3,4]:
                break
            else:
               print("Please, type the number of one of the options")
        except ValueError: ## type error
            print("Please, type an number")
    return intA

def statusType():
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
    