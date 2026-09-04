age = int(input("Enter your age: "))  # variable that receives the age
physical_condition = str(
    input("Is your physical condition good? ")
)  # variable that receives the answer about physical condition
medical_permission = str(
    input("Do you have medical permission? ")
)  # variable that receives the answer about medical permission

if age > 18 and (
    physical_condition == "yes" or medical_permission == "yes"
):  # condition, the parentheses determine that the condition inside is evaluated first
    print("You are classified")  # response
else:
    print("You are disqualified")
