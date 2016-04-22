#Jason and Jigar
#COM110


#BlackJack


from buttonclass import *
from blackjack import *
from time import *	
from splashScreen import*


gamesPlayed = 1


def playBlackJack(win,wallet):





    ##################### Initial Game Setup #########################

    #global variable to hold
    #the number of games played
    global gamesPlayed

    
    ##### How many gmaes played thus far check #####

    #if this is not the first game
    if gamesPlayed > 1:

        #create new instance of blackJack class
        blkjk = BlackJack(wallet)

        #delete the cards from previous game
        blkjk.clearHands()

        #deal new cards
        blkjk.initDeal(win,45,75,45,25,10)
    

    #this is the first game played    
    else:
        blkjk = BlackJack(wallet)
        blkjk.initDeal(win,45,75,45,25,10)

    ##################### ----------------- #########################
  







    ############# Initial Graphics Setup ####################

    #creat buttons 
    hitButton = Button(win, Point(20,40),15,10,"Hit!")
    stayButton = Button(win, Point(20,30),15,10,"Stay.")
    QuitButton = Button(win, Point(80,20),15,10,"Quit.")
    playAgainButton = Button(win, Point(80,30), 15,10, "Play\nAgain")
    IncBetButton = Button(win, Point(20,15),17,4,"Increase Bet")
    DecBetButton = Button(win, Point(20,10),17,4,"Decrease Bet")
    stayBetButton = Button(win, Point(20,5), 17,4, "Set Bet")

    #activate approproate buttons 
    DecBetButton.activate()
    IncBetButton.activate()
    stayBetButton.activate()
    QuitButton.activate()

    ############# ----------------------- ####################








    ############## Betting Component of Game ##################
    if gamesPlayed == 1:
        note = Text(Point(35,90), "The game will not start until you click the Set Bet button.")
        note.setSize(15)
        note.draw(win)

    #program freeze 
    pt = win.getMouse()

    #user can bet until they press stay
    while stayBetButton.clicked(pt) != True:

        #decrease bet amount by ten 
        if DecBetButton.clicked(pt):
            blkjk.reduceBet(10)

        #increase bet amount by ten 
        elif IncBetButton.clicked(pt):
            blkjk.increaseBet(10)

        elif QuitButton.clicked(pt):
            win.close()

        #freeze program again 
        pt = win.getMouse()

     ############## --------------------------- ##################








    ################### Actual Game Play #######################
    if gamesPlayed == 1:

        #deactivate bet buttons
        note.undraw() 
    
    IncBetButton.deactivate()
    DecBetButton.deactivate()
    stayBetButton.deactivate()

    #reveal hands 
    blkjk.revealHands()

    #activate game buttons 
    hitButton.activate()
    stayButton.activate()
    playAgainButton.deactivate()


    #boolean variable that is only
    #activated once the user has 
    #clicked the stay button 
    end = False
    

    #evaluates both hands
    pHand = blkjk.evalHand(blkjk.playerHand)
    dHand = blkjk.evalHand(blkjk.dealerHand)
    
   
    #user can hit while the their hand total is
    #less than 21, and they have not yet hit stay
    while pHand < 21 and dHand < 21 and end != True:
        
        pt = win.getMouse()

        #user gets a card
        if hitButton.clicked(pt):
            blkjk.hit(win)

        #user chooses to quit
        if QuitButton.clicked(pt):
            win.close()
            
        
        #user stays
        if stayButton.clicked(pt):
            blkjk.revealSecondDealerCard()
            dHand = blkjk.dealerPlays(win)
            end = True
        
        #continual evaluation of hand totals for both 
        pHand = blkjk.evalHand(blkjk.playerHand)
        dHand = blkjk.evalHand(blkjk.dealerHand)    
            
    ################### ---------------- #######################
    








    ##################### Post Game #########################
    
    #deactivates game buttons
    hitButton.deactivate()
    stayButton.deactivate()

    ## Evaluating the game post play ##

    #dealer and player have 21
    if pHand == 21 and dHand==21:
        blkjk.tie(win)
    
    #player has 21
    elif pHand == 21 and dHand != 21:
        #player has blackjack
        if len(blkjk.playerHand) == 2:
            blkjk.playerBlackjack(win)
        else:
            #player wins 
            blkjk.playerwin(win)
    
    #dealer has 21
    elif dHand == 21 and pHand != 21:
        
        #dealer has blackjack
        if len(blkjk.dealerHand) == 2:
            blkjk.revealSecondDealerCard()
            blkjk.dealerBlackjack(win)
        else:
            #dealer wins 
            blkjk.dealerwin(win)
    
    #dealer busts player doesnt 
    elif pHand < 21 and dHand > 21:
        blkjk.dealerBust(win)
    
    #player busts dealer doesnt 
    elif pHand > 21 and dHand < 21:
        blkjk.playerBust(win)
    
    #both the player and the dealer bust
    elif dHand < 21 and pHand < 21:
        if dHand > pHand:
            blkjk.dealerwin(win)
        elif pHand > dHand:
            blkjk.playerwin(win)
        else:
            blkjk.tie(win)

    ##################### --------- #########################

   





    #################### Post Play #######################
    

    ##### Program Freeze ######### 
    ##### Activate PlayAgain Button #####
    playAgainButton.activate()
    pt = win.getMouse()
    

   
   

    #user can continue to click anywhere 
    #besides the quit and playAgain buttons
    #loop breaks when user has clicked either button
    while playAgainButton.clicked(pt) != True  and QuitButton.clicked(pt) !=True:
        pt = win.getMouse()
    

    #user clicked quit button 
    if QuitButton.clicked(pt) == True:
        win.close()

    #user clicked playagain button     
    elif playAgainButton.clicked(pt) == True:
        
        ####### Undrawing the cards ###########

        #two method calls below return two lists
        #(one for the dealer and one for the player) 
        #of all the cards image objects that 
        #have been drawn to the screen 
        undrawListP = blkjk.getPImgObjList()
        undrawListD = blkjk.getDImgObjList()
        
    
        #goes through each of the lists and 
        #undraws each of the image objects  
        for i in range(len(undrawListP)):
            undrawListP[i].undraw()
        for j in range(len(undrawListD)):
            undrawListD[j].undraw()


        #gets the text object that 
        #tells the user who won and lost
        #and then undraws it from the screen 
        text = blkjk.resetResult()
        text.undraw()
        
        #increments the counter 
        gamesPlayed = gamesPlayed + 1

        #recursive call to go back 
        #and play again
        blkjk.currentWallet.undraw()
        blkjk.currentBet.undraw()
        blkjk.count.undraw()
        playBlackJack(win,blkjk.wallet)


def main():


    ########## Explanation + Intro + Game screen #############

    #### game explanation ###
    splashscreen()   

    ### Intro Screen ###
    win = GraphWin("BlackJack",600,600)
    win.setBackground("green")
    win.setCoords(0,0,100,100)

    Title = Text(Point(50,75),"Black Jack")
    Title.draw(win)
    Title.setSize(60)
    Title.setStyle('bold')
    WrittenBy = Text(Point(50,50),"Made by Jigar Dhimar and Jason Karos")
    WrittenBy.draw(win)

    GoButton = Button(win, Point(50,60), 18, 10, "Go!")
    GoButton.activate()
    pt = win.getMouse()
    while GoButton.clicked(pt) != True:
        pt = win.getMouse()
    Title.undraw()
    WrittenBy.undraw()
    GoButton.undraw()

    ### Method Call to Play Game ###
    wallet = 100 
    playBlackJack(win,wallet)


if __name__ == "__main__":
    main()
