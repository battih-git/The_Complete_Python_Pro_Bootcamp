print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill = 15
    print("Small Pizza costs $15")
    if pepperoni == 'Y':
        bill += 2
        print("Extra Pepperoni costs $2")
elif size == "M":
    bill = 20
    print("Medium Pizza costs $20")
    if pepperoni == 'Y':
        bill += 3
        print("Extra Pepperoni costs $3")
elif size == "L":
    bill = 25
    print("Large Pizza costs $25")
    if pepperoni == 'Y':
        bill += 3
        print("Extra Pepperoni costs $3")
else:
    print("You typed in wrong input.")

if extra_cheese == "Y":
    bill += 1
    print("Extra cheese cost extra $1.")
print(f"Your final bill is ${bill}")