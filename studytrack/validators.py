import re
from datetime import datetime

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def required(value: str, field: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError(f"{field} cannot be empty.")
    return value


def email(value: str) -> str:
    value = required(value, "Email")
    if not EMAIL_RE.match(value):
        raise ValueError("Enter a valid email address.")
    return value


def positive_int(value: str, field: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise ValueError(f"{field} must be a whole number.") from exc
    if number <= 0:
        raise ValueError(f"{field} must be greater than zero.")
    return number


def non_negative_int(value: str, field: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise ValueError(f"{field} must be a whole number.") from exc
    if number < 0:
        raise ValueError(f"{field} cannot be negative.")
    return number


def score(value: str, max_score: float) -> float:
    try:
        number = float(value)
    except ValueError as exc:
        raise ValueError("Score must be numeric.") from exc
    if number < 0 or number > max_score:
        raise ValueError(f"Score must be between 0 and {max_score}.")
    return number


def date_string(value: str) -> str:
    value = required(value, "Date")
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Date must use YYYY-MM-DD format.") from exc
    return value
