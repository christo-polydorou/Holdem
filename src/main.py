#TexasHold'em game
#Abby Ignasiak and Christo Polydorou 

import random
from HandValue import *
from Hand import *

def roundBet(player1, player2):
  '''Creates a round of betting between two players'''
  #first bet need a while loop, so validP1 bet is set to false
  validP1Bet = False
  #player1 will bet first
  print(player1.name, 'you will be betting first')
  while validP1Bet == False:
    #asks first player how much they would like to bet
    firstBet = int(input('How much would you like to bet (0 for no bet): '))
    print('\n')
    #checks to see if players bet is valid, if not valid it will repeat while loop
    if player1.validBet(firstBet) == False:
      print('You do not have enough chips for this bet, you only have', player1.chips, 'chips')
      validP1Bet = False
    #if its a valid bet, while loop breaks
    else:
      validP1Bet = True
  #first set of possibilities is if firstBet is 0
  if firstBet == 0:
    print(player2.name,',' ,player1.name, 'did not bet')
    #creates while loop to see if second bet is valid
    validP2Bet = False
    while validP2Bet == False:
      secondBet = int(input('How much would you like to bet?(0 for no bet): '))
      print('\n')
      #if not valid, while loop repeats
      if player2.validBet(secondBet) == False:
        print('You do not have enough chips for this bet, you only have', player1.chips, 'chips')
        validP1Bet = False
      #otherwise, loop is broken
      else:
        validP2Bet = True
    #if second bet it 0, nothing was put into the pot so 0 is returned
    if secondBet == 0:
      return 0
    else:
      #if the second player bets, first player will have to respond
      #while loop created to see if the first player's match bet it valid
      validMatchBet = False
      while validMatchBet == False:
        print(player1.name, ',' ,player2.name,'has bet', secondBet)
        matchBet = int(input('Will you match this bet or fold? (0 for fold):'))
        #if matchbet is equal to second bet, each player loses the chips they bet and the total sum is returned to be added to the pot
        if matchBet == secondBet:
          player1.chips = player1.chips-matchBet
          player1.chips = player1.chips-secondBet
          return matchBet + secondBet
        #if matchbet is less than second bet but is equal to the rest of player1's (player who gives matchbet) total chips than player1's chips are 0 and player2 only loses the matchbet
        elif matchBet < secondBet and matchBet == player1.chips:
          player1.chips = 0
          player2.chips = player2.chips - secondBet
          #secondbet and matchbet are returned 
          return secondBet + matchBet
        elif matchBet == 0:
          #if matchbet is 0, player1 folded which is represented by the returned -1
          return -1
        else:
          #if none of the conditons are met, it is an invalid bet
          print('This is an invalid bet, try again', '\n')
  #the rest of this function is if player1 did bet
  else:
    #player2 has the option to fold, raise, or call (match) the bet
    #variables are created for valid bet and to see if it is a raiseBet
    raiseBet = False
    validP2Bet = False
    print(player2.name,',', player1.name, 'has bet', firstBet, 'chips')
    while validP2Bet == False:
      #second bet1 is the responding bet to the  firstbet if its not 0
      secondBet = int(input('Will you match this bet, fold or raise?: '))
      print('\n')
      #if secondBet1 is 0, -2 is returned which means player2 folded
      if secondBet == 0:
        return -2
      #if the secondbet isn't valid, while loop repeats
      elif player1.validBet(secondBet) == False:
          print('You do not have enough chips for this bet, you only have', player2.chips, 'chips')
          validP2Bet = False
      #if secondbet is equal to firstbet then each player will lose the chips they bet and the total chips will be returned
      elif secondBet == firstBet:
        player1.chips = player1.chips-firstBet
        player2.chips = player2.chips-secondBet
        return firstBet + secondBet
      elif secondBet < firstBet:
          #if secondbet is less than firstbet but equal to player2's chips, each player has secondbet subtracted from their chips and secondbet*2 is returned
          if player2.chips == secondBet:
            player1.chips = player1.chips - secondBet
            player2.chips = player2.chips - secondBet
            return secondBet*2
          #if secondbet is less than firstbet but not equal to player2's chips, it is an invalid bet
          else:
            print('This is an invalid bet, try again')
            validP2Bet = False
      elif secondBet > firstBet:
        #if secondbet is 10 more than firstbet it a valid raise
        if firstBet + 10 == secondBet:
          validP2Bet = True
          raiseBet = True
        else:
          #if its not 10 more than the firstbet it is not a valid raise
          print('This is an invalid raise, try again')
          validP2Bet = False 
    #this if statement runs if player2 raised player1
    if raiseBet == True:
      print(player1.name, ',', player2.name, 'has raised you 10 chips')
      #while loop will be created to check wheter the response to the raise is valid
      validRaiseCall = False
      while validRaiseCall == False:
        raiseCall = int(input('Enter 10 (or rest of chips) to call, or 0 to fold: '))
        #if raisecall is 10 then it is a valid raise call and each player will lose what is equal to the secondbet. secondbet times 2 is returned
        if raiseCall == 10:
          player1.chips = player1.chips-secondBet
          player2.chips = player2.chips-secondBet
          return secondBet *2
        #if raisecall is greater than 10 it is not a valid raise call and loop will repeat
        elif raiseCall > 10:
          print('This is not a valid call, try again')
          validRaiseCall = False
        elif raiseCall <10:
          #if raisecall is equal to the rest of player2's chips, it is valid
          if raiseCall+firstBet == player2.chips:
            #each player will lose the secondbet plus the call. 2 times the secondBet and raiseCall will be returned
            player1.chips = player1.chips - (secondBet + raiseCall)
            player2.chips = player1.chips - (secondBet + raiseCall)
            return (secondBet + raiseCall)*2
          else: 
            #if not equal to rest of player1's chips, player1 loses there firstbet and player2 gains the bet. -1 is returned to show that player1 folded
            player1.chips = player1.chips - firstBet
            player2.chips = player2.chips + firstBet
            return -1

def makeTable(player1, player2, deck):
  '''Creates table given two players cards'''
  #newDeck is created as a copy of inputed deck. Deck is inputed in order to reduce repetition from Hand class
  newDeck = deck[:]
  #removes each players cards from deck
  for i in player1:
    newDeck.remove(i)
  for j in player2:
    newDeck.remove(j)
  #return table is the table that will be returned
  returnTable = []
  #loop runs 5 times to create 5 cards
  for i in range(5):
    #card is created from random int, since the list newDeck is getting smaller, range for random int must get smaller
    card = random.randint(0, 47-i)
    #card is added to returnTable
    returnTable.append(newDeck[card])
    #card is removed from newDeck
    newDeck.remove(newDeck[card])
  return returnTable

def main():
  '''Runs the game'''
  
  print('Welcome to texas holdem!', '\n')
  print('You will both start will 100 chips')
  #each player inputs their name
  player1 = input('Enter the name of player 1: ')
  player2 = input('Enter the name of player 2: ')
  print('\n')
  #object is created in Hand class for each player
  p1 = Hand(player1)
  p2 = Hand(player2)
  #Empty deck will be for if a player runs out of chips
  emptyDeck = False
  #loops runs until someones deck is empty
  while emptyDeck == False:
    pot = 0
    #clears player1's hand
    p1.clearHand()
    #creates hand for player1
    p1.makeHand()
    #loop created to make sure player1 and player2 do not have the same hand
    sameHand = True
    while sameHand == True:
      #clears player2's hand
      p2.clearHand()
      #makes player2's hand
      p2.makeHand()
      #counter for if they have same hand
      sameCounter = 0
      #if they share a card, sameCounter is increased by one
      for card in p1.hand:
        for card2 in p2.hand:
          if card == card2:
            sameCounter += 1
      #if sameCounter is less than 1 the loop breaks
      if sameCounter <1:
        sameHand = False
      #otherwise the loop repeats
      else:
        sameHand = True
    #table is created 
    tableCards = makeTable(p1.hand,p2.hand, p1.deck)
    #each player is shown their cards
    print(p1.name,',', 'Your cards are', p1.hand[0], 'and', p1.hand[1], '\n')
    print(p2.name,',', 'Your cards are', p2.hand[0], 'and', p2.hand[1], '\n')
    #first 3 cards are displayed
    print('The table is', tableCards[0], tableCards[1], tableCards[2], '\n')
    #first round of betting is initiated
    firstBetRound = (roundBet(p1,p2))
    #checks to see if either player folded 
    if firstBetRound == -1:
      #if player1 folded, player2 wins the pot (the pot is empty at this point but it is helpful to see that the pot is added to someones hand after the hand is over)
      print(player1, 'has folded his hand,', player2, 'you win the pot', '\n' )
      p2.chips = p2.chips + pot
    elif firstBetRound == -2:
      #if player2 folded, pot is added to player1's hand
      print(player2, 'has folded his hand,', player1, 'you win the pot', '\n')
      p1.chips = p1.chips + pot
    else:
      #if no one folded then what was returned in firstBetRound is added to the pot
      pot += firstBetRound
      #4th card is shown
      print('The table is now',tableCards[0], tableCards[1], tableCards[2], tableCards[3], '\n')
      #second round of betting is initiated
      secondBetRound = (roundBet(p1,p2))
      #Again a check is created to see if a player folded, same concept as the check earlier
      if secondBetRound == -1:
        print(player1, 'has folded his hand,', player2, 'you win the pot', '\n' )
        p2.chips = p2.chips + pot
      elif secondBetRound == -2:
        print(player2, 'has folded his hand,', player1, 'you win the pot', '\n')
        p1.chips = p1.chips + pot
      #if no one folded the next sequence is initiated
      else:
        #secondBetRound is added to the pot
        pot += secondBetRound
        #last card is revealed
        print('The table is now',tableCards[0], tableCards[1], tableCards[2], tableCards[3], tableCards[4], '\n')
        #third round of betting is initiated
        thirdBetRound = (roundBet(p1,p2))
        #checks to see if anyone folded
        if thirdBetRound == -1:
          print(player1, 'has folded his hand,', player2, 'you win the pot', '\n' )
          p2.chips = p2.chips + pot
        elif thirdBetRound == -2:
          print(player2, 'has folded his hand,', player1, 'you win the pot', '\n')
          p1.chips = p1.chips + pot
        else:
          #if no one has folded thirdBetRound is added to the pot
          pot += thirdBetRound
          #Object in HandValue is created for each player
          p1Score = HandValue(p1.hand,tableCards)
          p2Score = HandValue(p2.hand,tableCards)
          #if player1's final score is higher than player2's, player1 wins the pot
          if p1Score.getFinalScore() > p2Score.getFinalScore():
            p1.chips = p1.chips + pot
            print(p1.name, 'has won the hand!')
            print(p1.name, ',', 'you win', pot//2, 'chips', 'from', p2.name, '\n' )
          #if player2's final score is higher than player1's, player2 wins the pot
          elif p2Score.getFinalScore() > p1Score.getFinalScore():
            p2.chips = p2.chips + pot
            print(p2.name, 'has won the hand!')
            print(p2.name, ',', 'you win', pot//2, 'chips', 'from', p1.name, '\n')
          #if they have the same hand they split the pot
          else:
            print('You both have the same hand, you both get your money back','\n')
            pot = pot//2
            p1.chips = p1.chips + pot
            p2.chips = p2.chips + pot
    #checks to see if either players chip stack is empty
    #if either player's chip stack is empty, the loop will end
    if p1.chips == 0:
      emptyDeck = True
      print( p1.name, 'has ran out of chips, the game is over')
    elif p2.chips == 0:
      emptyDeck = True
      print(p2.name, 'has ran out of chips, the game is over' )

main()