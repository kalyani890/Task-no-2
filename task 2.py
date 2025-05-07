def calculator():
    print(" Simple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")

        choice = input("Enter operation (+, -, *, /): ")

        if choice == '+':
            result = num1 + num2
            print(f"\n Result: {num1} + {num2} = {result}")
        elif choice == '-':
            result = num1 - num2
            print(f"\n Result: {num1} - {num2} = {result}")
        elif choice == '*':
            result = num1 * num2
            print(f"\n Result: {num1} * {num2} = {result}")
        elif choice == '/':
            if num2 == 0:
                print("\n Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"\n Result: {num1} / {num2} = {result}")
        else:
            print("\n️ Invalid operation. Please use +, -, *, or /.")

    except ValueError:
        print(" Invalid input. Please enter numeric values.")

calculator()
