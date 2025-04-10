all_tasks_file = open("all_tasks.txt", "r")
all_tasks = [i for i in all_tasks_file.readlines() if i]
completed_tasks_file = open("completed.txt", "r")
completed_tasks = [i for i in completed_tasks_file.readlines() if i]
print(all_tasks)


def main():
    print("Welcome to my to-do list app")
    running = True
    show_tasks()
    while running:
        running = start_app()
        print("-" * 35)
        all_tasks_file = open("all_tasks.txt", "w")
        all_tasks_file.writelines(all_tasks)

        completed_tasks_file = open("completed.txt", "w")
        completed_tasks_file.writelines(completed_tasks)

    all_tasks_file.close()
    completed_tasks_file.close()


def start_app():
    print(
        """What you want to do?
    1. Add a task
    2. Mark as completed
    3. Delete a task
    4. Show current tasks
    5. Quit"""
    )
    choice = valid_choice(
        "Enter choice number (only numbers allowed)",
        "Please enter valid choice number.",
    )
    actions = {
        1: add_task,
        2: mark_completed if all_tasks else show_tasks,
        3: delete_task if all_tasks else show_tasks,
        4: show_tasks,
        5: quit_app,
    }

    action = actions.get(choice)
    action()

    if choice == 5:
        return 0
    return 1


def valid_choice(prompt, err_msg, all_choices=5):
    while True:
        try:
            choice = int(input(f"{prompt}: "))
            if 0 < choice <= all_choices:
                return choice

            print(err_msg)
        except ValueError:
            print(err_msg)


def add_task():
    global all_tasks
    task = input("Enter task to add: ")
    all_tasks.append(f"{task}\n")
    show_tasks()


def mark_completed():
    global all_tasks
    show_tasks()
    task_choice = valid_choice(
        "Enter task number to mark as completed",
        "Enter a valid task number.",
        len(all_tasks),
    )
    completed_tasks.append(all_tasks[task_choice - 1])
    all_tasks.remove(all_tasks[task_choice - 1])
    show_tasks()


def delete_task():
    global all_tasks
    show_tasks()

    choice = valid_choice(
        "Enter the task number to delete (numbers only)",
        "Please enter a valid task number.",
    )
    all_tasks.remove(all_tasks[choice - 1])
    show_tasks()


def show_tasks():
    if all_tasks:
        print("=" * 25)
        for n, task in enumerate(all_tasks, 1):
            print(f"{n}. {task.replace("\n","")}")
        print("=" * 25)
    else:
        print("## Your current to-do list is empty. ##")


def quit_app():
    print("Thanks for using this app")
    show_tasks()


main()
