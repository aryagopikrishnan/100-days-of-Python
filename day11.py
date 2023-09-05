# Blackjack Capstone project

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.



## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#START 


# USER AND COMPUTER GETS 2 RANDOM CARDS EACH
# USER AND COMPUETR CARD NUMBERS TO BE ADDED UP
# IF STATEMENT: 

import random

def card_deal():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

user_card=[]
computer_card = []
game_over = False

for _ in range(0,2):
    user_card.append(card_deal())
    computer_card.append(card_deal())


user_score = calculate_score(user_card)
computer_score = calculate_score(computer_card)


print(f"Your cards: {user_card}, current score: {user_score}")
print(f"Computer's first card: {computer_card[0]}")
if user_score==0 or computer_score==0 or user_score>21:
    game_over=True





