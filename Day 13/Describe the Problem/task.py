def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# Running through the range of 1-20 (20 is exclusive)
# 2. When is the function meant to print "You got it"?
# Once the loop reaches as 20
# 3. What are your assumptions about the value of i?
# The loop will never run till 20 because the value is not exclusive


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("Now you got it")
my_function()
