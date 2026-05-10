'''Assignment (12/02/2026)
Assignment Name : Smart Input Program
Description : Build a Python program that takes name, age, hobby prints a personalized message while categorizing age using conditionals.'''
# Function to categorize age
def categorize_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior Citizen"

# Taking name input
name = input("Enter your name: ").strip()

# Age validation
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be a positive number.")
    except ValueError:
        print("Please enter a valid number.")

# Taking multiple hobbies
hobbies = input("Enter your hobbies (separate by commas): ")
hobby_list = [h.strip() for h in hobbies.split(",")]

# Categorize age
category = categorize_age(age)

# Display output
print("\n" + "="*40)
print("        PERSONALIZED PROFILE")
print("="*40)

print(f"Name        : {name}")
print(f"Age         : {age}")
print(f"Category    : {category}")
print("Hobbies     : " + ", ".join(hobby_list))

print("\nHello", name + "!")
print(f"You are an {category}. It's great that you enjoy {', '.join(hobby_list)}.")
print("Keep pursuing your interests and keep learning!")

print("="*40)