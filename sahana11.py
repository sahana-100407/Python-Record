import random
import string
import sys

# Dictionary to store animal records
animal_dic = {}

print('\nAnimal Register Program:'
      '\n1: Enter A or a to add a new animal.'
      '\n2: Enter D or d to delete an animal.'
      '\n3: Enter U or u to update an animal.'
      '\n4: Enter L or l to check the list of animals.'
      '\n5: Enter E or e to exit the program.')

# ---------------- FUNCTIONS ----------------

def print_register():
    if not animal_dic:
        print("\nNo animals registered yet!")
        return

    table = PrettyTable(["ID", "Scientific Name", "Common Name"])
    for animal_id, data in animal_dic.items():
        table.add_row([animal_id, data["scientific_name"], data["common_name"]])

    print(table.get_string(title="Animal Register"))


def random_id():
    """Generate a random 4-character alphanumeric ID."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))


def add_animal():
    animal_id = random_id()
    scientific_name = input("\nPlease enter the scientific name: ").title()
    common_name = input("Please enter the common name: ").title()

    if not scientific_name or not common_name:
        print("You must write something!")
        return

    animal_dic[animal_id] = {
        'scientific_name': scientific_name,
        'common_name': common_name
    }
    print(f"\nAnimal '{common_name}' added successfully with ID {animal_id}!")


def delete_animal():
    animal_id = input("\nEnter the animal ID you want to delete: ").upper()
    try:
        if animal_id in animal_dic:
            choice = input(f"Are you sure you want to delete {animal_id}? (y/n): ").lower()
            if choice in ["y", "yes"]:
                del animal_dic[animal_id]
                print(f"{animal_id} has been deleted!")
            else:
                print("Deletion cancelled.")
        else:
            print("ID not found. Check the list by pressing 'L'.")
    except Exception as e:
        print(f"Something bad happened: {e}")


def update_animal():
    animal_id = input("\nEnter the animal ID you want to update: ").upper()
    try:
        if animal_id in animal_dic:
            choice = input(f"Update register {animal_id}? (y/n): ").lower()
            if choice in ["y", "yes"]:
                scientific_name = input("Write a new scientific name: ").title()
                common_name = input("Write a new common name: ").title()
                animal_dic[animal_id]['scientific_name'] = scientific_name
                animal_dic[animal_id]['common_name'] = common_name
                print("Register updated successfully!")
                print_register()
            else:
                print("Update cancelled.")
        else:
            print("ID not found. Check the list by pressing 'L'.")
    except Exception as e:
        print(f"Something bad happened: {e}")


def exit_program():
    print("Goodbye!")
    sys.exit()

# ---------------- MAIN PROGRAM LOOP ----------------

while True:
    user_input = input("\nWhat do you want to do? (A, D, U, L, E): ").lower()

    if user_input == "a":
        add_animal()
    elif user_input == "d":
        delete_animal()
    elif user_input == "u":
        update_animal()
    elif user_input == "l":
        print_register()
    elif user_input == "e":
        exit_program()
    elif not user_input:
        print("Please, enter something!")
    else:
        print("Invalid option. Try again!")
