import json
import os
from InquirerPy import prompt

dir_path = os.path.dirname(os.path.abspath(__file__))
toDo_dir = os.path.join(dir_path, "toDo_lists")

os.makedirs(toDo_dir, exist_ok=True) #

def loadToDOList():
    lists = []


    for file in os.listdir(toDo_dir):
        if file.endswith(".json"):
            lists.append(file)
    if not lists:
        print("There's no stored routine files, please add one first")
        return None, None
    
    print("Which list do you want to load?")
    options = [{
            "type": "list",
            "message": "Please select one option:",
            "choices": lists,
        }]
    result = prompt(options)
    choice = result[0]
    file_path = os.path.join(toDo_dir, choice)
    with open(file_path, mode="r", encoding="utf-8") as read_file:
        toDoList = json.load(read_file)
    return toDoList, choice


def saveToDoList(taskDict, name):
    if name == None:
        print("Type the to-do routine name")
        name = ((input(":  "))+".json")
        
    path_complete= os.path.join(toDo_dir, name)
    with open(path_complete, mode="w", encoding="utf-8") as write_file:
        json.dump(taskDict, write_file, indent=4)
    return name