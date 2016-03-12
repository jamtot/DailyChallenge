# disecting another users solution to learn some things

def getFileTxt(input):
    with open(input) as inputs:
        return inputs.read()

def guess(input):
    input, guesses, wrong = getFileTxt(input).splitlines(), [], 0
    for i in xrange(len(input)):
        #print [(input[i + 1:] + guesses).count('White') % 2] - returns [0] or [1]
        guesses += [['Black', 'White'][(input[i + 1:] + guesses).count('White') % 2]]
        #print guesses
        wrong += input[i] != guesses[-1]
        #print input[i], 'guesses', guesses[-1]
    print wrong, 'out of', len(input), 'wrong'

guess("input1.txt")
#guess("LotOfHats.txt")
