from colorama import Fore, Style, init
import os

# Initialize colorama
init(autoreset=True)

CONTACT_FILE = 'contact.txt'


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print formatted header with color."""
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + f"{title.center(40)}")
    print(Fore.CYAN + "=" * 40)


def add_contact(name, phone):
    """Add a new contact to the contact file."""
    if not os.path.exists(CONTACT_FILE):
        open(CONTACT_FILE, 'a').close()  # Create file if it doesn’t exist

    with open(CONTACT_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or ',' not in line:
                continue
            contact_name, _ = line.split(',', 1)
            if contact_name.lower() == name.lower():
                print(Fore.RED + "⚠️  Contact already exists.")
                return

    with open(CONTACT_FILE, 'a') as f:
        f.write(f"{name},{phone}\n")
    print(Fore.GREEN + "✅ Contact added successfully.")


def view_contacts():
    """Display all contacts."""
    print_header("All Contacts")
    try:
        with open(CONTACT_FILE, 'r') as f:
            contacts = [line.strip() for line in f if ',' in line.strip()]
            if not contacts:
                print(Fore.RED + "⚠️  No contacts found.")
                return

            for idx, line in enumerate(contacts, start=1):
                name, phone = line.split(',', 1)
                print(Fore.BLUE + f"{idx}. Name: {name}, Phone: {phone}")

    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")


def search_contact(name):
    """Search for a contact by name."""
    print_header(f"Search Result for '{name}'")
    found = False
    try:
        with open(CONTACT_FILE, 'r') as f:
            for line in f:
                if ',' not in line:
                    continue
                contact_name, phone = line.strip().split(',', 1)
                if contact_name.lower() == name.lower():
                    print(Fore.GREEN + f"✅ Found: Name: {contact_name}, Phone: {phone}")
                    found = True
                    break

        if not found:
            print(Fore.RED + "❌ Contact not found.")

    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")


def delete_contact(name):
    """Delete a contact by name."""
    try:
        with open(CONTACT_FILE, 'r') as f:
            contacts = [line.strip() for line in f if ',' in line.strip()]

        new_contacts = [line for line in contacts if line.split(',', 1)[0].lower() != name.lower()]

        if len(new_contacts) == len(contacts):
            print(Fore.RED + "❌ Contact not found.")
            return

        with open(CONTACT_FILE, 'w') as f:
            for contact in new_contacts:
                f.write(contact + "\n")

        print(Fore.GREEN + "🗑️  Contact deleted successfully.")

    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")


def update_contact(name, new_phone):
    """Update the phone number of a contact."""
    try:
        with open(CONTACT_FILE, 'r') as f:
            contacts = [line.strip() for line in f if ',' in line.strip()]

        updated = False
        for i in range(len(contacts)):
            contact_name, phone = contacts[i].split(',', 1)
            if contact_name.lower() == name.lower():
                contacts[i] = f"{contact_name},{new_phone}"
                updated = True
                break

        if not updated:
            print(Fore.RED + "❌ Contact not found.")
            return

        with open(CONTACT_FILE, 'w') as f:
            for contact in contacts:
                f.write(contact + "\n")

        print(Fore.GREEN + "🔁 Contact updated successfully.")

    except FileNotFoundError:
        print(Fore.RED + "⚠️  Contact file not found.")


# ======================
# Main Program Loop with match-case
# ======================
def main():
    while True:
        clear_screen()
        print_header("Contact Book Menu")
        print(Fore.CYAN + "1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        print(Fore.CYAN + "=" * 40)

        choice = input(Fore.YELLOW + "Enter your choice (1-6): ").strip()

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


if __name__ == "__main__":
    main()