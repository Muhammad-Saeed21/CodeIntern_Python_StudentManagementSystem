# ============================================================
# Project Title : Student Management System (Console App)
# Author        : Muhammad Saeed
# Description   : 
#   This console-based Python application allows users to:
#   - Add new student records
#   - Update existing student details
#   - Delete or search students
#   - Display all students in a formatted table
#   - Store student data permanently using a JSON file
#
# Technologies  : Python, JSON, File Handling
# ============================================================


# Import json module to store and retrieve data
import json

# Import os module to check file existence
import os


# File name where student data will be stored
FILE_NAME = "students.json"


# -----------------------------
# Function: Load students data
# -----------------------------
def load_students():
    # Check if JSON file exists
    if not os.path.exists(FILE_NAME):
        # If file does not exist, return empty list
        return []
    
    # Open file in read mode
    with open(FILE_NAME, "r") as file:
        # Load and return JSON data
        return json.load(file)


# -----------------------------
# Function: Save students data
# -----------------------------
def save_students(students):
    # Open file in write mode
    with open(FILE_NAME, "w") as file:
        # Save student list into JSON file with formatting
        json.dump(students, file, indent=4)


# -----------------------------
# Function: Add new student
# -----------------------------
def add_student():
    # Load existing students
    students = load_students()
    
    # Take roll number from user
    roll = input("Enter Roll No: ")
    
    # Check for duplicate roll number
    for s in students:
        if s["roll"] == roll:
            print("Student with this Roll No already exists!")
            return
    
    # Take student name
    name = input("Enter Name: ")
    
    # Take student marks
    marks = float(input("Enter Marks: "))
    
    # Create student dictionary
    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    
    # Add student to list
    students.append(student)
    
    # Save updated list
    save_students(students)
    
    # Success message
    print("Student added successfully!")


# -----------------------------
# Function: Display all students
# -----------------------------
def display_students():
    # Load students from file
    students = load_students()
    
    # If no students exist
    if not students:
        print("No student records found.")
        return
    
    # Print table header
    print("\n{:<10} {:<20} {:<10}".format("Roll No", "Name", "Marks"))
    print("-" * 40)
    
    # Print each student record
    for s in students:
        print("{:<10} {:<20} {:<10}".format(
            s["roll"], s["name"], s["marks"]
        ))


# -----------------------------
# Function: Search student
# -----------------------------
def search_student():
    # Load student data
    students = load_students()
    
    # Take roll number to search
    roll = input("Enter Roll No to search: ")
    
    # Search student
    for stu in students:
        if stu["roll"] == roll:
            print("\n Student Found:")
            print(stu)
            return
    
    # If student not found
    print("Student not found.")


# -----------------------------
# Function: Update student
# -----------------------------
def update_student():
    # Load student data
    students = load_students()
    
    # Take roll number
    roll = input("Enter Roll No to update: ")
    
    # Find and update student
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["marks"] = float(input("Enter new marks: "))
            
            # Save changes
            save_students(students)
            
            print("Student updated successfully!")
            return
    
    # If student not found
    print("Student not found.")


# -----------------------------
# Function: Delete student
# -----------------------------
def delete_student():
    # Load student data
    students = load_students()
    
    # Take roll number
    roll = input("Enter Roll No to delete: ")
    
    # Find / delete student
    for stu in students:
        if stu["roll"] == roll:
            students.remove(stu)
            
            # Save updated data
            save_students(students)
            
            print("Student deleted successfully!")
            return
    
    # If student is not found
    print("Student not found.")


# -----------------------------
# Menu Function
# -----------------------------
def main():
    # Infinite loop for menu
    while True:
        print("\n<===== Student Management System =====>")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")
        
        # Take user choice
        choice = input("Enter choice (1-6): ")
        
        # Menu operations
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            display_students()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# -----------------------------
# Program Execution Starts Here
# -----------------------------
main()