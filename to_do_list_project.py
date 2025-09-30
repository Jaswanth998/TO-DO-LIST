# ----------------- TO-DO LIST PROJECT -----------------

class TodoList:
    def __init__(self):
        self.tasks = []  # Stores tasks as dictionaries {"task": task_name, "completed": bool}

    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "completed": False})
        print(f"✅ Task '{task}' added successfully!")

    def remove_task(self, task):
        """Remove a task from the list"""
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"🗑 Task '{task}' removed successfully!")
                return
        print(f"⚠ Task '{task}' not found in the list.")

    def mark_completed(self, task):
        """Mark a task as completed"""
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f"✔ Task '{task}' marked as completed!")
                return
        print(f"⚠ Task '{task}' not found in the list.")

    def display_tasks(self):
        """Display all tasks with their status"""
        if self.tasks:
            print("\nYour Tasks:")
            print("-" * 40)
            for i, t in enumerate(self.tasks, start=1):
                status = "✅ Completed" if t["completed"] else "⏳ Not Completed"
                print(f"{i}. {t['task']} - {status}")
            print("-" * 40)
        else:
            print("📭 No tasks in your list.")


# ----------------- MAIN PROGRAM -----------------
def main():
    todo_list = TodoList()
    
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_completed(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("👋 Exiting To-Do List. Have a productive day!")
            break
        else:
            print("⚠ Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()