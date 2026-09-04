# colors = ["gray", "brown", "black", "red", "yellow"] > this is a list and can be modified later. The main caracteristic of a list is "[]".

# colors = ("gray", "brown", "black", "red", "yellow") > Meanwhile, this is a tupla and can not be modified later. The main caracteristic of a tupla is "()".

colors = (
    "gray",
    "brown",
    "black",
    "red",
    "yellow",
)  # The purpose of a tuple is to protect a list from having information added or deleted in an operation where its values cannot be changed.

colors_list = list(
    colors
)  # Here, The colors tuple will be transformed into a list, which will then be assigned to a variable.

colors_list.append(
    "green"
)  # This way you can "modify" tuplas, adding or removing info.

colors = tuple(
    colors_list
)  # Change the colors list into a tuple, returning to be "colors"

print(colors)
