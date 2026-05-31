def calculate(a: float, b: float, operation: str) -> float:

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ZeroDivisionError("Division by zero is impossible")
        return a / b

    else:
        raise ValueError(f"Invalid operation: {operation}")


# def calculate(a: float, b: float, operation: str) -> float:
#     match operation:
#         case "add":
#             return a + b
#         case "subtract":
#             return a - b
#         case "multiply":
#             return a * b
#         case "devide":
#             if b == 0:
#                 raise ZeroDivisionError("Division by zero is impossible")
#             return a / b
#         case _:
#             raise ValueError(f"Invalid operation: {operation}")
