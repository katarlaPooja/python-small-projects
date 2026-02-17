print("Welcome to student management system ")
students={}
# Function to add student
def add_student():
    name = input("Enter the student name: ").strip()
    if not name:
        print("Student name cannot be empty!")
        return
    if name in students:
        print("Student already exists!")
        return

    marks_input=input("enter marks(0_100):").strip()
    if not marks_input.isdigit():
        print("Invalid input! please enter numbers only.")
        return
    marks=int(marks_input)
    if marks<0 or marks>100:
      print("marks must be between 0to 100.")
      return
    status="Pass" if marks>=50 else "Fail"

    students[name] = {
        "marks": marks,
        "status": status
    }

    print("Student data added successfully!")

# Function to view students
def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n---student records-----")
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

        choice = input("Enter your choice: ").strip()

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
