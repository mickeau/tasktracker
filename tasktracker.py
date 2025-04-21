#Task Tracker
'''Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.

Task Properties
Each task should have the following properties:

id: A unique identifier for the task
description: A short description of the task
status: The status of the task (todo, in-progress, done)
createdAt: The date and time when the task was created
updatedAt: The date and time when the task was last updated
Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.'''

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
    print("List of all tasks:\n")
    for task in taskList:
        if task["id"] > 0:
            print(task["description"])

def listDone():
    print("List of completed tasks:\n")
    for task in taskList:
        if task["id"] > 0:
            if task["status"] == "done":
                print(task["description"])

def listInProgress():
    print("List of tasks in progress:\n")
    for task in taskList:
        if task["id"] > 0:
            if task["status"] == "in progress":
                print(task["description"])

def listToDo():
    print("List of tasks yet to be done:\n")
    for task in taskList:
        if task["id"] > 0:
            if task["status"] == "todo":
                print(task["description"])

if __name__ == "__main__":
    try:
        args = sys.argv
        # args[0] = current file
        # args[1] = function name
        # args[2:] = function args : (*unpacked)
        globals()[args[1]](*args[2:])
    except:
        print("User input error. Please check your arguments and try again.")