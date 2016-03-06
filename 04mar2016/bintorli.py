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

def splitinputs(input):
    return input.splitlines()

if __name__ == '__main__':
    splitputs = splitinputs(input)
    for line in splitputs:
        print line
        print bin_to_rli(line)
        print bin_to_rle(line)
