def add_task(task_list, task):
    task_list.append(task)
    print(f"Added task: {task}")
    

def delete_task(task_list):
    if not task_list:
        print("No tasks to delete.")
        return

    print("Tasks to delete:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

    try:
        task_number = int(input("Enter the number of the task you want to delete: "))
        if 1 <= task_number <= len(task_list):
            deleted_task = task_list.pop(task_number - 1)
            print(f'Deleted task: "{deleted_task}"')
        else:
            print("Invalid task number.\nplease try again")
    except ValueError:
        print("Please enter a valid number.")

def display_tasks(task_list):
    if  task_list==[]:
        print("No tasks to display.")
    else:
        print("Tasks to do:")
        for task in task_list:
            print(f"--> {task}")

def mark_complete(task_list, task):
    if task_list:
        print("Tasks to Mark:")
        for index, t in enumerate(task_list, start=1):
            print(f"{index}. {t}")

        try:
            task_number = int(input("Enter the number of the task you want to Mark: "))
            
            if 1 <= task_number <= len(task_list):
                marked_task = task_list[task_number - 1]
                task_list.remove(marked_task)
                print(f"'{marked_task}' - the Task Marked as completed.")
            else:
                print("Invalid task number. Please try again")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Task list is empty.")


def task_management():
    task_list = []
    print("*****TO-DO LIST APPLICATION*****")
    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. Display tasks")
        print("4. Mark task as complete")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        

            if choice == 1:
                task = input("Enter task to-do: ")
                add_task(task_list, task)

            elif choice == 2:
                delete_task(task_list)

            elif choice == 3:
                display_tasks(task_list)

            elif choice == 4:
                mark_complete(task_list, task)

            elif choice == 5:
                print("exited successfully!")
                break
        except ValueError:
            print("Invalid choice. Please enter a number.")
        print("- "*30)   

task_management()