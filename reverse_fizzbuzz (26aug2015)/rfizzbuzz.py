input0="""a
ac
b
a
ac
ab
ac
a
b
ac
a
abc
a"""

input1="""a
b
a
a
b
a
ab"""

input2="""b
be
ab
be
b
abe
b"""

def breakbuzz(inp):
    """This will only work for sequences in which all letters are shown together
    at some stage. It works out the multiples of each letter, gets the 
    lowest common multiple, then finds what numbers satisfy the equation."""

    inp=inp.splitlines()
    eqlist = inp
    seqlen = len(inp)
    inp="".join(inp)
    letters = []

    for l in inp:
        if l not in letters: 
            letters.append(l)

    for letter in letters:
        c=counter()
        for i in xrange(len(eqlist)):
            if letter in eqlist[i]:
                num=c.next()
                index=eqlist[i].index(letter)
                eqlist[i]=eqlist[i][:index]+str(num)+"*"+eqlist[i][index]+" "+eqlist[i][index+1:]   
      
    eqns=[]    
    for seq in eqlist:
        if all(letter in seq for letter in letters):
            eqns.append(seq)

    if len(eqns)<1:
        print "No equation to work with, I'm outta here."
        return

    equation = eqns[0]
    equation = equation.split()

    for i in xrange(len(equation)):
        equation[i]=equation[i].split("*")

    numlist,letterlist=zip(*equation)
    numlist=map(int,numlist)
    lowestcommult=lcmm(numlist)

    answerDict={}
    for i in xrange(len(letterlist)):
        print "%s is %d" % (letterlist[i],lowestcommult/numlist[i]),
        answerDict[letterlist[i]] = lowestcommult/numlist[i]
    print
    return answerDict
    
        
def counter(x=1):
    while True:
        yield x
        x+=1

def testbuzz(dictionary, lines):
    output=''
    i,curlines=1,0
    while curlines<lines:
        curline=''
        for key in sorted(dictionary):
            if i%dictionary[key]==0:
                curline+=key
        if not curline == '':
            output+=curline
            if curlines+1<lines:
                output+='\n'
            curlines+=1
        i+=1
    return output

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(nums):
    """Return lcm of a list of nums."""   
    return reduce(lcm, nums)

if __name__=="__main__":
    assert testbuzz(breakbuzz(input0),13) == input0
    assert testbuzz(breakbuzz(input1),7) == input1
    assert testbuzz(breakbuzz(input2),7) == input2
