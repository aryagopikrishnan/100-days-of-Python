# Hangman Game

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f"the word is {chosen_word}")
display = []


num_letters = len(chosen_word)
for i in range(num_letters):
    display.append("_")
print(display)


def game():
    
        
        num_lives = 6
        while num_lives > 0:


            guess = input("Guess a letter: ").lower()


            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
                
            if letter != guess:
                num_lives -=1
                      
            print(display)
            print(f"Lives left: {num_lives}")
            if "_" not in display:
                print("You Win.")
                
            
game()

  
            









