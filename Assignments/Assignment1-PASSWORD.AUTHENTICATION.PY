'''Assignment 1- 7th Feb 2026
Create a strong code for password authentication using python. 
'''
import re
import hashlib

# Function to check password strength
def validate_password(password):
    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return False
    if not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not re.search("[0-9]", password):
        print("Password must contain at least one number.")
        return False
    if not re.search("[!@#$%^&*]", password):
        print("Password must contain at least one special character.")
        return False

    return True


# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# User Registration
print("----- User Registration -----")
username = input("Enter username: ")

while True:
    password = input("Create password: ")

    if validate_password(password):
        hashed_password = hash_password(password)
        print("Password created successfully!")
        break
    else:
        print("Please try again.\n")


# Login Authentication
print("\n----- Login System -----")
attempts = 3

while attempts > 0:
    login_user = input("Enter username: ")
    login_pass = input("Enter password: ")

    hashed_input = hash_password(login_pass)

    if login_user == username and hashed_input == hashed_password:
        print("Login successful! Access granted.")
        break
    else:
        attempts -= 1
        print("Invalid credentials. Attempts left:", attempts)

if attempts == 0:
    print("Account locked due to multiple failed login attempts.")