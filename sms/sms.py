# Python modules
from termcolor import colored
from pyfiglet import Figlet
from tabulate import tabulate
from collections import deque
from typing import List, Union

# Local modules
from .rss import RequestSubSystem
from .students.student_db import StudentDb
from .students.student_req import StudentReq
from .algorithm import bubble_sort, insertion_sort, selection_sort, merge_sort
from .validator import Validator


class StudentManagementSystem:
    def __init__(self):
        self.database = StudentDb()
        self.request_subsystem = RequestSubSystem(self.database)

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
        print("e. Sort students' Name in ascending order")
        print("f. Sort students by PEM Group then Admin No in ascending order")
        print("g. Populate student data")
        print("h. Enter Student's Request")
        print("i. Exit the program")

    def choice_handler(self, choice):
        match choice:
            case "a":
                self.display_students()
            case "b":
                self.add_student()
            case "c":
                self.bubble_sort_admin_no()
            case "d":
                self.insertion_sort_pem_group()
            case "e":
                self.selection_sort_name()
            case "f":
                self.merge_sort_pem_group_admin_no()
            case "g":
                self.populate_data()
            case "h":
                self.enter_student_request()
            case "i":
                print("Exiting the program...")
                return -1
            case _:
                print(colored("Invalid choice. Please choose from a to f", "red"))

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
            if Validator.validate_year(year):
                break
            print(colored("Invalid year", "red"))
        while True:
            pem_group: str = input("Enter PEMGroup: ")
            if Validator.validate_pem_group(pem_group):
                break
            print(colored("Invalid PEMGroup", "red"))

        try:
            self.database.add_student(admin_no, name, email, year, pem_group)
            print(colored("Student record added successfully.", "green"))
        except Exception as e:
            print(colored(str(e), "red", attrs=["reverse", "blink"]))

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

    def _get_student_attr(self, *attrs: str) -> Union[List[str], List[tuple]]:
        if len(attrs) == 1:
            attr_list = [
                getattr(student, attrs[0]) for student in self.database.students
            ]
        else:
            attr_list = []
            for student in self.database.students:
                student_attrs = tuple(getattr(student, attr) for attr in attrs)
                attr_list.append(student_attrs)
        return attr_list

    def bubble_sort_admin_no(self):
        admin_nos = self._get_student_attr("admin_no")
        print(admin_nos)
        print("\nPasses: \n")
        sorted_admin_nos = bubble_sort(admin_nos)
        sorted_students = [
            self.database.get_student_by_admin_no(admin_no)
            for admin_no in sorted_admin_nos
        ]
        self.database.students = sorted_students
        print("\nStudents sorted by AdminNo in descending order:\n")
        self.display_students()

    def insertion_sort_pem_group(self):
        pem_groups_admin_nos = self._get_student_attr("pem_group", "admin_no")
        print("\nPasses: \n")
        sorted_admin_nos = insertion_sort(pem_groups_admin_nos)
        sorted_students = [
            self.database.get_student_by_admin_no(admin_no)
            for admin_no in sorted_admin_nos
        ]
        self.database.students = sorted_students
        print("\nStudents sorted by PEM in ascending order:\n")
        self.display_students()

    def selection_sort_name(self):
        names_admin_nos = self._get_student_attr("name", "admin_no")
        print("\nPasses: \n")
        sorted_admin_nos = selection_sort(names_admin_nos)
        sorted_students = [
            self.database.get_student_by_admin_no(admin_no)
            for admin_no in sorted_admin_nos
        ]
        self.database.students = sorted_students
        print("\nStudents sorted by Name in ascending order:\n")
        self.display_students()

    def merge_sort_pem_group_admin_no(self):
        pem_groups_admin_nos = self._get_student_attr("pem_group", "admin_no")
        print("\nPasses: \n")
        sorted_admin_nos = merge_sort(pem_groups_admin_nos)
        sorted_students = [
            self.database.get_student_by_admin_no(admin_no)
            for _, admin_no in sorted_admin_nos
        ]
        self.database.students = sorted_students
        print("\nStudents sorted by PEM then Admin No in ascending order:\n")
        self.display_students()

    def enter_student_request(self):
        self.request_subsystem.run()

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
                choice = input("\nPlease select one: ")
                if self.choice_handler(choice) == -1:
                    break

        except KeyboardInterrupt:
            print("\nExiting the program...")
