try:
    age = int(input("How old are you?"))
except ValueError:
    print("The input should be in integer.")
    print("Try again with valid input.")
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You can drive at age {age}.")
