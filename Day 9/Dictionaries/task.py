programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary["Loop"])

# Clearing the existing dictionary
programming_dictionary = {}
programming_dictionary.clear()
print(programming_dictionary)

# Edit an iter in a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
programming_dictionary['Bug'] = "A moth in your computer"
print(programming_dictionary['Bug'])

# Loop through your dictionary, it returns the key
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) # To print out the values, you can access it with keys of the dict.