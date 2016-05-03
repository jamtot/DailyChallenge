from itertools import combinations

def vamps(n, m):
    """ finds a 'vampire' number with n digits, which is both the product
    of m 2-digit 'fang' numbers, and comprised of the same digits as
    the fangs"""
    vampires = []
    for fangs in combinations(range(10,100), m):
        candidate = reduce(lambda x,y: x*y, fangs)
        candtsr=str(candidate)
        if sorted(candtsr) == sorted(''.join(map(str,fangs))):
            # can't have trailing pair of zeros, per description
            if candtsr[-2:] != "00" and len(candtsr) == n:
                vampires.append((candidate, fangs))
    return sorted(vampires)

def printit(it):
    print it

if __name__ == "__main__":
    # using list comprehensions to force a print is not good
    print "4 digit vampires with 2 fangs"
    [printit(v) for v in vamps(4,2)]
    print "6 digit vampires with 3 fangs"
    [printit(v) for v in vamps(6,3)]
    print "8 digit vampires with 4 fangs"
    [printit(v) for v in vamps(8,4)]
    
