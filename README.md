Command Line based task tracker

This is a small starter project from https://roadmap.sh/projects/task-tracker to build a task tracker.

The python script will take command line arguments to create, add to or update a JSON file to keep track of tasks.

Command line instructions (slightly different from task instructions):

Add a Task:

# Adding a new task
py tasktracker.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
py tasktracker.py update 1 "Buy groceries and cook dinner"
py tasktracker.py delete 1

# Marking a task as in progress or done
py tasktracker.py markInProgress 1
py tasktracker.py markDone 1

# Listing all tasks
py tasktracker.py list

# Listing tasks by status
py tasktracker.py list done
py tasktracker.py list todo
py tasktracker.py list in-progress

This is the first script I've ever written to run from the command line. Have dipped my toe into programmimg, solving endless puzzles and 
it's been cool to actually get my head around something that actually works rather than solving maths or string problems!
