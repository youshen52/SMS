# PythonModule
from collections import deque
from termcolor import colored
from pyfiglet import Figlet
import os

# Local Modules
from .students.student_req import StudentReq
from .validator import Validator


class RequestSubSystem:
    def __init__(self, database):
        self.request_queue = deque()
        self.database = database

    def choice_handler(self, choice):
        match choice:
            case "a":
                self.add_request()
            case "b":
                self.get_request_count()
            case "c":
                self.handle_next_request()
            case "d":
                print("Returning to Main Menu...")
                return -1
            case _:
                print(colored("Invalid choice. Please choose from a to d", "red"))

    @staticmethod
    def print_title():
        print(Figlet(font="slant").renderText("Student Request Subsystem"))
        print("-" * 16)

    @staticmethod
    def print_menu():
        print("a. Enter Student's Request")
        print("b. View Number of Requests")
        print("c. Service next in Queue")
        print("d. Return to Main Menu")

    def add_request(self):
        while True:
            admin_no = input("Enter Student Admin No: ")
            if Validator.validate_admin_no(
                admin_no
            ) and self.database.get_student_by_admin_no(admin_no):
                break
            print(colored("Invalid admin_no", "red"))

        request = input("Enter Student's Request: ")

        request = StudentReq(admin_no, request)
        self.request_queue.append(request)
        print(colored("Student request added successfully.", "green"))

    def get_request_count(self):
        print(len(self.request_queue))

    def handle_next_request(self):
        if self.request_queue:
            request = self.request_queue.popleft()
            print(f"AdminNo: {request.admin_no}")
            print(f"Request: {request.request}")
            print(f"Number of remaining requests: {self.get_request_count()}")
        else:
            print("No requests in the queue.")

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.print_title()
        while True:
            self.print_menu()
            choice = input("\nPlease select one: ")
            if self.choice_handler(choice) == -1:
                os.system("cls" if os.name == "nt" else "clear")
                break
