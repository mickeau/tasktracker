#Task Tracker

import datetime
import json
import os
import sys

TaskCounter = 1
# Open and read the JSON file
# TODO: add TaskCounter variable to JSON file
if os.path.exists('tasktracker.json'):
    with open('tasktracker.json', 'r') as file:
        taskList = json.load(file)
        TaskCounter = taskList[0]["taskCounter"]
        
else:
    taskList = []
    taskList.append(dict(id = 0, taskCounter = 1))

#Convert timestamp to readable date and time format
def timeConvert(timestr):
    time = timestr.strftime("%A, %d %B %Y %I:%M %p")
    return time

now = timeConvert(datetime.datetime.now())


def update_JSON():
    # Serializing json
    json_object = json.dumps(taskList, indent=4)
    
    # Writing to sample.json
    with open("tasktracker.json", "w") as outfile:
        outfile.write(json_object)

# add Task to task list using command line argument "add"
def add(description):
    global TaskCounter
    newTask = {
        "id": TaskCounter,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,

    }
    taskList.append(newTask)
    print(description, "added to todo list with ID:", TaskCounter)
    TaskCounter += 1
    taskList[0]["taskCounter"] = TaskCounter
    update_JSON()

def update(id, description):
    match = False
    # loop through dictionary list to find correct dictionary
    for task in taskList:
        if str(task["id"]) == id:
            match = True
            task["description"] = description
            task["updatedAt"] = now
            print("Task", id, "updated to", task["description"])
            break
    if match == False:
        print("Error: No task with id", id)

    update_JSON()

def markInProgress(id):
    match = False
    # loop through dictionary list to find correct dictionary
    for task in taskList:
        if str(task["id"]) == id:
            match = True
            task["status"] = "in progress"
            task["updatedAt"] = now
            print(task["description"], "marked as in progress")
            break
    if match == False:
        print("Error: No task with id", id)

    update_JSON()

def markDone(id):
    match = False
    # loop through dictionary list to find correct dictionary
    for task in taskList:
        if str(task["id"]) == id:
            match = True
            task["status"] = "done"
            task["updatedAt"] = now
            print(task["description"], "marked as done")
            break
    if match == False:
        print("Error: No task with id", id)

    update_JSON()        

def delete(id):
    match = False
    for task in taskList:
        if str(task["id"]) == id:
            match = True
            taskList.remove(task)
            print(task["description"], "removed from todo list")
            break
    if match == False:
        print("Error: No task with id", id)


    update_JSON()
    
def list():
    print("\nList of all tasks:\n")
    for task in taskList:
        if task["id"] > 0:
            print(task["id"], ":", task["description"])
    print("\n")

def listDone():
    print("\nList of completed tasks:\n")
    for task in taskList:
        if task["id"] > 0:
            if task["status"] == "done":
                print(task["id"], ":", task["description"])

def listInProgress():
    print("\nList of tasks in progress:\n")
    for task in taskList:
        if task["id"] > 0:
            if task["status"] == "in progress":
                print(task["id"], ":", task["description"])

def listToDo():
    print("\nList of tasks yet to be done:\n")
    for task in taskList:
        if task["id"] > 0:
            if task["status"] == "todo":
                print(task["id"], ":", task["description"])

if __name__ == "__main__":
    try:
        args = sys.argv
        # args[0] = current file
        # args[1] = function name
        # args[2:] = function args : (*unpacked)
        globals()[args[1]](*args[2:])
    except:
        print("User input error. Please check your arguments and try again.")