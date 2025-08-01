# Simple calculator

print("=== Simple Calculator ===")

while True:
    print("\nOptions:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            print(f"Result: {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"Result: {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"Result: {result}")
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {result}")
            else:
                print("Error: Cannot divide by zero.")

    else:
        print("Invalid option, please choose 1-5.")
