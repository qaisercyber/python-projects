from datetime import datetime

tasks = []


# ------------------ Add Task ------------------
def add_task():
    title = input("Enter task title: ").strip()
    deadline_input = input("Enter deadline (YYYY-MM-DD): ").strip()

    try:
        deadline = datetime.strptime(deadline_input, "%Y-%m-%d")
    except ValueError:
        print(" Invalid date format. Use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "deadline": deadline,
        "created_at": datetime.now()
    }

    tasks.append(task)
    print(" Task added successfully.")


# ------------------ View All Tasks ------------------
def view_tasks():
    if not tasks:
        print(" No tasks available.")
        return

    print("\n ALL TASKS")
    print("-" * 40)

    for i, task in enumerate(tasks, start=1):
        deadline_str = task["deadline"].strftime("%Y-%m-%d")
        print(f"{i}. {task['title']} | Deadline: {deadline_str}")


# ------------------ Show Overdue Tasks ------------------
def show_overdue_tasks():
    now = datetime.now()
    overdue_found = False

    print("\n OVERDUE TASKS")
    print("-" * 40)

    for task in tasks:
        if task["deadline"] < now:
            days_overdue = (now - task["deadline"]).days
            print(
                f"{task['title']} | "
                f"Deadline was {task['deadline'].strftime('%Y-%m-%d')} | "
                f"Overdue by {days_overdue} day(s)"
            )
            overdue_found = True

    if not overdue_found:
        print(" No overdue tasks!")


# ------------------ Menu ------------------
def show_menu():
    print("\n TASK DEADLINE REMINDER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Show Overdue Tasks")
    print("4. Exit")


# ------------------ Main Program ------------------
def main():
    while True:
        show_menu()
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            show_overdue_tasks()
        elif choice == "4":
            print(" Exiting Task Reminder.")
            break
        else:
            print(" Invalid choice.")


if __name__ == "__main__":
    main()
