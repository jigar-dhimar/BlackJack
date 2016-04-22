#Playing Card Class


class PlayingCard:


    def __init__(self, rank, suit):

        """Constructs a card object given a rank (an int 1-13) and
        a suite 'd','c', 'h' or 's' which corrispond to diamonds, clubs, hearts and spades"""
        
        #instance variables
        self.suit = suit
        self.rank = rank

    def getRank(self):
        """Returns the rank of the card"""
        return self.rank

    def getSuit(self):
        """Returns the suite of the given card"""
        return self.suit

    def BJValue(self):
        """Determines and then returns the value of the card in BlackJack"""
        
        #face cards 
        if self.rank > 10:
            return 10
        
        #aces
        elif self.rank == 1:
            return 11

        #not a face card or ace 
        #returns its own value
        return self.rank

    def __str__(self):
        """Will return the full name of the given card when called"""
        
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        suits ={'d':'of Diamonds', 'c':'of Clubs', 'h':'of Hearts', 's':'of Spades'}
        
        #returns string of card by getting the suit and rank from the list 
        name = ranks[self.rank-1] + " " + suits[self.suit]
        return name



    
