class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        print(f"Task added: {task_id}. {description}")

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task deleted: {task_id}. {task.description}")
        else:
            print("Task not found.")

    def mark_completed(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.completed = True
            print(f"Task marked as completed: {task_id}. {task.description}")
        else:
            print("Task not found.")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for task in self.tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"{task.task_id}. {task.description} - {status}")
        else:
            print("No tasks in the list.")

def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == "2":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            task_manager.mark_completed(task_id)
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
