"""from tarefa import """
def menu(tasks_list): ##The basic menu
    print("Your's to do List")
    base = "_" * (len(max(tasks_list, key=len)))
    print(base)
    number = 1
    for i in tasks_list:
        print(number,"° - ",i," -> ", tasks_list[i])
        number +=1
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
    return a

def main():
    tasksDict = {}
    print("Your's to do List")
    print("_________________________________________________________")
    print("                          empty                          ")
    print("_________________________________________________________")
    
    print("Please start with adding a task:")
    tasksDict.update({str(input()):" Work in progress"})
    print("Very Well")

    while True:
        res = menu(tasksDict)
        match res:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            

if __name__ == "__main__":
    main()

