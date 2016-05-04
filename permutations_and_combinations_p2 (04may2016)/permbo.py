def fac(n):
    if n == 0:
        return 1
    if n < 1: n*=-1
    for i in xrange(n-1,0,-1):
        n*=i
    return n 

def ind2fac(n):
    i,next=1,0
    fac = []
    while n > 0:
        next=n%i
        n/=i
        fac.insert(0, next)
        i+=1
    return fac

def fac2ind(numlist):
    nummy=0
    i,j = 0,len(numlist)-1
    while j >= 0:
        nummy+=numlist[i]*fac(j)
        i+=1
        j-=1
    return nummy

def getperm(index, lisht):
    factoradic = [int(n) for n in ind2fac(index)]
    factoradic = [0]*(len(lisht)-len(factoradic))+factoradic
    perm=[]
    for i in factoradic:
        perm += [lisht.pop(i)]
    return perm

def getpermnum(permutation):
    orig = []
    factoradic = []
    for i in permutation[::-1]:
        if len(orig) == 0:
            orig.append(i)
            factoradic.append(0)
        elif len(orig) == 1:
            if i < orig[0]:
                orig.insert(0, i)
                factoradic.insert(0,0)
            else: 
                orig.append(i) 
                factoradic.insert(0,1)
        else:
            for j in xrange(len(orig)-1):
                if j == 0 and orig[j] > i:
                    orig.insert(0, i)
                    factoradic.insert(0,0)
                    break
                elif orig[j] < i < orig[j+1]:
                    orig.insert(j+1,i)
                    factoradic.insert(0,j+1)
                    break
                elif orig[j+1] == orig[-1] and i > orig[-1]:
                    orig.append(i)
                    factoradic.insert(0,len(orig)-1)
                    break
    return fac2ind(factoradic)

if __name__ == "__main__":  
    assert getperm(2982, range(7)) == [4, 0, 6, 2, 1, 3, 5]
    print getperm(12345678901234, range(42))
    print getpermnum([25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 35, 32, 36, 34, 39, 
        29, 27, 33, 26, 37, 40, 30, 31, 41, 28, 38])
    print getperm(getpermnum([25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
        12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 35, 32, 36, 
        34, 39, 29, 27, 33, 26, 37, 40, 30, 31, 41, 28, 38]), range(42))
