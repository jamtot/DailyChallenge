# input has 1 per line
input = """0 0 1 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1"""

def bin_to_rli(binary_input):
    stringlist = binary_input.split()    
    zero, count, outputlist = True, 0, []
    for x in stringlist:
        if zero:
            if x == '1':
                outputlist.append(str(count))
                zero = False
        else:
            if x == '0':
                outputlist.append(str(count))
                zero = True
        count+=1
    # add the final count    
    outputlist.append(str(count))

    output = (' ').join(outputlist)
    return output

def bin_to_rle(binary_input):
    stringlist = binary_input.split()
    zero, count, outputlist = True, 0, []
    for x in stringlist:
        if zero:
            if x == '0':
                count+=1
            else:
                outputlist.append(str(count))
                zero, count = False, 0
        else:
            if x == '1':
                count+=1
            else:
                outputlist.append(str(count))
                zero, count = True, 0
    # add the final count    
    outputlist.append(str(count))

    output = (' ').join(outputlist)
    return output

def rli_to_bin(rle_input):
    stringlist = rle_input.split()
    previous, zero, first, outputlist, char = 0, True, True, [], ''
    for x in stringlist:
        x = int(x)
        toWrite = x-previous
        if zero:  
            char = '0'    
            # write x zeros
            zero = False
        else:
            char = '1'
            # write x many ones
            zero = True
        for i in xrange(toWrite):
            outputlist.append(char)
        previous=x

    output = (' ').join(outputlist)
    return output

def rle_to_bin(rle_input):
    stringlist = rle_input.split()
    zero, first, outputlist, char = True, True, [], ''
    for x in stringlist:
        x = int(x)
        if first:
            first = False
        else:
            x+=1
        if zero:  
            char = '0'    
            # write x zeros
            zero = False
        else:
            char = '1'
            # write x many ones
            zero = True
        for i in xrange(x):
            outputlist.append(char)

    output = (' ').join(outputlist)
    return output
    
def rle_to_rli(rle_input):
    stringlist = rle_input.split()
    outputlist = []
    aggr, first = 0, True
    for x in stringlist:
        x = int(x)
        if first:
            # don't add 1
            first = False
        else:
            # add one
            x+=1
        aggr+=x
        outputlist.append(str(aggr))
    return (' ').join(outputlist)
        
def rli_to_rle(rli_input):
    stringlist = rli_input.split()
    outputlist = []
    previous, first = 0, True
    for x in stringlist:
        x = int(x)
        towrite = x
        if first:
            # don't add 1
            first = False
        else:
            # add one
            previous+=1
        towrite= x-previous
        previous = x
        outputlist.append(str(towrite))
    return (' ').join(outputlist)

def rli_to_subrli(input):
    # splitting into needed data
    splitdata = input.split()
    start_index = int(splitdata.pop(0))
    length = int(splitdata.pop(0))

    # a list to hold the output
    outputlist = []
    
    # find the index for the entry at or just below the start_index
    index = 0
    for x in splitdata:
        x = int(x)
        if x < start_index:
            index+=1
        else: # greater or equal
            break
    
    # create a subsetted list of the data, only from the first point needed
    culledlist = splitdata[index:]

    # in the case of the substring starting at one,
    # there needs to be a 0 to denote no zeros
    if index%2==1:
        outputlist.append('0')

    for elem in culledlist:
        if (int(elem)-start_index) < length:      
            outputlist.append(str(int(elem)-start_index))
        else: break

    # append the last entry, which is going to be the final length
    outputlist.append(str(length))

    output = (' ').join(outputlist)
    return output

#------CHEATING---------- 
# will use this for testing purposes, as it will be right

def binary_overwrite(start_index, newdata, originaldata):
    newdata, originaldata = newdata.split(), originaldata.split()
    j = 0    
    for i in xrange(start_index, start_index+len(newdata)):
        originaldata[i] = newdata[j]
        j+=1
    return (" ").join(originaldata)

def cheat_overwrite(input):
    splitdata = input.split(" > ")
    changes = [int(n) for n in (splitdata.pop(0)).split()]
    start_index = changes.pop(0)
    changes = (" ").join(map(str, changes))
    tobechanged = splitdata.pop(0)
    return bin_to_rli(binary_overwrite(start_index, rli_to_bin(changes), rli_to_bin(tobechanged)))

#--------CHEATING------------

def rli_overwrite(input):
    # seperate out initial values
    splitdata = input.split(" > ")
    changes = [int(n) for n in (splitdata.pop(0)).split()]
    start_index = int(changes.pop(0))

    tobechanged = [int(n) for n in (splitdata.pop(0)).split()]
    
    # a list to hold the output
    outputlist = []
    
    # find the index for the entry at or just below the start_index
    index, firstchunk = 0, 0
    
    for x in tobechanged:
        if x < start_index:
            # add elements up until the overwrite
            outputlist.append(str(x))
            index+=1
            firstchunk+=1
        else: # greater or equal
            break

    #------middle bit-------------
    

    if len(outputlist)%2 == changes[0]:
        # add a marker to signify a change
        outputlist.append(str(start_index))

    for x in changes[not changes[0]:-1]:
        if len(outputlist)<1 or str(x+start_index) != outputlist[-1]:
            outputlist.append(str(x+start_index))

    # bring the index up to what would be the current position
    # to see if the current should be zeros or ones
    while (tobechanged[index] < changes[-1]+start_index):
        index+=1

    # if there's a change in number after the list, drop a changepoint
    if (index%2 == len(changes)%2):
    #if (len(outputlist)%2 != len(changes)%2):
    #if (len(outputlist)%2 == len(changes)%2): # passes 11/12 tests with this (although incorrect)
        outputlist.append(str(changes[-1]+start_index))
        index+=1

    #------end middle----------------

    # add in the rest after the overwrite
    for x in tobechanged:
        if x > changes[-1]+start_index:
            # add elements up until the overwrite
            outputlist.append(str(x))
            index+=1

    return (" ").join(outputlist)

def splitinputs(input):
    return input.splitlines()

def getfiletext(filename):
    with open(filename) as file:
        return file.read()

def writetofile(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

if __name__ == '__main__':

    print "Correct values (binary conversion):"
    print cheat_overwrite("3 0 3 > 2 3 7 10")
    print cheat_overwrite("3 1 3 > 2 3 7 10")
    print cheat_overwrite("3 1 3 > 10")
    print cheat_overwrite("3 1 3 > 0 10")
    print cheat_overwrite("3 0 3 7 10 12 15 > 8 9 10 13 14 18 19 21 22 23 24 25 26 32")

    print "RLI Overwrite values:"
    print rli_overwrite("3 0 3 > 2 3 7 10") # 2 | 6 | 7 10
    print rli_overwrite("3 1 3 > 2 3 7 10")#2 | 3 4 6 | 7 10
    print rli_overwrite("3 1 3 > 10")# | 4 6 | 10
    print rli_overwrite("3 1 3 > 0 10")#0 | 3 4 | 10
    print rli_overwrite("3 0 3 7 10 12 15 > 8 9 10 13 14 18 19 21 22 23 24 25 26 32")# | 3 6 10 13 15 18 | 19 21 22 23 24 25 26 32
