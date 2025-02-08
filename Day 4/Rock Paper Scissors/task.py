import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
selection = [rock,paper,scissors]
player_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player_selection = selection[player_selection]
computer_selection = random.choice(selection)
print(player_selection,"\n")
print("Computer Choose:\n",computer_selection)




if player_selection == rock and computer_selection == scissors:
    print("You Win.")
elif player_selection == paper and computer_selection == rock:
    print("You Win.")
elif player_selection == scissors and computer_selection == paper:
    print("You Win.")
elif computer_selection == player_selection:
    print("It's a draw.")
else:
    print("You Loose.")