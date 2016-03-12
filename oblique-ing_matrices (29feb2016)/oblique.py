from collections import defaultdict

def oblique(inputFile):
    # resizeable container
    output = defaultdict(list)
    with open(inputFile) as matrixFile:
        matrixTxt = matrixFile.read()
        splitrix = map(str.split, matrixTxt.splitlines())
        
        for i in xrange(len(splitrix)):
            for j in xrange(len(splitrix[i])):
                # get values at 0 (0), 1 (1, 6), 2 (2, 7, 12), etc.
                output[i+j] += [splitrix[i][j]] # outer [] keep them seperate

        for i in output:
            print ' '.join(output[i])       

oblique("input.txt")
print "-"*10 
oblique("input2.txt")      
