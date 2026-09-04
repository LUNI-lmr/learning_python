# def verify_even(number):

# if number % 2 == 0:

# print (f"The number {number} is even")

# else:

# print (f"The number {number} is odd")

# verify_even (4)

# instead os use this, you can use return True or False for flexibility:


def verify_even(number):
    """
    Checks if a given number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    if number % 2 == 0:  # noqa: SIM103
        return True

    else:
        return False


if verify_even(7):
    print("The number is even")

else:
    print("The number is odd")
