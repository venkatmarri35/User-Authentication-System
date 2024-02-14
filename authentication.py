# authentication.py

import hashlib
import getpass

def register(users):
    username = input("Enter your username: ")

    # Check if the username already exists
    if username in users:
        print("Username already exists. Please choose another.")
        return

    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    users[username] = {'password': hashed_password}
    print("Registration successful!")

def login(users):
    username = input("Enter your username: ")

    # Check if the username exists
    if username not in users:
        print("Username not found. Please register.")
        return

    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the entered password matches the stored hash
    if hashed_password == users[username]['password']:
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")
