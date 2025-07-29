#TASK TRACKER PROJECT
import sys
import json
import os
from datetime import datetime

def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return []


def main():
    print("You ran the task CLI!")
    print("Arguments received:", sys.argv)
    if len(sys.argv) < 2:
        print(input("Enter a a command i.e. (add, list, delete): "))
        return

    command = sys.argv[1]

    tasks = load_tasks()

    if command == "add":
        if len(sys.argv) < 3:
            print(f"Please enter a task description")
        else:
            description = sys.argv[2]
            print(f"Adding Task: {description}")
            new_task = {
                "id": len(tasks) + 1,
                "description": description,
                "status": "todo",
                "createdAt": datetime.now().isoformat(),
                "updatedAt": datetime.now().isoformat()
            }

            tasks.append(new_task)

            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent=2)

            print("Task saved!")
    elif command == "list":
        if len(sys.argv) > 2:
            desired_status = sys.argv[2]
            for task in tasks:
                if task['status'] == desired_status:
                    print(f"The task '{task['description']}' has the status {task['status']}")
        else:
            for task in tasks:
                print(f"Task '{task['description']}' has id {task['id']}")
        
    elif command == "mark-done":
        try:    
            task_id = int(sys.argv[2])
        except (ValueError, IndexError):
            print("Please provide a valid numeric task ID to update the status.")
            return
        
        for item in tasks:
            if task_id == item['id']:
                item['status'] = "done"
                item['updatedAt'] = datetime.now().isoformat()
                print(f"Status of a task with id {item['id']} has been updated")
                with open("tasks.json", "w") as f:
                    json.dump(tasks, f, indent=2)
                    break
            else:
                print(f"Task with id {task_id} does not exist.")

    elif command == "mark-in-progress":
        try:    
            task_id = int(sys.argv[2])
        except (ValueError, IndexError):
            print("Please provide a valid numeric task ID to update the status.")
            return
        
        for item in tasks:
            if task_id == item['id']:
                item['status'] = "in-progress"
                item['updatedAt'] = datetime.now().isoformat()
                print(f"Status of a task with id {item['id']} has been updated")
                with open("tasks.json", "w") as f:
                    json.dump(tasks, f, indent=2) 
                    break
            else:
                print(f"Task with id {task_id} does not exist.")

    elif command == "update":
        try:
            task_id = int(sys.argv[2])
        except(ValueError,IndexError):
            print("Please provide a valid numeric task ID to update.")
            return
        
        for item in tasks:
            if task_id == item['id']:
                item['description'] = input("Please Enter a new descrpition: ") 
                item['updatedAt'] = datetime.now().isoformat()  
                print(f"Task with id {item['id']} has been updated")
                with open("tasks.json", "w") as f:
                    json.dump(tasks, f, indent=2) 
                    break
            else:
                print(f"Task with id {task_id} does not exist.")
                    
    
    elif command == "delete":
        try:
            task_id = int(sys.argv[2])
        except (ValueError,IndexError):
            print("Please provide a valid numeric task ID to delete.")
            return
         
        for item in tasks:
            if task_id == item['id']:
                tasks.remove(item) 
                print(f"Task with id {item['id']} has been deleted")
                with open("tasks.json", "w") as f:
                    json.dump(tasks, f, indent=2)
                    break
            else:
                print(f"Task with id {task_id} does not exist.")
                 
if __name__ == "__main__":
    main()
    

