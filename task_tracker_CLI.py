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

    if command == "add":
        if len(sys.argv) < 3:
            print(f"Please enter a task description")
        else:
            description = sys.argv[2]
            print(f"Adding Task: {description}")
            tasks = load_tasks()
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
        tasks = load_tasks()
        for task in tasks:
            print(task["description"])
            

           
        

            


if __name__ == "__main__":
    main()

