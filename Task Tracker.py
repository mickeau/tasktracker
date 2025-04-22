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


TaskCounter = 1
# Open and read the JSON file
# TODO: add TaskCounter variable to JSON file
if os.path.exists('tasktracker.json'):
    with open('tasktracker.json', 'r') as file:
        taskList = json.load(file)
        TaskCounter = taskList[0]["taskCounter"]
        print("After opening JSON, the Task Counter is at ", TaskCounter)
        
else:
    taskList = []
    taskList.append(dict(taskCounter = 1))

#Convert timestamp to readable date and time format
def timeConvert(timestr):
    time = timestr.strftime("%A, %d %B %Y %I:%M %p")
    return time

now = timeConvert(datetime.datetime.now())

#function to add new tasks to list
def add():
    global TaskCounter
    newItem = {
        "id": str(TaskCounter),
        "description": input("Enter task description: "),
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,

    }
    TaskCounter += 1
    print("After addTask function, the Task Counter is at ", TaskCounter)
    return newItem

# Create loop to add as many tasks as necessary
TaskAdd = True
while TaskAdd == True:
    response = input("Would you like to add another task? ")
    if response == "Y" or response == "y" or response == "Yes" or response == "yes":
        newTask = add()
        taskList.append(newTask)
    elif response == "N" or response == "n" or response == "No" or response == "no":
        print("After breaking TaskAdd loop, the Task Counter is at ", TaskCounter)
        taskList[0]["taskCounter"] = TaskCounter
        TaskAdd = False
    else:
        continue

# Update dictionary in the dictionary of dictionaries


# Serializing json
json_object = json.dumps(taskList, indent=4)
 
# Writing to sample.json
with open("tasktracker.json", "w") as outfile:
    outfile.write(json_object)

print(taskList)
print(TaskCounter)