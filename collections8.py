fruits = ("apple", "banana", "orange", "grape")

print(fruits.count("banana"))  # Make sure that banana is in the code

# if "banana" in fruits:
# print("Banana is in the list") > you can use this as well

fruit_add = list(fruits)  # Changes tuple into a list

fruit_add.append("pineapple")  # add a new info on the list

fruits = tuple(fruit_add)  # Changes list into a tuple

print(fruits)
