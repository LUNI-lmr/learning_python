# "True" makes your loop an infinite loop
while True:
    number = int(input("Put an even number: "))  # multiple of 2

    # "%" represents a division
    if number % 2 == 0:  # makes the code accepts only even numbers (números pares).
        print("An even number was added")
        break  # put an end in this endless loop

    else:
        print("This is not an even number >_<")

print("end")
