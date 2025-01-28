# len(12345) This will return a type error because the len function only accepts sequence or collection data type
print("Hello") # This will return the result because string is a sequence data type.
print("\n")

# Type Checking: How to know the data type of object. We can use type function
print(type("Hello"))
print(type(1234))
print(type(3.1459))
print(type(True))
print("\n")

# Type conversion/casting: Convert a data from one type to another
print(type(int("123"))) # Convert str to int data type

# Fix the below code: Type error
# print("Number of letters in your name: " + len(input("Enter your name")))
name_of_user = input("Enter your name")
length = len(name_of_user)
print("Number of letters in your name: " + str(length))