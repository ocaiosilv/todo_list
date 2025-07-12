import os
from InquirerPy import prompt

def emptyDict(taskDict):
    if not taskDict:
        print("Your to do list is empty")
        return False
    else:
        return True
    
def taskselector(taskDict):
    choices = []
    if emptyDict(taskDict) == True:
        base = "_" * (len(max(taskDict, key=len)))
        print(base)
        for k, i in enumerate(taskDict):
            print(k+1,"° - ",i," -> ", taskDict[i])
            choices.append(i)
        print(base)
        options = [
        {
            "type": "list",
            "message": "Please select one option:",
            "choices": choices,
        }
        ]
        result = prompt(options)
        choice = result[0]
        return (choice)
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
    options = [
        {
            "type": "list",
            "message": "Please select one option:",
            "choices": ["Add a new Task", "Update Task status", "Remove a Task", "Edit a Task",
                        "Save the list", "Load a list", "Start a new list" , "Stop the program"]
        }
    ]
    result = prompt(options)
    choice = result[0]
    optionsList = options[0]["choices"]
    return (optionsList.index(choice) + 1)

def statusType(taskDict):
    if emptyDict(taskDict) == True:
        questions = [
        {
            "type": "list",
            "message": "Please select one option:",
            "choices": ["Work in progress", "Pending", "Done"]
        }
        ]
        result = prompt(questions)
        choice = result[0]
        return (choice)
    