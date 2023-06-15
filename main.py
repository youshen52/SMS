# Python modules
from termcolor import colored
from pyfiglet import Figlet
from tabulate import tabulate
import abc

# Local modules
from students.student_db import StudentDb
from algorithm import bubble_sort, insertion_sort
from validator import Validator


class StudentManagementSystem:
    def __init__(self):
        self.database = StudentDb()

    @staticmethod
    def print_title():
        print(Figlet(font="slant").renderText("Student Management System"))
        print("-" * 16)

    @staticmethod
    def print_menu():
        print("a. Display all students' records")
        print("b. Add a new student record")
        print("c. Sort students by AdminNo in descending order")
        print("d. Sort students' PEMGroup in ascending order")
        print("e. Populate student data")
        print("f. Exit the program")

    def choice_handler(self, choice):
        match choice:
            case "a":
                self.display_students()
            case "b":
                self.add_student()
            case "c":
                self.sort_admin_no()
            case "d":
                self.sort_pem_group()
            case "e":
                self.populate_data()
            case "f":
                print("Exiting the program...")
                return -1
            case _:
                print(colored("Invalid choice. Please choose from a to f", "red"))

    def display_students(self):
        headers = ["Name", "Email", "Year", "AdminNo", "PEMGroup"]
        rows = []
        for student in self.database.students:
            rows.append(
                [
                    student.name,
                    student.email,
                    student.year,
                    student.admin_no,
                    student.pem_group,
                ]
            )
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        print("\n")

    def add_student(self):
        while True:
            name = input("Enter Student Name: ")
            if Validator.validate_name(name):
                break
            print(colored("Invalid name", "red"))
        while True:
            admin_no: str = input("Enter AdminNo: ")
            if Validator.validate_admin_no(admin_no):
                break
            print(colored("Invalid admin number", "red"))
        while True:
            email: str = input("Enter your email: ")
            if Validator.validate_email(email):
                break
            print(colored("Invalid email", "red"))
        while True:
            year: str = input("Enter Year admitted: ")
            if Validator.validate_year(email):
                break
            print(colored("Invalid year", "red"))
        while True:
            pem_group: str = input("Enter PEMGroup: ")
            if Validator.validate_pem_group(email):
                break
            print(colored("Invalid PEMGroup", "red"))

        try:
            self.database.add_student(admin_no, name, email, year, pem_group)
            print(colored("Student record added successfully.", "green"))
        except Exception as e:
            print(colored(str(e), "red", attrs=["reverse", "blink"]))

    def sort_admin_no(self):
        # List of admin_nos
        admin_nos = [student.admin_no for student in self.database.students]
        # Perform Bubble sort and print passes
        print("\nPasses: \n")
        sorted_admin_nos = bubble_sort(admin_nos)
        # List of sorted admin_nos
        sorted_students = [
            self.database.get_student_by_admin_no(admin_no)
            for admin_no in sorted_admin_nos
        ]
        # Update database
        self.database.students = sorted_students
        # Display students
        print("\nStudents sorted by AdminNo in descending order:\n")
        self.display_students()

    def sort_pem_group(self):
        # List of pem groups
        pem_groups = [student.pem_group for student in self.database.students]
        # List of admin_nos
        admin_nos = [student.admin_no for student in self.database.students]
        # Zip pem groups and admin_nos
        pem_groups_admin_nos = list(zip(pem_groups, admin_nos))
        # Perform Insertion sort and print passes
        print("\nPasses: \n")
        sorted_admin_nos = insertion_sort(pem_groups_admin_nos)
        # List of sorted admin_nos
        sorted_students = [
            self.database.get_student_by_admin_no(admin_no)
            for admin_no in sorted_admin_nos
        ]
        # Update database
        self.database.students = sorted_students
        # Display students
        print("\nStudents sorted by PEM in ascending order:\n")
        self.display_students()

    def populate_data(self):
        self.database.purge_students()
        self.database.add_student(
            "2101252Y", "steve", "steve@mail.com", "2021", "IT2101"
        )
        self.database.add_student(
            "2121613Y", "strange", "tony@mail.com", "2021", "IT2103"
        )
        self.database.add_student(
            "2101122A", "peter", "peter@mail.com", "2021", "IT2101"
        )
        self.database.add_student("2121623Y", "tony", "tony@mail.com", "2021", "IT2103")
        self.database.add_student(
            "2121523Y", "banner", "banner@mail.com", "2021", "IT2102"
        )
        self.database.add_student(
            "2121563H", "clark", "clark@mail.com", "2021", "IT2102"
        )
        self.database.add_student(
            "2111025C", "bruce", "bruce@mail.com", "2021", "IT2102"
        )

        print(colored("Data populated successfully!", "green"))
        self.display_students()

    def run(self):
        try:
            self.print_title()
            while True:
                self.print_menu()
                choice = input("\nEnter your choice: ")
                if self.choice_handler(choice) == -1:
                    break

        except KeyboardInterrupt:
            print("\nExiting the program...")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()
