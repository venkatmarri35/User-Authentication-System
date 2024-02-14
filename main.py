import sys
sys.path.append('..')

from app.authentication import register, login

# Sample user database (in-memory)
users = {}

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        register(users)
    elif choice == '2':
        login(users)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
