# A simple way to use the same function multiple times with differents values.
def add(n1, n2):
    """
    Adds two numbers and returns the result.
    
    Args:
        n1 (int/float): The first number to add.
        n2 (int/float): The second number to add.
    
    Returns:
        int/float: The sum of the two numbers.
    """

    total = n1 + n2

    return total  # "return" allows us to use a value of the function outside of it. With not using it, you can not use a variable definied inside the function outside of it.


total_sum = add(5, 5)

total_sum2 = add(10, 20)

total_sum3 = add(100, 200)

print(f"We did some calculations. The total of the first is {total_sum}, the second is {total_sum2}, and the third is {total_sum3}.")  # This is how we can print the value returned by the function multiple times.
