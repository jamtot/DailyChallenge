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
        
def splitinputs(input):
    return input.splitlines()

if __name__ == '__main__':
    converted = []
    splitputs = splitinputs(input)
    for line in splitputs:
        #print line
        #print bin_to_rli(line)
        converted.append( bin_to_rli(line) )
        convertedstr = ('\n').join(converted)
    
    #print '----------'

    convertsplit = splitinputs(convertedstr)
    for line in convertsplit:
        print "The line being converted from rle:"        
        print line
        print "The converted binary string:"
        print rli_to_bin(line)
