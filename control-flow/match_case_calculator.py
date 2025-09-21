try:
    num1 = float(input("Enter the first number: ").strip())
    num2 = float(input("Enter the second number: ").strip())
except ValueError:
    print("Invalid number entered. Please enter numeric values.")
    raise SystemExit

op = input("Choose the operation (+, -, *, /): ").strip()

match op:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation. Please choose one of: +, -, *, /")
