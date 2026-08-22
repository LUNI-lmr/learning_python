numbers = [1, 2, 3, 4, 5]

numbers.append (6) # Add a new number

number_removed = numbers.pop (1) # remove a number on the index 1, counts "0"
print (f"Number {number_removed} was removed") # message

numbers.insert (2, 40) # Add a new number in index 3, which includes "0"

numbers.remove (4) # remove number 4

numbers.sort (reverse = True) # My list will be in decrescent order

print (numbers)