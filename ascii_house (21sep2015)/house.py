bp1="""3
   *
  ***
******"""

def base(stars):
    line = '+'
    line+= '-----'*stars
    return line[:-2]+'+'

def blank(blanks):
    line = "     "*blanks
    return line[:-2]

def walls(stars):
    line = '|'
    line+= '    '*stars
    return line[:-2]+'|'
    
def split_line(line):
    outty=[]
    cur=line[0]
    count=0
    for char in line:
        if cur==char:
            count+=1
        else:
            outty.append((cur, count))
            count = 0
            cur = char
    else:
        count+=1
        outty.append((cur, count))
    return outty
    

def house(blueprint):
    bp = blueprint.splitlines()
    ascii = ''
    lines = int(bp.pop(0))
    bp = bp[::-1]
    bottom = bp[0]
    ascii += base(len(bottom))
    ascii = walls(len(bottom))+'\n'+ascii
    #print ascii

    for i in xrange(1, lines):
        ltups = split_line(bp[i])
        #print ltups
        thisline = ''
        for x in ltups:
            if x[0] == "*":
                thisline+=blank(x[1])
            else:
                thisline+=base(x[1])
        else: 
            thisline+='\n'
            ascii = thisline+ascii
            thisline=''

        for x in ltups:
            if x[0] == "*":
                thisline+=walls(x[1])
            else:
                thisline+=blank(x[1])
        else: 
            thisline+='\n'
            ascii = thisline+ascii
            thisline=''

    ltups = split_line(bp[-1])
    for x in ltups:
        if x[0] == "*":
            thisline+=base(x[1])
        else:
            thisline+=blank(x[1])
    else: 
        thisline+='\n'
        ascii = thisline+ascii
        thisline=''

    print ascii


if __name__ == "__main__":
    house(bp1)
