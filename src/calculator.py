def calculate(a: float, b: float, operation: str) -> float:

    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        case _:
            raise ValueError(
                f"Invalid operation '{operation}'. Supported operations are: add, subtract, multiply, divide."
            )
