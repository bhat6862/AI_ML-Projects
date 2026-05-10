'''Assignment (19/02/2026) 
Assignment Name : Student Data Manager 
Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades'''
# Student Data Manager
students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

# Calculate class average
total = sum(students.values())
average = total / len(students)

# Find topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Function to assign grade
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

# Display student details
print("\nStudent Results")
print("-" * 30)

for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"Name: {name} | Marks: {marks} | Grade: {grade}")

print("\nClass Average:", round(average, 2))
print("Topper:", topper, "with", top_marks, "marks")