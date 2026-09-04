numbers = [5, 8, 2, 9, 0, 1, 3, 4]

for n in numbers:
    if n % 2 != 0:  # makes the code accepts only odd numbers (números ímpares).
        continue  # if a number is accept by the condition, it breaks the loop and it goes to another number, and if the number does not, it will print.

    print(f"The number {n} is even")
