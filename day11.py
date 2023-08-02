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

