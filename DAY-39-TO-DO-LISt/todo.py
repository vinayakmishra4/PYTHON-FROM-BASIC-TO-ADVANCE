# Creating To-Do List in Python with colorful output and explanations

# ANSI color codes for colorful terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"  # Reset color to default

# Initialize an empty list to store tasks
todo_list = []

# Function to add a new task
def add_task(task):
    """Adds a new task to the to-do list."""
    todo_list.append(task)
    print(f'{GREEN}Task "{task}" added to the list.{RESET}')

# Function to view all tasks
def view_tasks():
    """Displays all tasks in the to-do list."""
    if not todo_list:
        print(f"{RED}No tasks in the list.{RESET}")
    else:
        print(f"{YELLOW}To-Do List:{RESET}")
        # Enumerate adds numbering starting from 1
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

# Function to remove a specific task by its number
def remove_task(task_number):
    """Removes a task from the to-do list by its index."""
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f'{GREEN}Task "{removed_task}" removed from the list.{RESET}')
    else:
        print(f"{RED}Invalid task number.{RESET}")

# Main function to run the to-do list application
def main():
    """Main loop that presents the user with options."""
    while True:
        # Display the menu header in cyan color
        print(f"\n{CYAN}To-Do List Menu:{RESET}")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        # Ask user to choose an option
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            # Prompt user to enter a new task and add it
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            # Display all current tasks
            view_tasks()
        elif choice == '3':
            # Attempt to remove a task by its number
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                # Handle the case where input is not an integer
                print(f"{RED}Please enter a valid number.{RESET}")
        elif choice == '4':
            # Exit the application with a success message
            print(f"{GREEN}Exiting the To-Do List application.{RESET}")
            break
        else:
            # Handle invalid menu choices
            print(f"{RED}Invalid choice. Please try again.{RESET}")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
