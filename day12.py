# Number Guessing Game

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
correct_answer = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

while attempts>0:
    guess = int(input("Make a guess: "))
    if guess == correct_answer:
        print(f"You got it! The answer was {correct_answer}.")
        break
    elif guess > correct_answer:
        print("Too high.")
        attempts-=1
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess < correct_answer:
        print("Too low.")
        attempts-=1
        print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts==0:
        print("You've run out of guesses, you lose.")
        break

