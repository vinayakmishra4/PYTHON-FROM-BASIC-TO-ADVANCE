# 🌟 Python Interactive Demo: Collection & CLI Practice

def show_menu():
    print("\n===== Python Interactive Demo =====")
    print("1. Manage List")
    print("2. Manage Tuple")
    print("3. Dictionary CRUD")
    print("4. Set Operations")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

# --- List Operations ---
def manage_list():
    my_list = []
    while True:
        print("\n-- List Menu --")
        print("a. Add element")
        print("b. Remove element")
        print("c. Show list")
        print("d. Back to main menu")
        opt = input("Choose option: ").lower()
        if opt == 'a':
            elem = input("Enter element to add: ")
            my_list.append(elem)
            print(f"{elem} added!")
        elif opt == 'b':
            elem = input("Enter element to remove: ")
            try:
                my_list.remove(elem)
                print(f"{elem} removed!")
            except ValueError:
                print(f"{elem} not found in the list.")
        elif opt == 'c':
            print(f"Current List: {my_list}")
        elif opt == 'd':
            break
        else:
            print("Invalid option!")

# --- Tuple Operations ---
def manage_tuple():
    t = tuple(input("Enter elements separated by space: ").split())
    print(f"Your tuple: {t}")
    print(f"Length: {len(t)}")
    print(f"First element: {t[0] if t else 'Empty tuple'}")

# --- Dictionary CRUD ---
def manage_dict():
    my_dict = {}
    while True:
        print("\n-- Dictionary Menu --")
        print("a. Add/Update key-value")
        print("b. Delete key")
        print("c. Show dictionary")
        print("d. Back to main menu")
        opt = input("Choose option: ").lower()
        if opt == 'a':
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
            print(f"{key}:{value} added/updated!")
        elif opt == 'b':
            key = input("Enter key to delete: ")
            if key in my_dict:
                del my_dict[key]
                print(f"{key} deleted!")
            else:
                print(f"{key} not found!")
        elif opt == 'c':
            print(f"Current Dictionary: {my_dict}")
        elif opt == 'd':
            break
        else:
            print("Invalid option!")

# --- Set Operations ---
def manage_set():
    s1 = set(input("Enter first set elements separated by space: ").split())
    s2 = set(input("Enter second set elements separated by space: ").split())
    print(f"\nUnion: {s1 | s2}")
    print(f"Intersection: {s1 & s2}")
    print(f"Difference (s1 - s2): {s1 - s2}")
    print(f"Symmetric Difference: {s1 ^ s2}")

# --- Main Program ---
if __name__ == "__main__":
    while True:
        choice = show_menu()
        if choice == '1':
            manage_list()
        elif choice == '2':
            manage_tuple()
        elif choice == '3':
            manage_dict()
        elif choice == '4':
            manage_set()
        elif choice == '5':
            print("Exiting program. Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter a number 1-5.")