def personal_info(**info):  #  ** enables the function to create a dictionary of key-value pairs
    """
    Prints personal information provided as keyword arguments.

    Args:
        **info (dict): A dictionary of key-value pairs representing personal information.
    
    Returns:
        None: This function does not return any value; it prints the personal information provided.
    """
    for key, value in info.items():  #  Makes the dictionary easier to read
        print(f"{key}: {value}")

personal_info(name="John", age=30, city="New York")