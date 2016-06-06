from collections import Counter
from itertools import permutations
import datetime

def checkrange(n):
    low = int('1'+'0'*(n-1))
    high = int('9'*n)
    """not using list comprehension as it involves 
    calling the selfdesc() func twice"""
    #sdescs = [selfdesc(i) for i in xrange(low,high+1) if selfdesc(i) != 0]
    
    sdescs = []
    for i in xrange(low, high+1):
        n = selfdesc(i)
        if n != 0: sdescs.append(n)

    if len(sdescs) < 1:
        print "No self-descriptive number found"
    else:
        for n in sdescs:
            print n

def selfdesc(n):
    nlist = [int(i) for i in str(n)]
    if sum(nlist) == len(nlist):
        c = Counter(nlist)
        desc = [c[i] for i in xrange(len(nlist))]
        if nlist == desc:
            return int(''.join(map(str,desc)))
    return 0


def checkperms(n):
    sdescs = []
    part = map(list,list(partition(n)))
    for p in part:
        p+=[0]*(n-len(p))
        for perm in permutations(p):
            if perm[0] > 0 and perm[-1] == 0:
                if constraintcheck(perm):
                    if selfdescriptive(perm):
                        pernum = int(''.join(map(str,perm)))
                        if pernum not in sdescs:
                            sdescs.append(pernum)
    if len(sdescs) < 1:
        print "No self-descriptive number found"
    else:
        for n in sdescs:
            print n
      
def selfdescriptive(n):
    c = Counter(n)
    desc = [c[i] for i in xrange(len(n))]
    if list(n) == desc:
        return True
    return False

def constraintcheck(n):
    nlen=len(n)
    if sum(n) == xindex(n, nlen) == nlen:
        return True
    return False

def xindex(nlist, nlen):
    totes = 0
    for i in xrange(nlen):
        totes += nlist[i]*i
    return totes

def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
    return answer

if __name__ == "__main__":
    print constraintcheck([1,2,1,0])
    print selfdescriptive([1,2,1,0])

    assert selfdesc(101) == 0
    assert selfdesc(21200) != 0
    """
    start = datetime.datetime.now()
    for i in xrange(1,9):
        checkrange(i)
    print "Bruteforce:",(datetime.datetime.now() - start)
    """

    start = datetime.datetime.now()
    for i in xrange(1,9):
        checkperms(i)
    print "Partition and permutations:",(datetime.datetime.now() - start)
    
    start = datetime.datetime.now()
    checkperms(10)
    print "Partition and permutations, 10 digit number:",(datetime.datetime.now() - start)
    
    """ output

    No self-descriptive number found
    No self-descriptive number found
    No self-descriptive number found
    1210
    2020
    21200
    No self-descriptive number found
    3211000
    42101000
    Bruteforce: 0:05:27.670671
    No self-descriptive number found
    No self-descriptive number found
    No self-descriptive number found
    2020
    1210
    21200
    No self-descriptive number found
    3211000
    42101000
    Partition and permutations: 0:00:03.308865

    6210001000
    Partition and permutations, 10 digit number: 0:10:08.748553

    ------------------------------------------------------------
    after adding more constraint checking times are improved
    for the partition checking

    No self-descriptive number found
    No self-descriptive number found
    No self-descriptive number found
    2020
    1210
    21200
    No self-descriptive number found
    3211000
    42101000
    Partition and permutations: 0:00:00.437745

    6210001000
    Partition and permutations, 10 digit number: 0:01:05.516403

    """
