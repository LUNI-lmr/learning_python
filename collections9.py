girl = {  # Creates a dictionary
    "name": "Mary",
    "age": "20",
    "course": "engineer",
}

girl["grade"] = 9.5  # Add a new info

girl["age"] = 21  # update the age

girl.pop("course")  # remove info "course"

girl["courses"] = ["marketing", "HR", "advocacy"]  # Creates a string on the dictionary

print(girl["courses"][1])  # This way, you can see an info in a info more precisely

# print (girl)
