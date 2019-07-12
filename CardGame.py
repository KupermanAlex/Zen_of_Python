# import pygame
# import random
# from random import shuffle

# SUITS = ['heart','diamonds','spades','clubs']


# class Card :
#     def __init__(self, rank,suit):
#         self.rank = rank
#         self.suit = suit

#     def __repr__(self):
#         return (f'{self.__class__.__name__}'f'(rank={self.rank!r}, suit={self.suit!r})')

#     def __eq__(self, other):
#         if other.__class__ is not self.__class__:
#             return NotImplemented
#         return (self.rank, self.suit) == (other.rank, other.suit)
#     deck =[]       
#     deck= [(rank,suit) for rank in range(6,14) for suit in SUITS] 
    

##########################################
import random
from random import shuffle

RANKS =[ "Ace","6", "7","8", "9", "10", "Jack", "Queen", "King" ]
SUITS =[ "Clubs", "Diamonds", "Hearts", "Spades" ]


class Card:

    def __init__( self, rank, suit ):
        self.rank = rank
        self.suit = suit

    def __str__( self ):
        return self.rank + " of " + self.suit

class Deck:

    def __init__( self ):
        self.contents = []
        self.contents = [ Card( rank, suit ) for rank in RANKS for suit in SUITS ]
        random.shuffle( self.contents )
   

######################################

# import random



# suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
# deck = [(rank , s) for rank in range(6,15) for s in (suit)]




# print (random.choice(deck))
