temperature = float(input("Enter the temperature: "))  # temperature variable

if temperature < 20:  # condition
    print("Cold, huh?")  # cold message
elif temperature >= 20 and temperature < 30:  # conditions
    print("A bit warm")  # warm message
else:  # opposite condition
    print("Hellish heat")  # extreme heat message
