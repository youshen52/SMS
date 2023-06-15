from typing import List, Optional


class Student:
    def __init__(
        self: str,
        admin_no: str,
        name: str,
        email: str,
        year: int,
        pem_group: str,
    ):
        """
        Represents a student with the provided details.

        Args:
            admin_no (str): The admin number of the student.
            name (str): The name of the student.
            email (str): The email address of the student.
            year (int): The year the student was admitted.
            pem_group (str): The PEM group of the student.
        """
        self._admin_no = admin_no
        self._name = name
        self._email = email
        self._year = year
        self._pem_group = pem_group

    @property
    def admin_no(self) -> str:
        return self._admin_no

    @admin_no.setter
    def admin_no(self, value):
        self._admin_no = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def pem_group(self) -> str:
        return self._pem_group

    @pem_group.setter
    def pem_group(self, value):
        self._pem_group = value

    def __str__(self) -> str:
        return f"AdminNo: {self.admin_no}\nStudentName: {self.name}\nStudentEmail: {self.email}\nYearAdmitted: {self.year}\nPEMGroup: {self.pem_group}"
