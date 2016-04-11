input0="""123
44.234
0x123N"""

input1 = """123 234 345
3.23e5
1293712938712938172938172391287319237192837329
.25"""

input2 = """2015 4 4`Challenge #`261`Easy
234.2`234ggf 45`00`number string number (0)"""

def getinput(inp):
    return inp.splitlines()

def processline(line):
    res = []
    if '`' in line:
        for l in line.split('`'):
            res.append(processline(l))
    else:
        for n in line.split():
            try:
                try:
                    n = int(n)
                except ValueError:
                    n = float(n)
            except ValueError:
                pass # leave as is (NaN)
            res.append(n)
    return res

def isnumer(inp):
    lines = getinput(inp)
    for line in lines:
        res = processline(line)
        if len(res)>1:
            for r in res: 
                try:
                    print '"'+' '.join(r)+'"',
                except TypeError: print r,
            print
        else: print res[0]
    print

if __name__ == "__main__":
    isnumer(input0)
    isnumer(input1)
    isnumer(input2)
