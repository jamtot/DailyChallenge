input0 = [8, 1, 6, 3, 5, 7, 4, 9, 2]# => true
input1 = [2, 7, 6, 9, 5, 1, 4, 3, 8]# => true
input2 = [3, 5, 7, 8, 1, 6, 4, 9, 2]# => false
input3 = [8, 1, 6, 7, 5, 3, 4, 9, 2]# => false
bonusinput1= [1,15,14,4,12,6,7,9,8,10,11,5,13,3,2,1]# => false
bonusinput2= [8,11,14,1,13,2,7,12,3,16,9,6,10,5,4,15]# => true
bonusinput3= [73,77,11,66,25,107,4,112,12,99,85,
84,55,70,33,63,6,106,32,108,54,60,
18,76,47,110,35,96,36,78,46,116,13,
88,26,74,43,65,1,92,42,109,31,100,
75,82,34,69,51,119,50,72,37,58,24,
20,9,103,5,120,117,118,2,80,7,90,
22,81,57,71,48,121,49,61,38,59,64,
102,27,111,40,98,3,86,41,114,19,30,
17,95,44,101,56,83,39,115,45,62,14,
79,52,104,28,89,8,68,29,67,53,94,
93,91,16,105,21,10,23,87,15,113,97]# => true
bonusinput4= [37, 78, 29, 70, 21, 62, 13, 54, 5,
6, 38, 79, 30, 71, 22, 63, 14, 46,
47, 7, 39, 80, 31, 72, 23, 55, 15,
16, 48, 8, 40, 81, 32, 64, 24, 56,
57, 17, 49, 9, 41, 73, 33, 65, 25,
26, 58, 18, 50, 1, 42, 74, 34, 66,
67, 27, 59, 10, 51, 2, 43, 75, 35,
36, 68, 19, 60, 11, 52, 3, 44, 76,
77, 28, 69, 20, 61, 12, 53, 4, 45]# => true
bonusinput5= [1,120,121,48,85,72,73,60,97,24,25,144,
142,27,22,99,58,75,70,87,46,123,118,3,
11,110,131,38,95,62,83,50,107,14,35,134,
136,33,16,105,52,81,64,93,40,129,112,9,
8,113,128,41,92,65,80,53,104,17,32,137,
138,31,18,103,54,79,66,91,42,127,114,7,
5,116,125,44,89,68,77,56,101,20,29,140,
139,30,19,102,55,78,67,90,43,126,115,6,
12,109,132,37,96,61,84,49,108,13,36,133,
135,34,15,106,51,82,63,94,39,130,111,10,
2,119,122,47,86,71,74,59,98,23,26,143,
141,28,21,100,57,76,69,88,45,124,117,4]# => true


bonus2input1=[8, 1, 6, 3, 5, 7]# => true
bonus2input2=[3, 5, 7, 8, 1, 6]# => false
bonus2input3= [1,120,121,48,85,72,73,60,97,24,25,144,
142,27,22,99,58,75,70,87,46,123,118,3,
11,110,131,38,95,62,83,50,107,14,35,134,
136,33,16,105,52,81,64,93,40,129,112,9,
8,113,128,41,92,65,80,53,104,17,32,137,
138,31,18,103,54,79,66,91,42,127,114,7,
5,116,125,44,89,68,77,56,101,20,29,140,
139,30,19,102,55,78,67,90,43,126,115,6,
12,109,132,37,96,61,84,49,108,13,36,133,
135,34,15,106,51,82,63,94,39,130,111,10,
2,119,122,47,86,71,74,59,98,23,26,143]# => true

def magicsquare(sqinput):
    total = len(sqinput)
    size = int(total**0.5)
 
    # break the list into 3 seperate lists for the rows
    sublists = [sqinput[i:i+size] for i in range(0, len(sqinput), size)]
    rows =  map(sum,sublists)
    # unzipping the rows gets the columns
    cols = map(sum,zip(*sublists))
    
    # get your diagonals
    diags = [[],[]]
    for x in xrange(size):
        for y in xrange(size):
            index = size*x+y
            if index%(size+1)==0:
                diags[0].append(sqinput[index])
            if index%(size-1)==0 and index >0 and index<(total-1):
                diags[1].append(sqinput[index])

    diags = map(sum,diags)

    if diags[0] == diags[1]:
        for x, y in zip(rows, cols):
            if x==y==diags[0]:
                continue
            else: break
        else:
            print "Sum is %d." % diags[0]
            return True 
    return False


def ismagic(sqinput):
    # because we know that a square minus
    # a row is between squares (e.g. 3*2 is
    # between 2*2 and 3*3), we can square root,
    # truncate the decimal, add one and square 
    # that to achieve our total square size
    total = (int(len(sqinput)**0.5)+1)**2
    size = int(total**0.5)
    
    sparenums = []
    # in range of all nums
    sparenums = [num for num in range(1,total+1) if num not in sqinput]
    sublists = [sqinput[i:i+size] for i in range(0, len(sqinput), size)]

    # get the sum of the top rows
    rowsofar = map(sum, sublists)
    # if they're not equal, we're outta here
    if not all(x==rowsofar[0] for x in rowsofar):
        return False

    # row sums are equal, so thats the sum we want
    sumtoget = rowsofar[0]

    # get the sum of the columns minus last row
    cols = map(sum,zip(*sublists))

    # make the bottom row you need
    neededrow = []
    for col in cols:
        if (sumtoget-col) in sparenums:
            neededrow.append(sumtoget-col)
        else: return False

    # making sure numbers were only used once
    if sorted(neededrow) != sorted(sparenums):
        return False

    # add the new row to the end of the input
    for num in neededrow:
        sqinput.append(num)
        
    # now throw it into the other function
    return magicsquare(sqinput)

if __name__ == "__main__":
    assert magicsquare(input0) == True# True. Sum is 15.
    assert magicsquare(input1) == True# True. Sum is 15.
    assert magicsquare(input2) == False# False.
    assert magicsquare(input3) == False# False.
    assert magicsquare(bonusinput1) == False# False.
    assert magicsquare(bonusinput2) == True# True. Sum is 34.
    assert magicsquare(bonusinput3) == True# True. Sum is 671.
    assert magicsquare(bonusinput4) == True# True. Sum is 369.
    assert magicsquare(bonusinput5) == True# True. Sum is 870.

    assert ismagic(bonus2input1) == True# True. Sum is 15.
    assert ismagic(bonus2input2) == False# False.
    assert ismagic(bonus2input3) == True# True. Sum is 870.
