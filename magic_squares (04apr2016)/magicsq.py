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
            return "True. Sum is %d." % diags[0]
    return "False."

if __name__ == "__main__":
    print magicsquare(input0)# True. Sum is 15.
    print magicsquare(input1)# True. Sum is 15.
    print magicsquare(input2)# False.
    print magicsquare(input3)# False.
    print magicsquare(bonusinput1)# False.
    print magicsquare(bonusinput2)# True. Sum is 34.
    print magicsquare(bonusinput3)# True. Sum is 671.
    print magicsquare(bonusinput4)# True. Sum is 369.
