import random

class Hand():
  '''Class that creates a hand and holds its instance variables'''
  def __init__(self,name):
    #creates the name of the player from parameter
    self.name = name
    #hand is initially empty
    self.hand = []
    #each player starts with 100 chips
    self.chips = 100
    #this is the full deck
    self.deck = ['2H', '2S', '2C', '2D', '3H', '3S', '3C', '3D', '4H', '4S', '4C', '4D', '5H', '5S', '5C', '5D', '6H', '6S', '6C', '6D', '7H', '7S', '7C', '7D', '8H', '8S', '8C', '8D', '9H', '9S', '9C', '9D', '10H', '10S', '10C', '10D', '11H', '11S', '11C', '11D', '12H', '12S', '12C', '12D', '13H', '13S', '13C', '13D', '14H', '14S', '14C', '14D']

  def makeHand (self):
    #draws a random integer
    cardNum = random.randint(0,51) 
    #sets firstCard to the randomly generated card in the deck
    firstCard = self.deck[cardNum]
    #samecard will be used to see if the two cards are the same
    sameCard = True
    while sameCard == True:
      #generates new number, if equal to firstCard number then while loop continues
      cardNum2 = random.randint(0,51)
      if cardNum2 == cardNum:
        sameCard = True
      #if different cards, while loop breaks
      else:
        sameCard = False
    #second card is created through cardNum2
    secondCard = self.deck[cardNum2]
    #both first and second card are added to players hand
    self.hand.append(firstCard)
    self.hand.append(secondCard)

  def clearHand(self):
    '''Clears a player's hand'''
    self.hand = []
 
  def validBet(self, bet):
    '''Checks if a player's bet is valid'''
    #returns True if bet is valid, returns False is not
    if self.chips < bet:
      return False
    else:
      return True
