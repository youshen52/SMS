import re


class Validator:
    @staticmethod
    def validate_pattern(pattern: str, value: str) -> bool:
        compiled_pattern = re.compile(pattern)
        return bool(re.fullmatch(compiled_pattern, value))

    @staticmethod
    def validate_email(email: str) -> bool:
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        return Validator.validate_pattern(email_pattern, email)

    @staticmethod
    def validate_name(name: str) -> bool:
        name_pattern = r"^[A-Za-z\s]+$"
        return Validator.validate_pattern(name_pattern, name)

    @staticmethod
    def validate_admin_no(admin_no: str) -> bool:
        admin_no_pattern = r"[0-9]{6}[A-Za-z]{1}"
        return Validator.validate_pattern(admin_no_pattern, admin_no)

    @staticmethod
    def validate_pem_group(pem_group: str) -> bool:
        pem_group_pattern = r"[A-Za-z]{2,3}[0-9]{3,4}"
        return not Validator.validate_pattern(pem_group_pattern, pem_group)

    @staticmethod
    def validate_length(x: str) -> bool:
        return len(x) <= 100

    @staticmethod
    def validate_year(year: str) -> bool:
        try:
            year = int(year)
            return not (1000 < year < 2024)
        except ValueError:
            return True
