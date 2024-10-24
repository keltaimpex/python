num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


if operation == '+':
    print(f"The result is: {num1 + num2}")
elif operation == '-':
    print(f"The result is: {num1 - num2}")
elif operation == '*':
    print(f"The result is: {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation!")
