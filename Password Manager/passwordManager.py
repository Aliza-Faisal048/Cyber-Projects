import ast


PASSWORDS_FILE = "passwords.txt"


def add_password(website, username, password):
    try:
        with open(PASSWORDS_FILE, "r") as file:
            passwords = ast.literal_eval(file.read())
    except (FileNotFoundError, SyntaxError, ValueError):
        passwords = {}

    passwords[website] = {"username": username, "password": password}

    with open(PASSWORDS_FILE, "w") as file:
        file.write(str(passwords))


def retrieve_password(website):
    try:
        with open(PASSWORDS_FILE, "r") as file:
            passwords = ast.literal_eval(file.read())
        return passwords[website]["password"]
    except (FileNotFoundError, KeyError, SyntaxError, ValueError):
        return None

while(True) :
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        website = input("Enter the website: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        add_password(website, username, password)
        print("Password added successfully!")
    elif choice == '2':
        website = input("Enter the website to retrieve the password: ")
        password = retrieve_password(website)
        if password:
            print(f"The password for {website} is: {password}")
        else:
            print(f"No password found for {website}.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")