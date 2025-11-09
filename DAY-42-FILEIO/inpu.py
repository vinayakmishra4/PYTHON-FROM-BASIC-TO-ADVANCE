FILENAME='sample.txt'

"""
A simple Python script demonstrating file input/output (I/O) operations:
- Create a file and write initial content
- Append new content to the existing file
- Read and display file content
- Additional methods for line reading, counting, and clearing
"""

def create_file():
    with open(FILENAME, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
        file.write("File I/O operations in Python are fun!\n")

def update_file():
    with open(FILENAME, 'a') as file:
        file.write("Appending a new line to the file.\n")

def read_file():
    with open(FILENAME, 'r') as file:
        content = file.read()
        print(content)

def read_lines():
    """Reads the file line by line and prints each line."""
    with open(FILENAME, 'r') as file:
        for line in file:
            print(line.strip())

def count_lines():
    """Counts and prints the total number of lines in the file."""
    with open(FILENAME, 'r') as file:
        lines = file.readlines()
        print(f"Total lines: {len(lines)}")

def delete_file_content():
    """Clears all content from the file without deleting the file itself."""
    with open(FILENAME, 'w') as file:
        file.truncate(0)
    print("File content deleted successfully.")

while True:
    print("1. Create File")
    print("2. Update File")
    print("3. Read File")
    print("4. Read Lines")
    print("5. Count Lines")
    print("6. Delete File Content")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        create_file()
        print("File created successfully.")
    elif choice == '2':
        update_file()
        print("File updated successfully.")
    elif choice == '3':
        print("File content:")
        read_file()
    elif choice == '4':
        print("Reading file line by line:")
        read_lines()
    elif choice == '5':
        count_lines()
    elif choice == '6':
        delete_file_content()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")