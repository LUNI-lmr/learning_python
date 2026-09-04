age = 20

def my_function():
    """
    Prints a message with the name and age of the person.

    Args:
        None: This function does not take any arguments.

    Returns:
        None: This function does not return any value; it only prints a message.
    """

    name = "LUNI-lmr"

    print(f"This is my function. My name is {name} and I'm {age} years old.")


# my_function() > calling the function to execute it

# observation: you can use variables defined outside the function (like 'age') inside the function, but you cannot use variables defined inside the function (like 'name') outside of it.


def add(n1, n2):  # this is parameters/arguments and we use it when we want to pass values to the function
    """
    Adds two numbers and prints the result.

    Args:
        n1 (int/float): The first number to add.
        n2 (int/float): The second number to add.

    Returns:
        None: This function does not return any value; it only prints the sum.
    """

    total = n1 + n2

    print(f"The sum of {n1} and {n2} is {total}.")


# add (4, 9) # One way to call the function

# add (int(input("Enter the first number: ")), int(input("Enter the second number: "))) # This is how we can ask the user for input


def compliment(name):  # you can use an argument when you want to send a value to the function from outside of it.
    """
    Prints a compliment message for the given name.

    Args:
        name (str): The name of the person to compliment.

    Returns:
        None: This function does not return any value; it only prints a compliment message.
    """
    print(f"Congratulations, {name}! You are doing great!")


# compliment ("LUNI-lmr")
