while True:
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    count = int(input("Which number do you want? "))

    for n in numbers:
        multi = count * n

        print(f"{count} * {n} = {multi} ")

    continue_program = input("\nDo you want to perform another operation? (y/n): ")

    if continue_program.lower() == "n":
        print("Program ended.")

        break
