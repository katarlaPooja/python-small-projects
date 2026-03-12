import json
import csv
class StudentManager:
    def __init__(self):
# Function to Load data if file exists
        try:
            with open("students.json", "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            self.students = {}
            
# Function to Save data to JSON
    def save_data(self):
        with open("students.json", "w") as file:
            json.dump(self.students, file, indent=4)

# Function to  Add Student
    def add_student(self):
        name = input("Enter student name: ").strip().title()
        if name in self.students:
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
        self.students[name] = {"marks": marks, "status": status}
        self.save_data()
        print(f"Student {name} added successfully!")
        
#Function to View Students
    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
        print("\n--- Student Records ---")
        for name, details in self.students.items():
            print(f"Name: {name}")
            print(f"Marks: {details['marks']}")
            print(f"Status: {details['status']}")
            print("-" * 20)

# Function to  Update Student
    def update_student(self):
        name = input("Enter student name to update: ").strip().title()
        if name not in self.students:
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
        self.students[name]["marks"] = marks
        self.students[name]["status"] = status
        self.save_data()
        print(f"Student {name} updated successfully!")
        
# Function to  Delete Student
    def delete_student(self):
        name = input("Enter student name to delete: ").strip().title()
        if name not in self.students:
            print("Student not found!")
            return
        confirm = input(f"Are you sure you want to delete {name}? (yes/no): ").lower()
        if confirm == "yes":
            del self.students[name]
            self.save_data()
            print(f"Student {name} deleted successfully!")
        else:
            print("Deletion cancelled.")
# Function to Search Student
    def search_student(self):
        name = input("Enter student name to search: ").strip().title()
        if name not in self.students:
            print("Student not found!")
            return
        details = self.students[name]
        print("\n--- Student Found ---")
        print(f"Name: {name}")
        print(f"Marks: {details['marks']}")
        print(f"Status: {details['status']}")

# Function to Show Topper
    def show_topper(self):
        if not self.students:
            print("No student records available.")
            return
        topper = max(self.students, key=lambda x: self.students[x]["marks"])
        details = self.students[topper]
        print("\n🏆 Topper Details")
        print(f"Name: {topper}")
        print(f"Marks: {details['marks']}")
        print(f"Status: {details['status']}")

# Function to Show Statistics
    def show_statistics(self):
        if not self.students:
            print("No student records available.")
            return
        marks_list = [details["marks"] for details in self.students.values()]
        total = len(marks_list)
        average = sum(marks_list) / total
        highest = max(marks_list)
        lowest = min(marks_list)
        pass_count = sum(1 for m in marks_list if m >= 50)
        fail_count = total - pass_count
        print("\nClass Statistics")
        print(f"Total Students : {total}")
        print(f"Average Marks : {average:.2f}")
        print(f"Highest Marks : {highest}")
        print(f"Lowest Marks : {lowest}")
        print(f"Pass Count : {pass_count}")
        print(f"Fail Count : {fail_count}")

# Function to Show Ranking
    def show_ranking(self):
        if not self.students:
            print("No student records available.")
            return
        sorted_students = sorted(
            self.students.items(),
            key=lambda item: item[1]["marks"],
            reverse=True
        )
        print("\n🏅 Ranking")
        for rank, (name, details) in enumerate(sorted_students, start=1):
            print(f"{rank}. {name} - {details['marks']}")
    
# Function to Export
    def export_to_csv(self):
        if not self.students:
            print("No Student records available.")
            return
        with open("students_report.csv","w",newline="")as file:
            writer =csv.writer(file)
            #Header row
            writer.writerow(["Name","Marks","status"])
            #student data
            for name, details in self.students.items():
                writer.writerow([name,details["marks"],details["status"]])
        print("students reported sucessfully to students_report.csv")

# Function of Dashboar
    def show_dashboard(self):
        print("\n===Student Dashboard====")
        if not self.students:
            print("No students records available")
            print("===========")
            return
        marks_list = [details["marks"]for details in self.students.values()]
        total = len(marks_list)
        pass_count = sum(1 for details in marks_list if m >=50)
        fail_count = total-pass_count
        average = sum(marks_list) / total
        print(f"Total Students : {total}")
        print(f"Pass Students  : {pass_count}")
        print(f"Fail Students  : {fail_count}")
        print(f"Average Marks  : {average:.2f}")
        print("========")

# Function to Search by marks 
    def search_by_marks(self):
        if not self.students:
            print("No Students records available.")
            return
        marks_input = input("Enter minimum marks:").strip()
        if not marks_input.isdigit():
            print("Invalid input.Please enter numbers only.")
            return
        min_marks = int(marks_input)
        print(f"\nStudents with marks >={min_marks}")
        found = False
        for name,details in self.students.items():
            if details["marks"] >= min_marks:
                print(f"{name} - {details['marks']}")
                found = True
        if not found:
            print("No  Students found with that marks range.")
            
# Function to  Show Menu
    def show_menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Search Student")
            print("6. Show Topper")
            print("7. Show Statistics")
            print("8. Show Ranking")
            print("9. Export to csv")
            print("10. Search by marks")
            print("11. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                self.search_student()
            elif choice == "6":
                self.show_topper()
            elif choice == "7":
                self.show_statistics()
            elif choice == "8":
                self.show_ranking()
            elif choice == "9":
                self.export_to_csv()
            elif choice == "10":
                self.search_by_marks()
            elif choice == "11":
                print("Exiting program... Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# Function to Login
def login():
    USERNAME = "admin"
    PASSWORD = "1234"
    print("====== Login System ======")
    while True:
        username = input("Enter Username: ")
        password = input("Enter password: ")
        if username == USERNAME and password == PASSWORD:
            print("Login Sucessfully!\n")
            break
        else:
            print("Invalid username or password.Try again.\n")
            
# Function to Show Main
if __name__ == "__main__":
    login()
    print("Welcome to the Student Management System!")
    manager = StudentManager()
    manager,show_dashboard()
    manager.show_menu()
    print("Project setup completed")
