def strip(hand):
  '''Removes suits from hand'''
  #new list called newHand is created that will be returned at the end
  newHand = []
  #every card in hand is searched, if statement differentiates between double digit and single digit cards (4H vs 14H).
  for card in hand:
    if len(card) == 2:
      #slice excludes last character and is added to newHand
      newCard = card[0:1]
      newHand.append(newCard)
    else:
      newCard = card[0:2]
      newHand.append(newCard)
  #newHand is returned
  return newHand

def sort(hand):
  '''Returns a sorted list of integers from an unsorted list of string or integer numbers'''
  #sortedHand is created from hand, this is the list that will be returned at the end.
  sortHand = hand[:]
  #checks to see if list is strings or not, if first item is a string all the rest will be based on rest of program
  if isinstance(sortHand[0], str):
    #for loop goes through every item and converts it into an integer
    for i in range(0, len(sortHand)):
      sortHand[i] = int(sortHand[i])
  #selection sort algorithm will loop through each value in a list and if the value before it is greater then it they swap
  for i in range(len(sortHand)):
    j = i
    while j > 0 and sortHand[j] < sortHand[j-1]:
      sortHand[j], sortHand[j-1] = sortHand[j-1], sortHand[j]
      j = j -1
  return sortHand

def onlySuits(hand):
  '''Returns only the suits of a hand'''
  #empty list is created that will be returned
  justSuits = []
  for card in hand:
  #if length is equal to 2, the second character will be added to justSuits 
    if len(card) == 2:
      new = card[1:]
      justSuits.append(new)
    #if length is greater than 2, the third character will be added to justSuits
    else: 
      new = card[2:]
      justSuits.append(new)
  return justSuits

class HandValue():
  '''Class representing the value of a player's hand '''
  
  def __init__(self, hand, table):
    '''Initilizes the HandValue class'''
    #totalHand is all table including the hand
    self.totalHand = hand + table
    #hand without the suits
    self.stripHand = strip(self.totalHand[:])
    #sorted hand of integers
    self.sortedHand = sort(self.stripHand[:])

  def fourOfKind(self):
    '''Searches for four of a kind in the hand'''
    for card in self.sortedHand:
      #if the count of any card is four inside stripHand, the integer of the card will be returned
      if self.sortedHand.count(card) == 4:
        return (card)
        
  def fullHouse(self):
    '''Searches for a full house in the hand'''
    #check will be to see whether full house is present, threecard will be for the card that has three of a kind, two card will be for the pair
    check = 0
    threeCard = 0
    twoCard = 0
    #searches every card in stripped hand
    for card in self.sortedHand:
      #if count of the card is 3, threecard is assinged to this card and 2 is added to check
      if self.sortedHand.count(card) == 3:
        check += 2
        threeCard = card
      #if count is 2, two card is assigned to the card and 2 is added to check
      elif self.sortedHand.count(card) == 2:
        check += 1
        twoCard = card
    #if check is greater than or equal to 8 (meaning there is a there is a two pair and threepair, both cards will be returned)
    if check >= 8:
      return [(threeCard), (twoCard)]
  
  def flush(self):
    '''Searches for a flush in the hand'''
    #justSuitedHand will be used to only contain the suits
    justSuitedHand = onlySuits(self.totalHand)
    #flush suit will be created to find the suit that is flushed 
    flushSuit = []
    #searches every suits count, if 5 then added to flushSUit
    for suit in justSuitedHand:
      if justSuitedHand.count(suit) >= 5:
        flushSuit.append(suit)
    #flushedHand will be for the cards that contain the flushed suit
    flushedHand = []
    if len(flushSuit) > 1: 
      #searches self.totalHand, if contains the flushSuit, it is added to flushedHand
      for card in self.totalHand:
        if flushSuit[0] in card:
          flushedHand.append(card)
      #sortedFlush strips and sorts all the flushed cards
      sortedFlush = sort(strip(flushedHand))  
      #the max of the list is returned
      return max(sortedFlush)

  def straight(self):
    '''Searches for a straight in the hand'''
    #removes any duplicates from hand, because a straight has no use for duplicated cards
    removeDup = (list(dict.fromkeys(self.sortedHand[:])))
    #this list will contained the cards that form a straight (if it can be formed)
    straight = []
    #based on the length, cetain combinations can be formed
    if len(removeDup) == 5:
      #if only 5 cards, only 1 straight can be formed
      combo1 = removeDup[0:5]
      if combo1[4] - combo1[0] == 4:
        #if the straight can be formed (the last card minus the first card is 4) it is added to the list
        #only the last card of the straight is added because thats the only thing necessary to determine the level of the straight
        straight.append(combo1[4])
    elif len(removeDup) == 6:
      #if 6 cards, two combos can be formed
      combo1 = removeDup[0:5]
      combo2 = removeDup[1:6]
      #if either combo forms a straight, theyre added to straight 
      if combo1[4] - combo1[0] == 4:
        straight.append(combo1[4])
      if combo2[4] - combo2[0] == 4:
        #straight must be reset to be blank so that only the higher straight will be returned
        straight = []
        straight.append(combo2[4])    
    elif len(removeDup) ==7:
      #if removeDup is 7 cards, 3 different straight combos are possible
      combo1 = removeDup[0:5]
      combo2 = removeDup[1:6]
      combo3 = removeDup[2:]
      #if any of the straight combos form a straight, theyre added to straight
      if combo1[4] - combo1[0] == 4:
        straight.append(combo1[4])
      if combo2[4] - combo2[0] == 4:
        #again straight needs to be reset so only higher straight is returned
        straight = []
        straight.append(combo2[4])
      if combo3[4] - combo3[0] == 4:
        straight = []
        straight.append(combo3[4])
    #if straight contains any items, its only item is returned
    if len(straight) ==1:
      return(straight[0])

  def threeOfKind(self):
    '''Searches for three of a kind in the hand '''
    #searches through sortedhand, if count of a card number if 3 then a new hand is created
    for card in self.sortedHand:
      if self.sortedHand.count(card) == 3:
        #the card that shows up 3 times will be removed from a copy of sortedhand. 
        handWithoutCard = self.sortedHand[:]
        handWithoutCard.remove(card)
        handWithoutCard.remove(card)
        handWithoutCard.remove(card)
        #the remaining highest two cards will be returned
        return int(card), int(handWithoutCard[3]), int(handWithoutCard[2])
    
  def twoPair(self):
    '''Searches for a two pair in the hand '''
    #check will contain the two pair (if its there)
    check = []
    #searches through sorted hand
    for card in self.sortedHand:
      #if a card shows up twice, it is added to check
      if self.sortedHand.count(card) == 2:
        check.append(card)
    #if hand contains two pairs, check will have 4 values
    if len(check) == 4:
      # #removes duplicates
      check = list(dict.fromkeys(check))
      #copy of sorted hand it created
      nonPairs = self.sortedHand[:]
      #removes the two pair cards
      nonPairs.remove(check[0])
      nonPairs.remove(check[1])
      nonPairs.remove(check[0])
      nonPairs.remove(check[1])
      #returns highest of the pairs first, second highest, and then the highest card outside of the two pairs
      return [(check[1]), (check[0]), (nonPairs)[2]]
    
  def pair(self):
    '''Searches for a pair in hand '''
    #searches through sorted hand
    for card in self.sortedHand:
      #searches to find if the count of a card is 2
      if self.sortedHand.count(card) == 2:
        #copy of sortedHand is made
        handWithoutPair = self.sortedHand[:]
        #card is removed twice, because occurs twice
        handWithoutPair.remove(card)
        handWithoutPair.remove(card)
        #card is returned first, then the 3 highest cards in the hand without the pair
        return (card), handWithoutPair[4], handWithoutPair[3], handWithoutPair[2]

  def getFinalScore(self):
    '''Returns final score of a hand '''
    #all the hands are in ranking order, therefore if one is fulfilled others wont be (for example, if there is a full house in a hand there is also 3 of a kind and a two pair, by having this in ranking order two pair and 3 of a kind wont be fulfilled)
    #if multiple numbers are needed in a calculation I had to divide by 10 and then 1000 and then 100000 so that numbers dont add to previous numbers added (example: 14 plus 10 should be 1410 instead of 1500)
    if self.fourOfKind():
      #highest ranking hand (in my game) has a score of 8000 plus the card that apperas 4 times
      return 8000 + self.fourOfKind()*10
    elif self.fullHouse():
      #second highest ranking hand is a full house, which is 7000 and the cards that form the full house
      return 7000 + (self.fullHouse()[0])*10 + (self.fullHouse()[1]/10)
    elif self.flush():
      #third highest hand is a flush, equal to 6000 + the highest card with that suit
      return 6000 + self.flush()*10
    elif self.straight():
      #next hand is a straight which is 5000 + its top card
      return 5000 + self.straight()*10
    elif self.threeOfKind():
      #three of a kind is next which is 4000 + plus the 3 of a kind card and the next two highest cards
      return 4000 + (self.threeOfKind()[0])*10 + (self.threeOfKind()[1])/10 + (self.threeOfKind()[2])/1000
    elif self.twoPair():
      #two pair is 3000 plus the two pair cards and the next highest card
      return 3000 + self.twoPair()[0]*10 + self.twoPair()[1]/10 + self.twoPair()[2]/1000
    elif self.pair():
      #1 pair is 2000 plus the one pair card and the next 3 highest cards
      pairReturn = self.pair()[:]
      return 2000 + pairReturn[0]*10 + pairReturn[1]/10 + pairReturn[2]/1000 + pairReturn[3]/100000
    else:
      #if no hand can be formed, 1000 plus the next 5 highest cards is the score
      return 1000 + self.sortedHand[6]*10 + self.sortedHand[5]/10 + self.sortedHand[4]/1000 + self.sortedHand[3]/100000 + self.sortedHand[2]/10000000 
      