from operations import calculate


def format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return str(value)


def print_welcome() -> None:
    print("\n=== Python CLI Calculator ===")
    print("Commands:")
    print("  C = Clear current calculation")
    print("  R = Reset calculator history")
    print("  P = Print previous operations")
    print("  Q = Quit")


def print_operations() -> None:
    if not operation_history:
        print("\nNo previous operations found.")
        return

    print("\n=== Operation History ===")
    for index, entry in enumerate(operation_history, start=1):
        print(f"{index}. {entry}")


def get_number_input(prompt: str) -> float | str:
    while True:
        user_input = input(prompt).strip()

        if user_input.upper() in {"C", "R", "P", "Q"}:
            return user_input.upper()

        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or a command (C, R, P, Q).")


def get_operation_input(prompt: str) -> str:
    valid_operations = {"+", "-", "*", "/", "add", "sub", "mult", "div"}
    while True:
        user_input = input(prompt).strip().lower()

        if user_input.upper() in {"C", "R", "P", "Q"}:
            return user_input.upper()

        if user_input in valid_operations:
            return user_input

        print("Invalid operation. Please enter one of: +, -, *, /, add, sub, mult, div.")


operation_history: list[str] = []


def main() -> None:
    print_welcome()

    while True:
        print("\n--- New Calculation ---")
        first_number = get_number_input("Enter first number: ")

        if first_number == "C":
            continue
        if first_number == "P":
            print_operations()
            continue
        if first_number == "R":
            operation_history.clear()
            print("Calculator history has been reset.")
            continue
        if first_number == "Q":
            print("Exiting calculator...")
            break

        current_result = first_number

        while True:
            operation = get_operation_input(
                "\nSelect operation (+, -, *, /, add, sub, mult, div): "
            )

            if operation == "C":
                print("Current calculation cleared.")
                break
            if operation == "P":
                print_operations()
                continue
            if operation == "R":
                operation_history.clear()
                print("Calculator history has been reset.")
                break
            if operation == "Q":
                print("Exiting calculator...")
                return

            second_number = get_number_input("Enter second number: ")

            if second_number == "C":
                print("Current calculation cleared.")
                break
            if second_number == "P":
                print_operations()
                continue
            if second_number == "R":
                operation_history.clear()
                print("Calculator history has been reset.")
                break
            if second_number == "Q":
                print("Exiting calculator...")
                return

            try:
                result = calculate(current_result, operation, second_number)
                history_entry = (
                    f"{format_number(current_result)} {operation} "
                    f"{format_number(second_number)} = {format_number(result)}"
                )
                operation_history.append(history_entry)

                print(f"Result: {format_number(result)}")
                current_result = result

            except ZeroDivisionError as error:
                print(error)
            except ValueError as error:
                print(error)


if __name__ == "__main__":
    main()