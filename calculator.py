# Basic Calculator Program

# Function to perform the calculation
def calculator():
    # Input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on user input
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    else:
        result = "Invalid operation!"

    # Display the result
    print(f"The result of {num1} {operation} {num2} = {result}")

# Call the calculator function
calculator()
