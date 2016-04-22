from deck import *
from random import *
from graphics import *
from time import *

class BlackJack:



    def __init__ (self, wallet, dHand=[], pHand=[]):

        """constructs a Blackjack object with instance varibles for total player funds,
        and default dealer and player hand lists"""

        #instance variables
        self.dealerHand = dHand
        self.playerHand = pHand
        self.wallet = wallet


        #shuffles up the deck of the card
        self.playingDeck = Deck()
        self.playingDeck.shuffle()
        self.pHandImgList = []#list for storing imgs currently on player's side of board
        self.dHandImgList = []#^^^^^^^^^^^^^^but for dealer
        self.result = Text(Point(50,50), "none")

    def initDeal(self,gwin,xposD,yposD,xposP,yposP,initBet):

        """deals initial card objects into dealer and player hands and draws face down cards onto given
        win for the dealer and player at given X and Y positions and also sets the initial bet that the player bets."""

        #deals out initial cards, 2 per player and
        #displays dealer and player hands on graphical win
        
        self.xD = xposD#x position for dealer card
        self.yD = yposD#y position for dealer card
        self.xP = xposP#X for player card
        self.yP = yposP#Y for player card
        self.playerInc = 0 #counter for how many cards in player's gand
        self.bet = initBet #stored varible for current bet
        self.gwin = gwin # stored varible for given window
        self.wallet = self.wallet - self.bet #removes bet from players total cash amount
        self.HandValue = 0 #varible for storing the total BJValue of player's hand
        
        #for player
        for i in range(2): #for loop that draws two cards from the deck and adds them to playerhand
            #and then draws two face down cards on the player's side 
            dealtCard = self.playingDeck.dealCard()
            self.playerHand.append(dealtCard)
            
            imgfileName = "b1fv.gif"#face down card img
            img1 = Image(Point(self.xP+3*self.playerInc,self.yP-2*self.playerInc), "playingCards/" + imgfileName)
            #^^^^^^^^draws cards incrementally at given X and Y positions which vary based ons self.playerInc
            img1.draw(gwin)

            self.pHandImgList.append(img1)#adds img drawn to player img list
            self.playerInc = self.playerInc + 1#adds 1 to self.playerInc

    
            
            self.HandValue = self.HandValue + dealtCard.BJValue()#adds the BJValue of the card drawn to self.HandValue
            


        #for dealer
        self.dealerInc = 0#same as above but for dealer
        for j in range(2):
            dealtCard = self.playingDeck.dealCard()
            self.dealerHand.append(dealtCard)

            imgfileName = "b1fv.gif"
            img1 = Image(Point(self.xD+3*self.dealerInc,self.yD-2*self.dealerInc), "playingCards/" + imgfileName)
            img1.draw(gwin)

            self.dHandImgList.append(img1)
            self.dealerInc = self.dealerInc + 1

        #Wallet
        self.currentWallet = Text(Point(self.xP+40,self.yP-20),"Remaining Cash: "+str(self.wallet))#text object for
        #total amount of money that the player has left to bet with
        self.currentWallet.draw(gwin)

        #Bet
        self.currentBet = Text(Point(self.xP+40,self.yP -15),"Current Bet: "+str(self.bet))#text object for
        #current amount of money the player has bet
        self.currentBet.draw(gwin)
                             
    
    
        

    def hit(self,gwin):
        """adds a new card to the player's hand and places it at self.xP, self.yP at given win"""
        dealtCard = self.playingDeck.dealCard()#draw card from the deck
        

        imgfileName = str(dealtCard.getSuit()) + str(dealtCard.getRank()) + ".gif"#gets the img file name associated with drawnCard
        img1 = Image(Point(self.xP+3*self.playerInc,self.yP-2*self.playerInc), "playingCards/" + imgfileName)#draws card at location based on playerInc
        img1.draw(gwin)
        self.pHandImgList.append(img1)#adds drawn card's img to imgList
        self.HandValue = self.HandValue + dealtCard.BJValue() #increases self.HandValue to match player hand's new total value
        
        self.count.setText("Current Hand: "+str(self.HandValue))#changes Current hand value to match total hand Vaue
        
        self.playerInc = self.playerInc + 1

        self.playerHand.append(dealtCard)

  


    def increaseBet(self, value):
        """increases self.bet value by given value"""
        #increases the initial bet by given value
        if self.wallet < value:#if player tries to bet more than their wallet
            #bet the remainder of their wallet and set wallet to 0
            self.bet = self.bet + self.wallet
            self.wallet = 0
            self.currentBet.setText("Current Bet: "+str(self.bet))
            self.currentWallet.setText("Remaining Cash: "+str(self.wallet))
        else:#else just bet the amount given
            self.wallet = self.wallet - value
            self.bet = self.bet + value
            self.currentBet.setText("Current Bet: "+str(self.bet))
            self.currentWallet.setText("Remaining Cash: "+str(self.wallet))


    def reduceBet(self, value):
        """decreases self.bet value by given value"""
        
        if self.bet < value:#if player tries to decrease bet by larger amount than remaining bet
            #then just adds the remaining bet and sets bet to 0 and says that the player may not
            #bet lower 
            self.wallet = self.wallet + self.bet
            self.bet = 0
            self.currentBet.setText("Cannot bet any lower")
        else:#else just decreases bet value by given value
            self.wallet = self.wallet + value
            self.bet = self.bet - value
            self.currentBet.setText("Current Bet: "+str(self.bet))
            self.currentWallet.setText("Remaining Cash: "+str(self.wallet))
        
    def revealHands(self):
        """replaces the hidden card images with the appropriate image that matches the
        cards in the player and dealer hands"""
        #player reveals cards
        self.playerInc = 0
        for card in self.playerHand:#for each card in playerHand 
            turnedCard = self.pHandImgList.pop(0)#removes first card from img list and sets that as turnedCard
            turnedCard.undraw()#undraws turnedCard
            imgfileName = str(card.getSuit()) + str(card.getRank()) + ".gif"#creates imgFileName from card using .getSuit and .getRank methods
            img1 = Image(Point(self.xP+3*self.playerInc,self.yP-2*self.playerInc), "playingCards/" + imgfileName)#creates img object at location
            img1.draw(self.gwin)
            

            self.pHandImgList.append(img1)#adds image to img list
            self.playerInc = self.playerInc + 1

        self.count = Text(Point(self.xP+25,self.yP+20),"Current Hand: "+str(self.HandValue))#sets current value to total hand value at that point
        self.count.draw(self.gwin)#draws self.count

        self.dealerInc = 0
        for card in self.dealerHand[:1]:#same but for dealer and will only do it for the first card in the hand (e.g., it leaves one flipped)
            turnedCard = self.dHandImgList.pop(0)
            turnedCard.undraw()
            imgfileName = str(card.getSuit()) + str(card.getRank()) + ".gif"
            img1 = Image(Point(self.xD+3*self.dealerInc,self.yD-2*self.dealerInc), "playingCards/" + imgfileName)
            img1.draw(self.gwin)

            self.dHandImgList.append(img1)
            self.dealerInc = self.dealerInc + 1
    
    def revealSecondDealerCard(self):
        """reveales the remaining unflipped dealer card when called"""
    
        turnedCard = self.dHandImgList.pop(0)#removes the first img from img list (the last flipped card)
        turnedCard.undraw()#undraws it

        dealtCard = self.dealerHand[1]#sets dealtCard to the second card dealtCard
        
        imgfileName = str(dealtCard.getSuit()) + str(dealtCard.getRank()) + ".gif" #creates name of img for dealtCard using getSuit and getRank methods
        img1 = Image(Point(self.xD+3*self.dealerInc,self.yD-2*self.dealerInc), "playingCards/" + imgfileName)#creates img object for dealtCard
        img1.draw(self.gwin)

        self.dHandImgList.append(img1)#adds card to dealer imgList
        self.dealerInc = self.dealerInc + 1#increases the total hand size by 1


    def evalHand(self,hand):

        """finds the total of the cards in the hand that is passed in 
        and returns total (ace counts as 11 if doing so allows total 
        to stay under 21)"""

        self.total = 0 #accumulater varible
        
  
        for i in range(len(hand)):#finds the total value for the given hand
            self.total = self.total + hand[i].BJValue()

        for j in range(len(hand)):#finds if any of cards are aces and subtacts 10 fromt toal if the hand total is >21 and hand has an ace
            if hand[j].BJValue() == 11 and self.total > 21:
                self.total = self.total - 10
                if hand == self.playerHand:#if the hand is the player hand then adjusts the text object readout apropriately 
                    self.HandValue = self.HandValue - 10
                    self.count.setText("Current Hand: "+str(self.HandValue))

        return self.total #returns total value

    
    def dealerPlays(self, gwin):
        """dealer will draw cards and add them to its hand while its hand value is below 17"""
        #dealer deals cards to his or herself, stopping when hitting "soft 17"
        while self.evalHand(self.dealerHand) < 17:
            dealtCard = self.playingDeck.dealCard()
            self.dealerHand.append(dealtCard)
            
            imgfileName = str(dealtCard.getSuit()) + str(dealtCard.getRank()) + ".gif"
            img1 = Image(Point(self.xD+3*self.dealerInc,self.yD-2*self.dealerInc), "playingCards/" + imgfileName)
            img1.draw(gwin)

            self.dHandImgList.append(img1)
            

            self.dealerInc = self.dealerInc + 1
            sleep(.5)
            
        return self.evalHand(self.dealerHand)


    def getPImgObjList(self):
        """returns list of player img Objects current in the list"""
        return self.pHandImgList

    def getDImgObjList(self):
        """returns list of dealer img Objects current in its list"""
        return self.dHandImgList
    
    def resetResult(self):
        """returns the text object message that tells the player who won"""
        return self.result
    
    def clearHands(self):
        self.playerHand = []
        self.dealerHand = []
        dHand = []
        pHand = []
        

    def playerBlackjack(self, win):
        """prints a message that the player has won and adds the apropriate funds to player wallet and sets bet to 0"""
        self.result = Text(Point(50,50), "Blackjack! Player wins!")
        self.result.draw(win)
        self.wallet = self.wallet + (self.bet*1.5)
        self.bet = 0
        self.currentBet.setText("Current Bet: "+str(self.bet))
        self.currentWallet.setText("Remaining Cash: "+str(self.wallet))


    def dealerBlackjack(self, win):
        """prints that the dealer has won and sets the bet to 0"""
        
        self.result = Text(Point(50,50), "Blackjack! Dealer wins!")
        self.result.draw(win)
        self.bet = 0
        self.currentBet.setText("Current Bet: "+str(self.bet))
        self.currentWallet.setText("Remaining Cash: "+str(self.wallet))
        
    def dealerwin(self, gwin):
        """ prints that a message that the dealer has won and sets bet to 0"""

        self.result = Text(Point(50,50), "The Dealer has won the round.")
        self.result.draw(gwin)
        self.bet = 0
        self.currentBet.setText("Current Bet: "+str(self.bet))
        self.currentWallet.setText("Remaining Cash: "+str(self.wallet))
    

    def playerwin(self, gwin):

        """ prints a message that the player has won and adds the apropriate funds to the player wallet and sets bet to 0 """

        self.result = Text(Point(50,50), "You have won the round.")
        self.result.draw(gwin)
        self.wallet = self.wallet + (2*self.bet)
        self.bet = 0
        self.currentBet.setText("Current Bet: "+str(self.bet))
        self.currentWallet.setText("Remaining Cash: "+str(self.wallet))


    def dealerBust(self, gwin):
        """prints a message that the dealer busted and adds the apropriate funds to the player wallet and sets bet to 0"""
        
        self.result = Text(Point(50,50), "Dealer Bust! You win!")
        self.result.draw(gwin)
        self.wallet = self.wallet + (2*self.bet)
        self.bet = 0
        self.currentBet.setText("Current Bet: "+str(self.bet))
        self.currentWallet.setText("Remaining Cash: "+str(self.wallet))

    def playerBust(self, gwin):
        """prints a message that the palyer busted and sets the current bet to 0"""
        
        self.result = Text(Point(50,50), "Player Bust! You Lose!")
        self.result.draw(gwin)
        self.bet = 0
        self.currentBet.setText("Current Bet: "+str(self.bet))
        

    def tie(self, gwin):
        """prints a message that the player and dealer have tied and returns the current bet to the player wallet"""
    
        self.result = Text(Point(50,50), "The round ends in a push.")
        self.result.draw(gwin)
        self.wallet = self.wallet + self.bet
        self.bet = 0
        self.currentBet.setText("Current Bet: "+str(self.bet))
        self.currentWallet.setText("Remaining Cash: "+str(self.wallet))


