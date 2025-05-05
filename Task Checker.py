# Define a class to represent a Task
class Tasks:
    def __init__(self, task):
        # Initialize the task with the task description
        self.task = task

    def __str__(self):
        # Define how the task will be displayed as a string
        return f"{self.task}"

# Create an empty list to store all task objects
tasks = []

# Function to display all tasks
def show_tasks():
    if not tasks:
        # If the list is empty, tell the user they have nothing to do
        print("You have nothing to do today!")
        return

    # Enumerate through tasks and display each with its index
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")  # Print task number and task description
        print()  # Blank line for spacing

# Function to add a new task
def add_tasks():
    print("Add a new task")

    # Prompt the user to enter the task description
    task = input("Enter your task description: ").strip()

    # Create a new task object and add it to the task list
    task = Tasks(task)
    tasks.append(task)

    # Confirm to the user that the task was added
    print(f"Task {task} added!\n")

# Function to edit an existing task
def edit_task():
    if not tasks:
        # Inform the user if there are no tasks to edit
        print("You have nothing to edit!")
        return

    # Show the list of tasks to the user
    show_tasks()

    try:
        # Ask user which task to edit (by number)
        choice = int(input("Select the task you wish to edit: "))
        if 1 <= choice <= len(tasks):
            # Get the selected task
            task = tasks[choice - 1]
            print(f"Editing task: {task}")

            # Ask for new task description (press Enter to keep current one)
            new_task = input(f"Enter new task [{task.task}]: ") or task.task
            task.task = new_task  # Update the task

            print("Task updated successfully!\n")
        else:
            # If the chosen number is out of range
            print("Invalid choice, please try again")
    except ValueError:
        # Handle non-numeric input
        print("Invalid input, please type in the number of the task you wish to edit")

# Function to remove a task
def remove_tasks():
    if not tasks:
        # Inform the user if there are no tasks to remove
        print("You have no tasks to do!")
        return

    # Show all current tasks
    show_tasks()

    try:
        # Ask user which task to remove
        choice = int(input("Which task would you like to remove? "))
        if 1 <= choice <= len(tasks):
            # Remove the selected task from the list
            removed = tasks.pop(choice - 1)
            print(f"Removing task: {removed}")
        else:
            # If the chosen number is invalid
            print("Invalid choice, please try again!")
    except ValueError:
        # Handle non-integer input
        print("Invalid input! Please enter the number of the task")

# Main function to control the menu system
def main():
    # Ask for the user's name
    name = input("Please Enter your Name:\n")

    while True:
        # Display the menu and options
        print(f"\nGood Morning {name}! Let's see what you have to do today:")
        print("1. Show Tasks")
        print("2. Add Tasks")
        print("3. Edit Tasks")
        print("4. Remove Tasks")
        print("5. Exit")

        # Get the user's menu choice
        choice = input("\nPlease select an option: ")

        # Match user choice to corresponding function
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            remove_tasks()
        elif choice == '5':
            # Exit the loop and say goodbye
            print("Goodbye!")
            break
        else:
            # Handle invalid menu option
            print("Invalid option, please try again")

# If this file is run directly, call the main function
if __name__ == "__main__":
    main()