import json

# Load data if file exists
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = {}

# json fuction
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

# Function to add data
def add_student():
    name = input("Enter student name: ").strip().title()
    if name in students:
        print("Student already exists!")
        return
    marks_input = input("Enter marks (0-100): ").strip()
    if not marks_input.isdigit():
        print("Invalid input! Please enter numbers only.")
        return
    marks = int(marks_input)
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return
    status = "PASS" if marks >= 50 else "FAIL"
    students[name] = {"marks": marks, "status": status}
    save_data()
    print(f"Student {name} added successfully!")

# ---------- View Students ----------
def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for name, details in students.items():
        print(f"Name: {name}")
        print(f"Marks: {details['marks']}")
        print(f"Status: {details['status']}")
        print("-"*20)

# ---------- Update Student ----------
def update_student():
    name = input("Enter student name to update: ").strip().title()
    if name not in students:
        print("Student not found!")
        return
    marks_input = input("Enter new marks (0-100): ").strip()
    if not marks_input.isdigit():
        print("Invalid input! Please enter numbers only.")
        return
    marks = int(marks_input)
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return
    status = "PASS" if marks >= 50 else "FAIL"
    students[name]["marks"] = marks
    students[name]["status"] = status
    save_data()
    print(f"Student {name} updated successfully!")

# ---------- Delete Student ----------
def delete_student():
    name = input("Enter student name to delete: ").strip().title()
    if name not in students:
        print("Student not found!")
        return
    del students[name]
    save_data()
    print(f"Student {name} deleted successfully!")

# ---------- Search Student ----------
def search_student():
    name = input("Enter student name to search: ").strip().title()
    if name not in students:
        print("Student not found!")
        return
    details = students[name]
    print("\n--- Student Found ---")
    print(f"Name: {name}")
    print(f"Marks: {details['marks']}")
    print(f"Status: {details['status']}")

# ---------- Show Topper ----------
def show_topper():
    if not students:
        print("No student records available.")
        return
    topper = max(students, key=lambda x: students[x]["marks"])
    details = students[topper]
    print("\n🏆 Topper Details")
    print(f"Name: {topper}")
    print(f"Marks: {details['marks']}")
    print(f"Status: {details['status']}")

# ------function to Add Statistics
def show_statistics():
    if not students:
        print("No student records available.")
        return
    marks_/list =[details["marks"] for details in students .values()]
    total = len(marks_list)
    average = sum(marks_list) / total
    highest = max(marks_list)
    lowest = min(marks_list)
    pass_count = sum(1 from m in marks_list if m >= 50)
    fail_count = total - pass_count
    print("\n Class Statistics")
    print(f"Total Students : {total}")
    print(f"Average Marks : {average:.2f}")
    print(f"Highest Marks : {highest}")
    print(f"Lowest Marks : {lowest}")
    print(f"Pass_count : {pass_count}")
    print(f"Fail_count : {fail_count}")

# ---------- Menu ----------
def show_menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Show Topper")
        print("7. Show Statistics")
        print("8. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            show_topper()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# ---------- Main ----------
if __name__ == "__main__":
    print("Welcome to the Student Management System!")
    show_menu()
    print("Project setup completed")
