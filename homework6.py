import csv

def display_menu():
    print("Please choose an option:")
    print("1. Enter or update preferences")
    print("2. View current preferences")
    print("3. Quit")

def enter_or_update_preferences(file_path):
    preferences = {}

    preferences["Language"] = input("Please enter your preferred language: ")
    preferences["Theme Color"] = input("Please enter your theme color: ")
    preferences["Notification Settings"] = input("Please enter your notification settings: ")

    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(preferences.keys())
            writer.writerow(preferences.values())
        print("Preferences saved successfully.")
    except IOError:
        print("An error occurred when writing to the file.")

def view_current_preferences(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            preferences = list(reader)
            if len(preferences) == 0:
                print("No preferences found.")
                return
        for i, row in enumerate(preferences):
            if i == 0:
                print("Current Preferences:")
            print(', '.join(row))
    except FileNotFoundError:
        print("No preferences found. Please add some preferences first.")
    except IOError:
        print("An error occurred while reading the file.")

def main():
    path = "preferences.csv"

    print("Welcome to the User Preference Manager!")
    
    while True:
        display_menu()
        try:
            choice = int(input("Please enter your choice (1, 2, or 3): "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            continue

        if choice == 1:
            enter_or_update_preferences(path)
        elif choice == 2:
            view_current_preferences(path)
        elif choice == 3:
            print("Thank you for using the User Preference Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
