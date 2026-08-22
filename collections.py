# How to create a list in a single variable. Just use an array with square brackets and separate the elements with commas. For example:

fruits = ["apple", "banana", "watermelon", "grape", "orange", "banana", "kiwi", "tomato"] # list of fruits.

# print(fruits) > Show the list.

# print(fruits[0]) > Show the first element of the list, which begins with index 0.

# print(fruits[:4]) > Show the first four elements of the list, which does not recognize the first element as "0".

# print(fruits[2:4]) > Show the elements from index 2 (which includes "0") to index 4 (which does not include "0").

# print(len(fruits)) > Show the quantity of elements, which does not count the first as "0".  

# print(fruits[-1]) > Show the last element of the list, which is the same as print(fruits[len(fruits)-1]).

# print(fruits.count("banana")) > Show the quantity of elements that are equal to "banana".

# print(fruits.index("kiwi")) > Show the index of the element that is equal to "kiwi" (counts "0")

if "banana" in fruits:
    print("Banana is in the list")