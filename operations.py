def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def calculate(first_number: float, operation: str, second_number: float) -> float:
    if operation in ("+", "add"):
        return add(first_number, second_number)
    if operation in ("-", "sub"):
        return subtract(first_number, second_number)
    if operation in ("*", "mult"):
        return multiply(first_number, second_number)
    if operation in ("/", "div"):
        return divide(first_number, second_number)

    raise ValueError(f"Unsupported operation: {operation}")