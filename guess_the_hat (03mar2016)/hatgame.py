"""
breakdown of solution
The player at the back can see all but his own hat
He can relay information to the next player by his guess, as one mistake
can be made.
If there are an odd number of black hats, he can let the next player
know by guessing black.
Now the next player knows that if he sees an odd number of black hats,
his is white.
Else his is black.
Every time black is guessed, it switches from odd to even, or vice versa
"""

def hatgame(input):
    # get the list of hats
    loopList = getFileTxt(input).splitlines()
    hatList = getFileTxt(input).splitlines()

    # create something to keep track of black
    # every time this changes, the guess is black
    blackOdd = True
    # create a list to keep track of the guesses
    guesses = []
    # remove the first hat, as the first guess isn't based on the list
    loopList.pop(0) 

    blackHats = 0
    for hat in loopList:
        if hat == "Black":
            blackHats+=1

    if blackHats%2==1: blackOdd = True
    else: blackOdd = False
    # go through each person for their guess
    for i in xrange(len(hatList)):
        # set the black hat count to 0
        bHats=0
        # loop through the hats in front
        for hat in loopList:
            # for every black hat
            if "Black" in hat:
                # add 1 to the count
                bHats+=1

        # if black should be odd
        if blackOdd:
            # but black is even
            if bHats%2==0:
                guesses.append("Black")
                blackOdd = not blackOdd
            else:
                guesses.append("White")
        # if black should be even
        else:
            # but it is odd
            if bHats%2==1:
                guesses.append("Black")
                blackOdd = not blackOdd
            else:
                guesses.append("White")
        # remove the next guessers hat
        if len(loopList) > 0:
            loopList.pop(0)

    right = 0         
    for i in xrange(len(hatList)):
        if hatList[i] == guesses[i]:
            right+=1
             
        #print "%s guessed %s." % (hatList[i], guesses[i])
    print "%d right out of %d" % (right, len(hatList))
            

def getFileTxt(input):
    with open(input) as inputs:
        return inputs.read()

hatgame('input1.txt')
hatgame('input2.txt')
hatgame('input3.txt')
hatgame('LotOfHats.txt')

# this works, but it's quick and dirty - with more exposure to
# python, I feel I can make this much better
