Fruits = ["apple", "banana", "cherry"]

print(Fruits)  # Show the list of fruits

Fruits_add = str(input("Enter a fruit to add to the list: "))

# Fruits.append (Fruits_add) > add the fruit to the list

Fruits.insert(0, Fruits_add)  # add a fruit to the list and its position, includes "0"

# Fruits.remove ("apple") > remove a fruit from the list

# Fruits.pop (2) > remove the fruit on index 2, counts "0"
# It also can be done this way:
# Fruit_removed = Fruits.pop (2)
# print(f"Fruit {Fruit_removed} was removed from the list.")

# Fruits.clear () > Clear the list

print(f"the new list is: {Fruits}")  # Show the updated list of fruits
