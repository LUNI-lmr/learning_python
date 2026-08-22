fruits1 = ["apple", "watermelon", "banana"]
fruits2 = ["grape", "cherry", "guava"]

all_fruits = fruits1 + fruits2

all_fruits2 = all_fruits.copy() # A second version of the list. This way I can modify only one version

all_fruits.remove("banana") # Remove a fruit of the first version

print (all_fruits)
print (all_fruits2)