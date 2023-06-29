from .student import Student
from typing import List


class StudentDb:
    def __init__(self):
        self.__students = []

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students: List[Student]):
        self.__students = students

    def add_student(self, admin_no, name, email, year, pem_group):
        student = Student(admin_no, name, email, year, pem_group)
        self.students.append(student)

    def get_student_by_admin_no(self, admin_no):
        for student in self.__students:
            if student.admin_no == admin_no:
                return student
        return None

    def get_students_by_pem_group(self, pem_group):
        students = []
        for student in self.__students:
            if student.pem_group == pem_group:
                students.append(student)
        return students

    def purge_students(self):
        self.students = []
