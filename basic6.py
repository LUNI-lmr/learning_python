age = int(input("Enter your age: "))  # variable that receives the age

if 18 <= age <= 35:
    physical_condition = str(input("Is your physical condition good? "))
    medical_permission = str(input("Do you have medical permission? "))
    if physical_condition == "yes" or medical_permission == "yes":
        print("You are classified")
    else:
        print("You are disqualified")
else:
    print("You are disqualified")
