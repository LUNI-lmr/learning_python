def count(number):
    """
    Counts from the given number down to 0 and prints each number.

    Args:
        number (int): The number to count until 0.

    returns:
        None: This function does not return any value; it prints the count of the number down to 0.
    """
    while True:
        print(number)
        number -= 1
        if number <= 0:
            break


#  count(int(input("Enter a number to count down from: ")))


def count_2(number):
    """
    Counts from the given number down to 0 and prints each number.

    Args:
        number (int): The number to count until 0.

    returns:
        None: This function does not return any value; it prints the count of the number down to 0.
    """

    for i in range(number, 0, -1):
        print(i)


# count_2(int(input("Enter a number to count down from: ")))


def bigger_number(list_of_numbers):
    """
    Finds the biggest number in a list of numbers.

    Args:
        list_of_numbers (list): A list of numbers to find the biggest number from.

    Returns:
        int/float: The biggest number in the list.
    """
    bigger_number = list_of_numbers[0]
    for number in list_of_numbers:
        bigger_number = max(bigger_number, number)
    return bigger_number


list = [1, 6, 3, 6, 4, 8, 9, 10, 6, 89]

biggest_number = bigger_number(list)

print(f"The biggest number in the list is: {biggest_number}")
