while True:
    numbers = range(1, 101)

    count = int(input("Which number do you want? "))
    operation = input("Which operation do you want (add/sub/multi/div): ").lower()

    if operation == "add":
        for n in numbers:
            result = count + n
            print(f"{count} + {n} = {result}")

    elif operation == "sub":
        for n in numbers:
            result = count - n
            print(f"{count} - {n} = {result}")

    elif operation == "multi":
        for n in numbers:
            result = count * n
            print(f"{count} * {n} = {result}")

    elif operation == "div":
        for n in numbers:
            if n == 0:
                continue
            result = count / n
            print(f"{count} / {n} = {result}")

    else:
        print("OperationalError")

    continue_program = input("\nDo you want to perform another operation? (y/n): ")

    if continue_program.lower() == "n":
        print("Program ended.")
        break
