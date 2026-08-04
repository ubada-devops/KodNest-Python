# Simple Calculator Program

def main():
    try:
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        operation = input("Enter operation (+, -, *, /): ").strip()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        # Format output as integer if it's a whole number
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
