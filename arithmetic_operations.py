def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
    - num1 (float)
    - num2 (float)
    - operation (str): 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float or str: result of the operation or a message if division by zero
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
