import json
import os

def loadToDOList():
    lists = {}
    num = 1
    dir_path = r"C:\Users\Caio\Desktop\todo_list"

    for file in os.listdir(dir_path):
        if file.endswith(".json"):
            lists[num] = file
            print(num," - ",file)
            num +=1 

    print("Which list do you want to load?")
    while True:
        a = input(":  ")
        try:
            intA = int(a)
            if intA in lists:
                file_path = os.path.join(dir_path, lists[intA])
                with open(file_path, mode="r", encoding="utf-8") as read_file:
                    toDoList = json.load(read_file)
                return toDoList, lists[intA]
            else:
               print("Please, type the number of one of the options")
        except ValueError: 
            print("Please, type a number")

def saveToDoList(taskDict, name):
    if name != None:
        with open(name, mode="w", encoding="utf-8") as write_file:
            json.dump(taskDict, write_file, indent=4)
    else:
        print("Type the to-do routine name")
        name = ((input(":  "))+".json")
        with open(name, mode="w", encoding="utf-8") as write_file:
            json.dump(taskDict, write_file, indent=4)
        