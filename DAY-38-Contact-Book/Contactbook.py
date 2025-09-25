from colorama import Fore, Style, init
import os

# Initialize colorama
init(autoreset=True)

contact = 'contact.txt'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + f"{title.center(40)}")
    print(Fore.CYAN + "=" * 40)

def add_contact(name, phone):
    with open(contact, 'a') as f:
        f.write(f"{name},{phone}\n")
    print(Fore.GREEN + "✅ Contact added successfully.")

def view_contacts():
    print_header("All Contacts")
    try:
        with open(contact, 'r') as f:
            contacts = f.readlines()
            if not contacts:
                print(Fore.RED + "⚠️  No contacts found.")
                return
            for idx, line in enumerate(contacts, start=1):
                name, phone = line.strip().split(',')
                print(Fore.BLUE + f"{idx}. Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")

def search_contact(name):
    print_header(f"Search Result for '{name}'")
    found = False
    try:
        with open(contact, 'r') as f:
            for line in f:
                contact_name, phone = line.strip().split(',')
                if contact_name.lower() == name.lower():
                    print(Fore.GREEN + f"✅ Found: Name: {contact_name}, Phone: {phone}")
                    found = True
        if not found:
            print(Fore.RED + "❌ Contact not found.")
    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")

def delete_contact(name):
    try:
        with open(contact, 'r') as f:
            contacts = f.readlines()

        with open(contact, 'w') as f:
            found = False
            for line in contacts:
                contact_name, phone = line.strip().split(',')
                if contact_name.lower() != name.lower():
                    f.write(line)
                else:
                    found = True

        if found:
            print(Fore.GREEN + "🗑️  Contact deleted successfully.")
        else:
            print(Fore.RED + "❌ Contact not found.")
    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")

def update_contact(name, new_phone):
    try:
        with open(contact, 'r') as f:
            contacts = f.readlines()

        with open(contact, 'w') as f:
            found = False
            for line in contacts:
                contact_name, phone = line.strip().split(',')
                if contact_name.lower() == name.lower():
                    f.write(f"{contact_name},{new_phone}\n")
                    found = True
                else:
                    f.write(line)

        if found:
            print(Fore.GREEN + "🔁 Contact updated successfully.")
        else:
            print(Fore.RED + "❌ Contact not found.")
    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")

# ======================
# Main Program Loop with match-case
# ======================
while True:
    print_header("Contact Book Menu")
    print(Fore.CYAN + "1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")
    print(Fore.CYAN + "=" * 40)

    choice = input(Fore.YELLOW + "Enter your choice (1-6): ").strip()

    # Use match-case instead of if-elif (Python 3.10+)
    match choice:
        case '1':
            clear_screen()
            print_header("Add New Contact")
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            if name and phone:
                add_contact(name, phone)
            else:
                print(Fore.RED + "❌ Name and phone number cannot be empty.")

        case '2':
            clear_screen()
            view_contacts()

        case '3':
            clear_screen()
            name = input("Enter name to search: ").strip()
            if name:
                search_contact(name)
            else:
                print(Fore.RED + "❌ Name cannot be empty.")

        case '4':
            clear_screen()
            name = input("Enter name to delete: ").strip()
            if name:
                delete_contact(name)
            else:
                print(Fore.RED + "❌ Name cannot be empty.")

        case '5':
            clear_screen()
            name = input("Enter name to update: ").strip()
            new_phone = input("Enter new phone number: ").strip()
            if name and new_phone:
                update_contact(name, new_phone)
            else:
                print(Fore.RED + "❌ Name and new phone number cannot be empty.")

        case '6':
            print(Fore.MAGENTA + "\n👋 Exiting the Contact Book. Goodbye!\n")
            break

        case _:
            print(Fore.RED + "❌ Invalid choice. Please try again.")

    input(Fore.YELLOW + "\nPress Enter to continue...")
    clear_screen()
