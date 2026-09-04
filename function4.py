def list(*numbers):  # * gives permission to you to use an unlimited number of arguments
    """
    Sums up a list of numbers.

    Args:
        *numbers (int/float): An unlimited number of numbers to sum up. 
    
    Returns:
        int/float: The sum of the numbers provided.
    """
    result = 0

    for number in numbers:
        result += number

    return result


sum_list = list(4, 6, 2, 5, 7, 0, 9)

print(f"The result is {sum_list}.")
