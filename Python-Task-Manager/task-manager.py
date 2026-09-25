#---------------------------------------
#Python Task Manager
#---------------------------------------

#List of required operations:
# 1. Viewing all tasks
# 2. Viewing tasks with a particular status (or priority)
# 3. Adding a task
# 4. Editing an existing task
# 5. Changing the status of a task
# 6. Removing a task
# 7. Data summary of all tasks (AKA stats)
# 8. Exit

#Other requirements:
# - Needs persistence (JSON file)
# - Should handle invalid user input 
# - Should have a way to handle the first run of the program
# - Should handle "ugly" JSON
# - Should handle duplicate task names
# - Each task needs the following:
#   - name
#   - description
#   - priority
#   - completion status


#---------------------------------------
#Imports
#---------------------------------------

from pathlib import Path
import os
import json
import textwrap
import sys
#---------------------------------------
#Functions
#---------------------------------------

def block(words): # For making nice-looking headers
    words = str(words)
    if len(words) > 40:
        wrapped_words = textwrap.fill(words, width=40)

        print("-" * 40)
        print(wrapped_words)
        print("-" * 40)
    else:
        length = len(words)
        padding_amount = 15
        padding = length + padding_amount
        dash_line_length = length + (padding_amount*2)
        print("-" * dash_line_length)
        print(words.rjust(padding, " "))
        print("-" * dash_line_length)

def validMenuInput(thing, a: int, b: int): # Just validates if something is an int and if so if it's within the range set
    try:
        thing = int(thing)
        if thing < a or thing > b:
            return False
        else:
            return True
    except ValueError:
        return False

def menuSelect(inputMessage, x: int, y: int): # If it's valid then an integer version of thing is returned. Keeps looping until True
    # inputMessage is the message to display when prompting input
    # x is the minimum number for the range of "options" the user can select from (for example 1 if it's 1-8)
    # y is the maximum number for the range of "options" the user can select from (for example 8 if it's 1-8)
    while True:
        thing = input(inputMessage)
        if validMenuInput(thing, x, y) == True:
            thing = int(thing)
            return thing
        else:
            print(f"Error: Invalid input. Please enter a number between {x} and {y}")
            continue

def printMenu(): # Just prints the list of options
    block("TASK MANAGER")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Edit a task")
    print("4. Remove a task")
    print("5. See statistics")
    print("6. Exit")

def viewTasks(data: dict): # Creates a nice little table for tasks
    nameLen = 0
    nameLens = []
    descLen = 0
    descLens = []
    priorLen = 0
    priorLens = []
    statLen = 0
    statLens = []
#---------------------------------
    for i in data.keys():
        nameLens.append(len(i))
    try:
        nameLen = max(nameLens)
        if nameLen > 40:
            nameLen = 40
    except ValueError:
        nameLen = len("Names")
    if nameLen < len("Names"):
        nameLen = len("Names")
#---------------------------------
    for i in data.keys():
        descLens.append(len(data[i]["description"]))
    try:
        descLen = max(descLens)
        if descLen > 40:
            descLen = 40
    except ValueError:
        descLen = len("Description")
    if descLen < len("Description"):
        descLen = len("Description")
#---------------------------------
    for i in data.keys():
        priorLens.append(len(data[i]["priority"]))
    try:
        priorLen = max(priorLens)
        if priorLen > 40:
            priorLen = 40
    except ValueError:
        priorLen = len("Priority")
    if priorLen < len("Priority"):
        priorLen = len("Priority")
#---------------------------------
    for i in data.keys():
        statLens.append(len(data[i]["status"]))
    try:
        statLen = max(statLens)
        if statLen > 40:
            statLen = 40
    except ValueError:
        statLen = len("Status")
    if statLen < len("Status"):
        statLen = len("Status")
#---------------------------------
    print(f"{'Names':^{nameLen}} | {'Description':^{descLen}} | {'Priority':^{priorLen}} | {'Status':^{statLen}}")
    lineLen = len(f"{'Names':^{nameLen}} | {'Description':^{descLen}} | {'Priority':^{priorLen}} | {'Status':^{statLen}}")
    print("-"*lineLen)

    for n in data.keys():
    
        nameWrap = textwrap.wrap(n, nameLen)
        #nameLen = tableLength
        descWrap = textwrap.wrap(data[n]["description"], descLen)
        #descLen = tableLength
        priorWrap = textwrap.wrap(data[n]["priority"], priorLen)
        #priorLen = tableLength
        statWrap = textwrap.wrap(data[n]["status"], statLen)
        #statLen = tableLength

        lens = []
        lens.append(len(nameWrap))
        lens.append(len(descWrap))
        lens.append(len(priorWrap))
        lens.append(len(statWrap))

        # print(lens)
        maxLen = max(lens)
        # print(maxLen)

        if len(nameWrap) < maxLen:
            addRows = maxLen - len(nameWrap)
            for i in range(addRows):
                nameWrap.append("")
                # print(nameWrap)

        if len(descWrap) < maxLen:
            addRows = maxLen - len(descWrap)
            for i in range(addRows):
                descWrap.append("")
                # print(descWrap)


        if len(priorWrap) < maxLen:
            addRows = maxLen - len(priorWrap)
            for i in range(addRows):
                priorWrap.append("")
                # print(priorWrap)


        if len(statWrap) < maxLen:
            addRows = maxLen - len(statWrap)
            for i in range(addRows):
                statWrap.append("")
                # print(statWrap)
        
        lineLen = len(f"{'Names':^{nameLen}} | {'Description':^{descLen}} | {'Priority':^{priorLen}} | {'Status':^{statLen}}")
        for i in range(maxLen):
            print(f"{nameWrap[i]:^{nameLen}} | {descWrap[i]:^{descLen}} | {priorWrap[i]:^{priorLen}} | {statWrap[i]:^{statLen}}")
        
        print("-"*lineLen)

#------------------------------------------------------------------------------
#filterTasks Description:
# # Takes a dictionary, a 'type' (In this case priority or status)
# and a filter (In this case, any of the values that correspond to the 'type')
# and then runs through the keys matching those arguments and puts them in a temporary dictionary
# before printing the temporary dictionary
def filterTasks(data: dict, type, filter): 
    tempDict = {}
    for i in data.keys():
        if data[i][type] == filter:
            tempDict[i] = data[i]
        else:
            continue
    if tempDict == {}:
        print(f"No matches for a task with {type} '{filter}'")
    else:
        viewTasks(tempDict)


def isKeyInDict(data: dict, thing): # Just checks if a key is present in a dictionary
    if thing in data:
        return True
    else:
        return False


def statistics():

    if tasks == {}:
        print("There are no tasks")
    else:
        #Status counters
        ns = 0
        ip = 0
        c = 0
        for i in tasks.keys():
            if tasks[i]["status"] == "not started":
                ns += 1
            elif tasks[i]["status"] == "in progress":
                ip += 1
            else:
                c += 1
        #Priority counters
        l = 0
        m = 0
        h = 0
        for i in tasks.keys():
            if tasks[i]["priority"] == "low":
                l += 1
            elif tasks[i]["priority"] == "medium":
                m += 1
            else:
                h += 1


        #Counters:
        #Total Tasks
        block("TOTAL")
        print(f"Total tasks: {len(tasks)}")
        #Counts by status/priority
        block("STATUS")
        print(f"Tasks not started: {ns}")
        print(f"Tasks in progress: {ip}")
        print(f"Tasks complete: {c}")
        block("PRIORITY")
        print(f"Number of low priority tasks: {l}")
        print(f"Number of medium priority tasks: {m}")
        print(f"Number of high priority tasks: {h}")
        #completion percentage
        comp = (c / len(tasks)) * 100
        block("COMPLETION")
        print(f"Percentage of tasks completed: {comp}%")

#---------------------------------------
#-------------Main program--------------
#---------------------------------------



#----------------------
#task body rough draft
#----------------------


# tasks = {
#     "task_name-1":{ <----- Task name would be the name of the dictionary for that task
#         "description": "Description placed here", <----- description will simply be a string given by the user
#         "priority": "Low", <----- Priority could either be string-based or integer based (perhaps 1-5 or 1-10?)
#         "status": "Complete" <----- Status will just be simple not started, in progress, and complete
#     }
# }


#------------------------------
#Test Dictionary
#------------------------------

# tasks = {
#     "task1":{
#         "description":"writing 67 a bunch",
#         "priority":"high",
#         "status":"not started"
#     },
#     "task2":{
#             "description":"writing 69 a bunch",
#             "priority":"medium",
#             "status":"in progress"
#     },
#     "task3":{
#             "description":"writing 21 a bunch",
#             "priority":"low",
#             "status":"complete"
#     }
# }










#------------------------------------
#Checking JSON file
#------------------------------------
json_file = Path(os.getcwd()) / "Python-Task-Manager" / "task-manager.json" # Since this is just for practice and me, I'm partially hardcoding the path to the json file



if json_file.exists() == False: # if the json file doesn't exist, we create it and write an empty dictionary to it
    tasks = {}
    with open(json_file, "w") as file:
        json.dump(tasks, file, indent=4)
    block("Welcome to the Python Task Manager. It seems like this is your first time using this program as there is no saved data.")
else: # if the json file does exist, we load in the json from the file into our tasks variable (which is our main dictionary)
    try:
        with open(json_file, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError: # If "corrupt" then we give the user the option to leave and fix it or wipe the file
        print("Error: There was an issue loading the data from the JSON file. It may be corrupt.")
        print("\nPlease close this program and fix it. Otherwise the file will be overwritten to be empty if you continue")
        while True:
            choice = input("\nClose this program? (y/n): ").lower().strip()
            if choice == "y":
                sys.exit()
            elif choice == "n":
                tasks = {}
                with open(json_file, "w") as file:
                    json.dump(tasks, file, indent=4)
                break
            else:
                print("Error: Please input 'y' or 'n'")


if isinstance(tasks, dict) == False:
    print("ERROR: tasks is not a dictionary. Please fix your JSON file")
    sys.exit()

# Proper value detection
if tasks != {}:
    for i in tasks.keys():
        if not isinstance(tasks[i], dict):
            print(f"ERROR: task '{i}' is not a dictionary. Please fix your JSON file")
            sys.exit()
        # if "description" in tasks[i].keys():
        #     print("description present")
        if "description" not in tasks[i].keys():
            print(f"ERROR: task '{i}' is missing a description. Please fix your JSON file")
            sys.exit()
        if not isinstance(tasks[i]["description"], str):
            print(f"ERROR: task '{i}' doesn't have a description with a string value. Please fix your JSON")
            sys.exit()
        if "status" not in tasks[i].keys():
            print(f"ERROR: task '{i}' is missing a status. Please fix your JSON file")
            sys.exit()
        if "priority" in tasks[i].keys():
            if not isinstance(tasks[i]["priority"], str):
                print(f"ERROR: task '{i}' doesn't have a priority with a string value. Please fix your JSON")
                sys.exit()
            if tasks[i]["priority"] != "low" and tasks[i]["priority"] != "medium" and tasks[i]["priority"] != "high":
                print(f"ERROR: task '{i}' has invalid priority '{tasks[i]["priority"]}'. Please fix your JSON file")
                sys.exit()
        if "priority" not in tasks[i].keys():
            print(f"ERROR: task '{i}' is missing a priority. Please fix your JSON file")
            sys.exit()
        if "status" in tasks[i].keys():
            if not isinstance(tasks[i]["status"], str):
                print(f"ERROR: task '{i}' doesn't have a status with a string value. Please fix your JSON")
                sys.exit()
            if tasks[i]["status"] != "not started" and tasks[i]["status"] != "in progress" and tasks[i]["status"] != "complete":
                print(f"ERROR: task '{i}' has invalid status '{tasks[i]["status"]}'. Please fix your JSON file")
                sys.exit()
        if len(tasks[i].keys()) > 3 and (tasks[i] != "description" and tasks[i] != "status" and tasks[i] != "priority"):
            print(f"Error: task '{i}' has a foreign key. Please fix your JSON file")
            sys.exit()



#--------
#Menu
#--------
while True:
    printMenu()
    choice = menuSelect("Select an operation to perform (1-6): ", 1, 6)
    if choice == 1: # View tasks --------------------------------------------------------------------------------
        if tasks == {}:
            block("There are no tasks to display.")
        else:
            while True:
                print("1. View all tasks")
                print("2. Filter by priority")
                print("3. Filter by status")
                print("4. Return to main menu")
                subChoice = input("How would you like to view your tasks: ")
                if validMenuInput(subChoice, 1, 4) == True:
                    subChoice = int(subChoice)
                    if subChoice == 1:
                        viewTasks(tasks)
                    elif subChoice == 2:
                        while True:
                            print("1. low")
                            print("2. medium")
                            print("3. high")
                            print("4. Return to view menu")
                            subChoice = input("What priority do you want to filter by: ")
                            if validMenuInput(subChoice, 1, 4) == True:
                                subChoice = int(subChoice)
                                if subChoice == 1:
                                    filterTasks(tasks, "priority", "low")
                                elif subChoice == 2:
                                    filterTasks(tasks, "priority", "medium")
                                elif subChoice == 3:
                                    filterTasks(tasks, "priority", "high")
                                elif subChoice == 4:
                                    break
                    elif subChoice == 3:
                        while True:
                            print("1. not started")
                            print("2. in progress")
                            print("3. complete")
                            print("4. Return to view menu")
                            subChoice = input("What status do you want to filter by: ")
                            if validMenuInput(subChoice, 1, 4) == True:
                                subChoice = int(subChoice)
                                if subChoice == 1:
                                    filterTasks(tasks, "status", "not started")
                                elif subChoice == 2:
                                    filterTasks(tasks, "status", "in progress")
                                elif subChoice == 3:
                                    filterTasks(tasks, "status", "complete")
                                elif subChoice == 4:
                                    break
                    elif subChoice == 4:
                        break
                else:
                    print("Error: Invalid input. Please enter a number corresponding to your menu choice")
                continue
    elif choice == 2: # Add a task --------------------------------------------------------------------------------
        while True:
            nameOTask = str(input("Input the name of the task: ")).lower().strip()
            if isKeyInDict(tasks, nameOTask) == True:
                print(f"Error: A task named '{nameOTask}' already exists. Please choose a different name")
            else:
                break
        descOTask = str(input("Input a description of the task: "))
        while True:
            priorOTask = str(input("Input the priority of the task (high, medium, low): ").lower().strip())
            if priorOTask != "high" and priorOTask != "medium" and priorOTask != "low":
                print("Error: Not a valid priority.")
            else:
                break
        while True:
            statOTask = str(input("Input the status of the task (not started, in progress, complete): ").lower().strip())
            if statOTask != "not started" and statOTask != "in progress" and statOTask != "complete":
                print("Error: Not a valid status. Please check your spelling and try again")
            else:
                break
        tasks[nameOTask] = {"description": descOTask, "priority": priorOTask, "status": statOTask}
        print(f"Task '{nameOTask}' was added to tasks")
        #---------------
        # Saving
        #---------------
        with open(json_file, "w") as file:
            json.dump(tasks, file, indent=4)
    elif choice == 3: # Edit a task --------------------------------------------------------------------------------
        if tasks == {}:
            block("There are no tasks to edit.")
        else:
            while True:
                print("1. Edit the name of a task")
                print("2. Edit the description of a task")
                print("3. Edit the status of a task")
                print("4. Edit the priority of a task")
                print("5. Exit to main menu")
                subChoice = input("What would you like to edit: ")
                if validMenuInput(subChoice, 1, 5) == True:
                    subChoice = int(subChoice)
                    if subChoice == 1:
                        viewTasks(tasks)
                        while True:
                            taskToEdit = input("Input the current name of the task: ").lower().strip()
                            if isKeyInDict(tasks, taskToEdit) == True:
                                while True:
                                    newName = input(f"Enter the new name of '{taskToEdit}': ").lower().strip()
                                    if newName == taskToEdit:
                                        print("Error: Please input a new name for the task, not the existing name")
                                    elif isKeyInDict(tasks, newName) == True:
                                        print("Error: A task with that name already exists. Please enter a completely new name")
                                    else:
                                        tasks[newName] = tasks.pop(taskToEdit)
                                        print(f"Name of '{taskToEdit}' was changed to '{newName}' successfully")
                                        #---------------
                                        # Saving
                                        #---------------
                                        with open(json_file, "w") as file:
                                            json.dump(tasks, file, indent=4)
                                        break
                            else:
                                print("Error: A task of that name does not exist")
                    elif subChoice == 2:
                        viewTasks(tasks)
                        while True:
                            taskToEdit = input("Input the name of the task you'd like to edit: ").lower().strip()
                            if isKeyInDict(tasks, taskToEdit) == True:
                                while True:
                                    newDesc = input(f"Enter the new description for '{taskToEdit}': ")
                                    if newDesc == "":
                                        print("Error: Description must contain text, cannot be empty")
                                        continue
                                    elif newDesc == tasks[taskToEdit]["description"]:
                                        print("Error: Please enter a new description")
                                    else:
                                        tasks[taskToEdit]["description"] = newDesc
                                        #---------------
                                        # Saving
                                        #---------------
                                        with open(json_file, "w") as file:
                                            json.dump(tasks, file, indent=4)
                                        break
                            else:
                                print("Error: A task of that name does not exist")
                    elif subChoice == 3:
                        viewTasks(tasks)
                        while True:
                            taskToEdit = input("Input the name of the task you'd like to edit: ").lower().strip()
                            if isKeyInDict(tasks, taskToEdit) == True:
                                while True:
                                    newStat = input(f"Enter the new status for '{taskToEdit}': ").lower().strip()
                                    if newStat != "not started" and newStat != "in progress" and newStat != "complete":
                                        print("Error: Please input 'not started', 'in progress', or 'complete'")
                                    elif newStat == tasks[taskToEdit]["status"]:
                                        print("Error: Please enter a new status")
                                    else:
                                        tasks[taskToEdit]["status"] = newStat
                                        #---------------
                                        # Saving
                                        #---------------
                                        with open(json_file, "w") as file:
                                            json.dump(tasks, file, indent=4)
                                        break
                            else:
                                print("Error: A task of that name does not exist")
                    elif subChoice == 4:
                        viewTasks(tasks)
                        while True:
                            taskToEdit = input("Input the name of the task you'd like to edit: ").lower().strip()
                            if isKeyInDict(tasks, taskToEdit) == True:
                                while True:
                                    newPrior = input(f"Enter the new priority for '{taskToEdit}': ").lower().strip()
                                    if newPrior != "low" and newPrior != "medium" and newPrior != "high":
                                        print("Error: Please input 'low', 'medium', or 'high'")
                                    elif newPrior == tasks[taskToEdit]["priority"]:
                                        print("Error: Please enter a new priority")
                                    else:
                                        tasks[taskToEdit]["priority"] = newPrior
                                        #---------------
                                        # Saving
                                        #---------------
                                        with open(json_file, "w") as file:
                                            json.dump(tasks, file, indent=4)
                                        break
                            else:
                                print("Error: A task of that name does not exist")
                    elif subChoice == 5:
                        break
                else:
                    print("Error: Invalid input. Please enter a number corresponding to your menu choice")
                continue
    elif choice == 4: # Remove a task --------------------------------------------------------------------------------
        if tasks == {}:
            print("Error: There are no tasks to delete")
        else:
            viewTasks(tasks)
            while True:
                nameOTask = str(input("What task do you want to delete: ").lower().strip())
                if isKeyInDict(tasks, nameOTask) == False:
                    print("Error: A task of that name does not exist")
                else:
                    break
            while True:
                confirm = str(input(f"Are you sure you want to delete '{nameOTask}' from tasks? (y/n): ").lower().strip())
                if confirm == "y":
                    del tasks[nameOTask]
                    print(f"'{nameOTask}' was successfully deleted from tasks")
                    #---------------
                    # Saving
                    #---------------
                    with open(json_file, "w") as file:
                        json.dump(tasks, file, indent=4)
                    break
                elif confirm == "n":
                    break
                else:
                    print("Error: Please input 'y' or 'n'")
    elif choice == 5: # See statistics --------------------------------------------------------------------------------
        statistics()
    elif choice == 6: # Exit --------------------------------------------------------------------------------
        sys.exit()

