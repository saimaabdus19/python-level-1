import datetime

def log_error():
    error_message = input("Enter your error message: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("error_log.txt", "a") as file:
            file.write(f"[{timestamp}] {error_message}\n")
        print("Error logged successfully.")
    except Exception as e:
        print(f"An error occurred while logging the error: {e}")

def view_errors():
    try:
        with open("error_log.txt", "r") as file:
            errors = file.readlines()
            if errors:
                print("\nLogged Errors:")
                for error in errors:
                    print(error.strip())
            else:
                print("No error messages found.")
    except FileNotFoundError:
        print("No error messages found.")
    except Exception as e:
        print(f"An error occurred while reading the error log: {e}")

def main():
    print("Welcome to the Error Logger!")

    while True:
        print("\nMenu:")
        print("1. Log a new error message")
        print("2. View all error messages")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            log_error()
        elif choice == "2":
            view_errors()
        elif choice == "3":
            print("Thank you for using the Error Logger. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
