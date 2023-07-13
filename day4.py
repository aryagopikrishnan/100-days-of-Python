#Day 4 - Randomization

import random

coin_side = random.randint(0,1)
if coin_side == 1:
    print("Heads")
else:
    print("Tails")

#-------------------------------------------------------
# Code 2: Random selection from a list of names

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# print(type(names))

n = len(names)
x = random.randint(0,n-1)
random_choice = names[x]
print(f"{random_choice} is the winner!")

#-----------------------------------------------------------------------------------

# Code 3: Treasure map

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])-1
row = int(position[1])-1

map[row][column] = 'X'

print(f"{row1}\n{row2}\n{row3}")

#-------------------------------------------------------------------------------

#Code 4: Rock, Paper, Scissor

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


import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

game = [rock, paper, scissors]

print(game[player_choice])
print("Computer chose: ")

computer_choice = random.randint(0,2)
print(game[computer_choice])

if computer_choice == 0 and player_choice == 1:
  print("You Win!")
elif computer_choice == 1 and player_choice == 0:
  print("You Win!")
elif computer_choice == 2 and player_choice == 0:
  print("You Win!")
elif computer_choice == player_choice:
  print("It's a draw")
else:
  print("You lose.")
