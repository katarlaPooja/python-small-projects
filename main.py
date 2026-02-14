print("Welcome to student management system ")
students={}
# Function to add student
def add_student():
    name = input("Enter the student name: ")
    marks = int(input("Enter the marks: "))

    if marks >= 50:
        status = "PASS"
    else:
        status = "FAIL"

    students[name] = {
        "marks": marks,
        "status": status
    }

    print("Student data added successfully!")

# Function to view students
def view_students():
    if not students:
        print("No student records found.")
    else:
        for name, details in students.items():
            print(f"\nName: {name}")
            print(f"Marks: {details['marks']}")
            print(f"Status: {details['status']}")

# Menu function
def show_menu():
   while True:
        print("\n1. Add student")
        print("2. View students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
print(students)
show_menu()
print("project setup completed")
