input1="1101010"
input2="000000000000000000000000000000010000000000000000000000000000000"

"111"	"101"	"010"	"000"	"110"	"100"	"011"	"001"

def XOR(a,b,c):
    index = ''.join(map(str,[a,b,c]))
    return {
        '111': 0,
        '101': 0,
        '010': 0,
        '000': 0,
        '110': 1,
        '100': 1, 
        '011': 1,
        '001': 1, 
            }[index]

def ca(inp, lines):
    prev = [int(i) for i in inp]
    printline(prev)
    for q in xrange(lines):
        #next = [ XOR(prev[i-1], prev[i], prev[i+1]) for i in xrange(1,len(prev)-1)]
        prev = [prev[-1]]+prev+[prev[0]] # to compensate for the lost
        next = [prev[i-1] ^ prev[i+1] for i in xrange(1,len(prev)-1)]
        printline(next)
        prev = next

def printline(line, syms = ' x'):
    print ''.join([syms[x] for x in line]) 

if __name__ == "__main__":
    ca(input1, 6)
    ca(input2, 31)
