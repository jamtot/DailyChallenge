def openfile(filename):
    with open(filename) as file:
        return (file.read()).splitlines()

def writefile(filename, toWrite):
    with open(filename, 'w') as file:
        file.write(toWrite)
        

def inventory(filename):
    candy = openfile(filename)
    total = len(candy)
    candy = sorted(candy)
    index, canDict, out = 0, {}, []

    while index < total:
        count = candy.count(candy[index])
        canDict[candy[index]] = count
        index+=count

    out+= ["%d pieces in total!" % total]
    out+= ["The haul consists of:"]
    # orders the dictionary by value instead of key
    for x in sorted(canDict, key=canDict.get, reverse=True):
        out += ["%s: %d pieces, %.1f%% of the total." % (
                x, canDict[x], float(canDict[x])/float(total)*100)]
    
    output = ("\n").join(out)
    print output
    writefile("inventoried.txt", output)
 
if __name__ == "__main__":
    inventory("candy.txt")
