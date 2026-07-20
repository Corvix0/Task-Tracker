print("Hello")
import json
import os

JSON_FILE = "data.json"

with open(JSON_FILE, 'r') as f:
    data = json.load(f)

def get_next_id():
    if not data["Tasks"]:
        return 0
    return max(task["Task_ID"] for task in data["Tasks"]) + 1

def add_task():
    
    task_name = input("Enter task description: ")
    task_progress = input("Enter current task progress: ")

    new_task = {
        "Task_ID" : get_next_id(),
        "Task_name" : task_name,
        "Task_progress" : task_progress 
    }

    data["Tasks"].append(new_task)
    
    save_data()
#add_task()

def remove_task():
    try:
        
        target = int(input("Enter task ID for deleting: "))
        for i,task in enumerate(data["Tasks"]):
            print(i,task)
            if task["Task_ID"] == target:
                del data["Tasks"][i]
                save_data()
                return
            
    except ValueError:
        print("Enter a valid number")



def update_task():
    try:
        target = int(input("Enter task ID for update: "))
        for task in data["Tasks"]:
            if task["Task_ID"] == target:
                new_name = input("Enter update: ").strip()
                if new_name:
                    task["Task_name"] = new_name
                save_data()
                return
        print("Task ID not found")
    except ValueError:
        print("Enter valid number")
#update_task()
def show_tasks():
    for task in data["Tasks"]:
        #print(task)
        print(f"{task['Task_ID']} {task['Task_name']:<20}  {task['Task_progress']}")
#show_tasks()

def save_data():
    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    

while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Update task")    
    print("4. Show all tasks")
    print("0. Exit")
    op = int(input("Select operation from list: "))
    if op == 0:
       save_data()
       break
    elif op == 1:
        add_task()
    elif op == 2:
        remove_task()
    elif op == 3:
        update_task()
    elif op == 4:
        
        show_tasks()
    else:
        print("invalid input")