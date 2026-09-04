while True:  # It ensures that the loop starts correctly.
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    option = input("Enter the option: ")

    if option == "1":
        print("Result:", number1 + number2)

    elif option == "2":
        print("Result:", number1 - number2)

    elif option == "3":
        print("Result:", number1 * number2)

    elif option == "4":
        if number2 != 0:  # != means "different"
            print("Result:", number1 / number2)
        else:
            print("It is not possible to divide by zero.")

    else:
        print("Invalid option.")

    # it will complete the loop
    continue_program = input("\nDo you want to perform another operation? (y/n): ")

    if continue_program.lower() == "n":
        print("Program ended.")
        break
