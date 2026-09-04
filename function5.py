def find_average(*numbers):
    """
    Calculates the average of a list of numbers.
    
    Args:
        *numbers (int/float): An unlimited number of numbers to calculate the average from.

    Returns:
        float: The average of the numbers provided.
    """
    qtt = len(numbers)

    sum = 0

    for number in numbers:
        sum += number

    average = sum / qtt

    return average


result = find_average(12, 90, 45, 34, 23, 73, 21)

print(f"The average of the numbers is: {result}")
 