class ToDoList:
    def __init__(self):
        # Initialize an empty dictionary to store tasks
        self.tasks = {}  # Dictionary: Task ID as key, details as values.
        # Define a set containing unique task statuses
        self.task_statuses = {"Incomplete", "Complete"}  # Set of unique statuses.
    
    def add_task(self):
        # Get task details from user input
        task_name = input("Enter the task: ")
        task_priority = input("Enter the task priority (Low/Medium/High): ")
        # Store task details in a tuple
        task_details = (task_name, task_priority, "Incomplete")
        # Generate a unique task ID
        task_id = len(self.tasks) + 1
        # Store the task in the dictionary
        self.tasks[task_id] = task_details
        print(f"Task '{task_name}' with priority '{task_priority}' added.")
    
    def display_tasks(self):
        # Check if the task list is empty
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Your To-Do List:")
            # Iterate through tasks and display details
            for task_id, task_info in self.tasks.items():  # self.tasks.items() returns key-value pairs (task ID and task details).
                task_name, task_priority, task_status = task_info
                print(f"{task_id}. {task_name} (Priority: {task_priority}, Status: {task_status})")
    
    def mark_complete(self):
        try:
            # Get task ID from user
            task_id = int(input("Enter the task ID to mark as complete: "))
            if task_id in self.tasks:
                # Update task status to 'Complete'
                task_name, task_priority, _ = self.tasks[task_id]
                self.tasks[task_id] = (task_name, task_priority, "Complete")
                print(f"Task '{task_name}' marked as complete.")
            else:
                print("Task ID not found.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    def update_task(self):
        try:
            # Get task ID from user
            task_id = int(input("Enter the task ID to update: "))
            if task_id in self.tasks:
                task_name, task_priority, task_status = self.tasks[task_id]

                # Get new details
                new_task_name = input(f"Enter new task name (or press Enter to keep '{task_name}'): ").strip()
                new_priority = input(f"Enter new priority (Low/Medium/High, or press Enter to keep '{task_priority}'): ").strip()

                # Keep old values if user doesn't enter anything
                task_name = new_task_name if new_task_name else task_name
                task_priority = new_priority if new_priority else task_priority

                # Update task details
                self.tasks[task_id] = (task_name, task_priority, task_status)
                print(f"Task {task_id} updated successfully!")
            else:
                print("Task ID not found.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    def remove_task(self):
        try:
            # Get task ID from user
            task_id = int(input("Enter the task ID to remove: "))
            if task_id in self.tasks:
                # Remove the specified task
                removed_task = self.tasks.pop(task_id)
                print(f"Task '{removed_task[0]}' removed.")
            else:
                print("Task ID not found.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    def clear_all_tasks(self):
        # Ask for user confirmation before clearing all tasks
        confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()
        if confirm == "yes":
            self.tasks.clear()
            print("All tasks have been deleted.")
        else:
            print("Operation canceled.")
    
    def display_statuses(self):
        # Display all unique statuses from the set
        print("Unique Task Statuses:")
        for status in self.task_statuses:
            print(status)
    
    def main_menu(self):
        # Main loop to interact with the user
        while True:
            print("\nTo-Do List Menu")
            print("1. Add Task")
            print("2. Display Tasks")
            print("3. Mark Task as Complete")
            print("4. Update Task")  # New option added here
            print("5. Remove Task")
            print("6. Delete All Tasks")
            print("7. Display Unique Statuses")
            print("8. Exit")
            
            try:
                # Get user choice and call corresponding method
                choice = int(input("Enter your choice (1-8): "))
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.display_tasks()
                elif choice == 3:
                    self.mark_complete()
                elif choice == 4:
                    self.update_task()  # Calls update function
                elif choice == 5:
                    self.remove_task()
                elif choice == 6:
                    self.clear_all_tasks()
                elif choice == 7:
                    self.display_statuses()
                elif choice == 8:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 8.")
            except ValueError:
                print("Invalid input! Please enter a number.")

# Create an instance of ToDoList and start the program
todo_list = ToDoList()
todo_list.main_menu()
