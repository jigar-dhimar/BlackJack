
#Deck Class

from playingcard import *
from random import *

class Deck():

    def __init__(self, cardList = []):
        
        """Creates an empty list 'cardList', 52 playingCard objects and stores those
            objects inside the list with the correct suites and numbers of a deck of playing
            cards."""
            
        suites = ['d', 'c', 'h', 's']
        self.cardList = cardList
        
        #nested for loop creates a 
        #deck of 52 card objects in a list 
        for s in suites:
            for r in range(1,14):
                card = PlayingCard(r,s)
                self.cardList.append(card)
        

    def shuffle(self):
        """Shuffles cardList so that the card objects are in a completely new order"""
        
        for shuffle in range(1000):

            #pops out a random card in list
            #assigns it to a variable 
            card = self.cardList.pop(randrange(0,52))     

            #that card is randomly inserted somewhere                               
            self.cardList.insert(randrange(0,52), card)

            #this repeats 1000-1 times 
    
    def dealCard(self):
        """Removes the first card from the deck and returns it"""
        return self.cardList.pop(0)

    def cardsLeft(self):
        """Returns the remaining cards in the deck as a string literal"""
        return len(self.cardList)

        
        
    
    
