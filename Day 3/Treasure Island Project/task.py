print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? \n Type \"left\" or \"right\": ").lower()
if direction == 'left':
    print("You've come t a lake. There is an island in the middle of the lake.")
    choice = input("Type \"wait\" for a boat. Type \"swim\" to swim across: ").lower()
    if choice == 'wait':
        print("You've arrive at the island unharmed. There is house with 3 doors.")
        color = input("One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if color == 'yellow':
            print("You found the treasure! You Win!")
        elif color == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif color == 'red':
            print("It's a room full of fire. Game Over.")
    elif choice == 'swim':
        print("You get attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game Over")
