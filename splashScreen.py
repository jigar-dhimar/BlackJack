from graphics import*
from buttonclass import * 

def splashscreen():

	############# Graphics Set up ###############
	#creates graphics window
	win = GraphWin("Blackjack!", 620,600)
	win.setBackground("black")


	#create continue button 
	continueButton = Button(win, Point(550,530), 65, 40, "Continue")
	continueButton.activate()

	#picture 
	
	img1 = Image(Point(500, 270), "playingCards/" + "s1.gif")
	img1.draw(win)
	img1 = Image(Point(410, 270), "playingCards/" + "h13.gif")
	img1.draw(win)


	############## Blackjack Explanation ################

	###### Basic explanation ########### 
	expl = Text(Point(193, 38), "How the game works")
	expl.setSize(27)
	expl.setFill("steelblue")
	expl.draw(win)
	explanationText = """ 
The aim of the game is to create a better hand than the dealer's. Create a hand with a value 
that is as close to 21 as possible, without exceeding 21. If your hand exceeds 21 you lose. If you 
have a better hand than the dealer or you have blackjack(two cards that add up to 21) you win!
	"""

	explanation = Text(Point(300,80), explanationText)
	explanation.setFace("helvetica")
	explanation.setSize(9)
	explanation.setFill("green")
	explanation.draw(win)




	####### Card value explained ######## 
	cardexpl = Text(Point(140, 150), "Card Values")
	cardexpl.setSize(27)
	cardexpl.setFill("steelblue")
	cardexpl.draw(win)

	cardexplanation = Text(Point(240, 180), "The rules of blackjack divide the cards into three categories of value:")
	cardexplanation.setFace("helvetica")
	cardexplanation.setSize(9)
	cardexplanation.setFill("green")
	cardexplanation.draw(win)

	cardList = ["Cards 2-9 hold their own value", "10/Jack/Queen/King all equal ten", "The ace may equal 11 or 1"]

	for i in range(len(cardList)):
                
		temp = Text(Point(150, 200+20*i), cardList[i])
		temp.setFill("green")
		temp.setSize(9)
		temp.setFace("helvetica")
		temp.draw(win)
	


	####### Ace explanation #########
	aceHeader = Text(Point(165, 305), "The Special Ace")
	aceHeader.setSize(26)
	aceHeader.setFill("steelblue")
	aceHeader.draw(win)


	aceHelper = """
The rules of blackjack give the ace a flexible value. It can be worth either 11 or 1. Normally, 
the ace will have a value of 11. The value of the ace changes when the player asks for an extra 
card that gives him a total value over 21. When this happens the ace's value becomes 1.
"""
	
	aceExplanation = Text(Point(300, 350), aceHelper)
	aceExplanation.setFill("green")
	aceExplanation.setFace("helvetica")
	aceExplanation.setSize(9)
	aceExplanation.draw(win)



	#gameplay options

	gameOpt = Text(Point(270, 420), "Options when the cards have been dealt")
	gameOpt.setSize(22)
	gameOpt.setFill("steelblue")
	gameOpt.draw(win)

	gameHelper = "When the cards have been dealt, and you don't have blackjack, you have the following options:"
	gameExpl = Text(Point(300, 450), gameHelper)
	gameExpl.setFill("green")
	gameExpl.setFace("helvetica")
	gameExpl.setSize(9)
	gameExpl.draw(win)


	gameList = ["Stand: You're content with your cards and you don't wish to receive any more cards.", 
				"Hit: You can ask for an extra card to increase the value of your hand."
				]

	for j in range(len(gameList)):
                
		temp = Text(Point(270, 470+20*j), gameList[j])
		temp.setFill("green")
		temp.setFace("helvetica")
		temp.setSize(9)
		temp.draw(win)





	############ Program Freeze ##################
	click = win.getMouse()


	### program will not continue to game until user clicks continue ###
	while continueButton.clicked(click) != True:

		click = win.getMouse()
		continueOn = click.getX() >= 505 and click.getX() <= 555 and click.getY() >= 505 and click.getY() <= 555

	win.close()

