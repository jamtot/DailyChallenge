input1="""14
Circle,4
Circle,5
Circle,6
Bamboo,1
Bamboo,2
Bamboo,3
Character,2
Character,2
Character,2
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9"""

input2="""14
Circle,4
Bamboo,1
Circle,5
Bamboo,2
Character,2
Bamboo,3
Character,2
Circle,6
Character,2
Circle,1
Bamboo,8
Circle,1
Bamboo,7
Bamboo,9"""

input3="""14
Circle,4
Circle,5
Circle,6
Circle,4
Circle,5
Circle,6
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9
Circle,4
Circle,5
Circle,6"""

input4="""14
Circle, 1
Circle, 1
Circle, 1
Circle, 2
Circle, 3
Circle, 4
Bamboo, 1
Bamboo, 2
Bamboo, 3
Bamboo, 3
Bamboo, 3
Bamboo, 3
Bamboo, 4
Bamboo, 5"""

from copy import deepcopy

# pair - two same suit tiles, with same value
# set - three same suit tiles, with same value
# sequence - three tiles same suit, imcrementing in value
#
# bonus: quad - 4 of the same suit and value, will be 1 more than 
#        normal hand of 14 per quad, but has to only have 1 pair

def hand_sorter(input):
    from collections import defaultdict
    hand = input.splitlines()
    c_num = int(hand.pop(0))
    #cards = sorted([x.split(",") for x in hands[:c_num]])
    cards=defaultdict(list)
    for suit, value in map(lambda x: str.split(x, ","),hand[:c_num]):
        cards[suit].append(int(value))
    # check card against next card, if equal or incremented, check next
    # when pair, set or seq found, remove and add to count or something

    # check for a sequence first
    print cards  
    if checkychecky(cards):
            print "Hand is good!"
    else: print "This check is not so good."
        

def checkychecky(cards):
    
    card_copy = deepcopy(cards)
    suits_involved=len(card_copy)
    for suit in card_copy:
        if c1(card_copy, suit)==0 or c2(card_copy,suit)==0 or c3(card_copy,suit)==0 or c4(card_copy, suit)==0 or c5(card_copy,suit)==0 or c6(card_copy,suit)==0:
            suits_involved-=1
    if suits_involved==0: return True
    else: return False
            
    
def c1(cards,suit):
    #print "CHECK-1"
    cardoncopy = deepcopy(cards)
    length=0
    #for suit in cardoncopy:
    check_pair(cardoncopy, suit)#0  
    check_set(cardoncopy, suit)#1
    check_seq(cardoncopy, suit)#2
    length+=len(cardoncopy[suit])
    #print "LENGTH:",length
    return length

def c2(cards,suit): 
    #print "CHECK-2"
    cardoncopy = deepcopy(cards)
    length=0 
    #for suit in cardoncopy:
    check_pair(cardoncopy, suit)#0
    check_seq(cardoncopy, suit)#2
    check_set(cardoncopy, suit)#1 
    length+=len(cardoncopy[suit])
    #print "LENGTH:",length
    return length

def c3(cards,suit):
    #print "CHECK-3"
    cardoncopy = deepcopy(cards)
    length=0
    #for suit in cardoncopy: 
    check_set(cardoncopy, suit)#1
    check_pair(cardoncopy, suit)#0
    check_seq(cardoncopy, suit)#2
    length+=len(cardoncopy[suit])
    #print "LENGTH:",length
    return length
           
def c4(cards,suit):
    #print "CHECK-4"
    cardoncopy = deepcopy(cards)
    length=0
    #for suit in cardoncopy:
    check_set(cardoncopy, suit)#1
    check_seq(cardoncopy, suit)#2
    check_pair(cardoncopy, suit)#0
    length+=len(cardoncopy[suit])
    #print "LENGTH:",length
    return length

def c5(cards,suit): 
    #print "CHECK-5"
    cardoncopy = deepcopy(cards) 
    length=0
    #for suit in cardoncopy:
    check_seq(cardoncopy, suit)#2
    check_pair(cardoncopy, suit)#0
    check_set(cardoncopy, suit)#1
    length+=len(cardoncopy[suit])
    #print "LENGTH:",length
    return length

def c6(cards,suit):
    #print "CHECK-6"
    cardoncopy = deepcopy(cards)
    length=0
    #for suit in cardoncopy: 
    check_seq(cardoncopy, suit)#2
    check_set(cardoncopy, suit)#1
    check_pair(cardoncopy, suit)#0
    length+=len(cardoncopy[suit])
    #print "LENGTH:",length
    return length

def check_pair(cards, suit):
    i = 0
    while i < len(cards[suit]):
        for j in xrange(len(cards[suit])):
            if (i!=j) and cards[suit][i]!=[]:
                if cards[suit][i] == cards[suit][j]:
                    #print "removing pair",cards[suit][i],cards[suit][j]
                    if j>i: j-=1
                    del cards[suit][i]
                    del cards[suit][j]
                    i=0
                    break
        i+=1
    return cards       
    

def check_set(cards, suit):
    i = 0
    while i < len(cards[suit]):
        breaking=False
        for j in xrange(len(cards[suit])):
            if (i!=j) and cards[suit][i]!=[]:
                if cards[suit][i] == cards[suit][j]:
                    for k in xrange(len(cards[suit])):
                        if (k!=i) and (k!=j):
                            if cards[suit][i] == cards[suit][k]:
                                #print "removing set",cards[suit][i],cards[suit][j],cards[suit][k]
                                if j>i: j-=1
                                if k>i: k-=1
                                if k>j: k-=1
                                del cards[suit][i]
                                del cards[suit][j]
                                del cards[suit][k]
                                breaking=True
                                i=0
                                break
            if breaking: break
        i+=1
    return cards 

def check_seq(cards, suit):
    i = 0
    #breaking=False
    while i < len(cards[suit]):
        breaking=False
        if cards[suit][i]!=[]:
            for j in xrange(len(cards[suit])):
                if cards[suit][j]!=[]:
                    if int(cards[suit][i])-int(cards[suit][j])==1:
                        for k in xrange(len(cards[suit])):
                            if cards[suit][k]!=[]:
                                if int(cards[suit][i])-int(cards[suit][k])==2:
                                    #print "removing seq",cards[suit][i],cards[suit][j],cards[suit][k]
                                    if j>i: j-=1
                                    if k>i: k-=1
                                    if k>j: k-=1
                                    del cards[suit][i]
                                    del cards[suit][j]
                                    del cards[suit][k]
                                    i=0
                                    breaking=True
                                    break
                    if breaking: break
        i+=1
    return cards 

hand_sorter(input1)
hand_sorter(input2)    
hand_sorter(input3)
hand_sorter(input4)




