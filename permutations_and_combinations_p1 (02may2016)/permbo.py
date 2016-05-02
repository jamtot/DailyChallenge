def fac(n):
    if n == 0:
        return 1
    if n < 1: n*=-1
    for i in xrange(n-1,0,-1):
        n*=i
    return n 

def getperm(n, perm):
    numlist = range(n)
    perms = fac(n)
    if perms < perm:
        return "Permutation out of range."

    start,end=0,len(numlist)-1
    for blah in xrange(perm):
        i=end
        while True:
            i-=1
            if numlist[i] < numlist[i+1]:
                j = end
                while not (numlist[i] < numlist[j]):
                    j-=1
                numlist[i], numlist[j] = numlist[j], numlist[i]
                r = numlist[i+1:]
                r.reverse()
                numlist[i+1:]=r
                break
    return numlist
                    
def perms(n):
    numlist = range(n)
    permutations = [numlist[:]]
    start,end=0,len(numlist)-1
    while True:
        i=end
        while True:
            i-=1
            if numlist[i] < numlist[i+1]:
                j = end
                while not (numlist[i] < numlist[j]):
                    j-=1
                numlist[i], numlist[j] = numlist[j], numlist[i]
                r = numlist[i+1:]
                r.reverse()
                numlist[i+1:]=r
                permutations.append(numlist[:])
                break
            if i == start: 
                return permutations

def combinations(n, outof):
    return sorted({tuple(sorted(x[:n])) for x in perms(outof)})

def getcombo(n, outof, comb):
    combos = combinations(n, outof)
    if comb < len(combos):
        return combos[comb]
    else:
        return "Out of range."

def cheatperms(n):
    from itertools import permutations
    return list(permutations(range(n)))

if __name__ == "__main__":  
    assert getperm(6,239) == [1, 5, 4, 3, 2, 0] # 240th permutation
    assert getperm(7,3239) == [4, 2, 6, 5, 3, 1, 0] # 3240th permutation
    print getcombo(3,8,23)
    print getcombo(4,9,111)
