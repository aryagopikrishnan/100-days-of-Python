# Hangman Game

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"the word is {chosen_word}")
display = []

num_letters = len(chosen_word)
for i in range(num_letters):
    display.append("_")
print(display)

guess = input("Guess a letter: ").lower()


for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        

print(display)




