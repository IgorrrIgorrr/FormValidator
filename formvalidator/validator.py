import re

from email_validator import EmailNotValidError, validate_email


def find_field_type(value: str) -> str:
    if re.match(r"^\d{2}\.\d{2}\.\d{4}$", value) or re.match(
        r"^\d{4}-\d{2}-\d{2}$", value
    ):
        return "date"
    if re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
        return "phone"
    try:
        validate_email(value)
        return "email"
    except EmailNotValidError:
        pass
    return "text"
