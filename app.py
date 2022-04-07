from card import *
from hand import *


def isCardValid(card):

    if (not isinstance(card, Card)):
        return False

    suit = card.suit
    value = card.value

    validSuits = ['C', 'D', 'H', 'S']
    validValue = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    if (suit not in validSuits):
        return False

    if (value not in validValue):
        return False

# print(card.integerValue)

    return True


def isHandValid(hand):
    if (not isinstance(hand, Hand)):
        return False

    cards = hand.cards

    if (len(cards) != 5):
        return False

    cards = list(set(cards)) # Removing potential duplicates

    if (len(cards) != 5):
        return False

    for card in cards:
        if(not isCardValid(card)):
            return False

    return True
    
# def sortHand(hand):
