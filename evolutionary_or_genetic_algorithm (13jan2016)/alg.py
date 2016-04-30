from random import randint
import string

def algorithm(strng):
    """evolutionary algorithm that changes one letter at a time
    randomly, checks the fitness, and replaces the letter if it's
    better. I'm not sure if this is the right way to go about this."""
    chars = string.printable[:95]
    algstring = ''.join([randchar(chars) for i in xrange(len(strng))])
    gennum = 1
    fitness = hammingDistance(strng, algstring)
    printgen(gennum, fitness, algstring)
    strlen = len(algstring)
    
    #found = []
    i=0
    while fitness > 0:
        #while i in found: i+=1
        if i >= strlen: i%=strlen
        newdaddy = algstring[:i]+randchar(chars)+algstring[i+1:]
        newdaddy=newdaddy[:strlen]
        if fitness > hammingDistance(strng, newdaddy):
            fitness = hammingDistance(strng, newdaddy)
            algstring = newdaddy
            #found+=[i]
            printgen(gennum, fitness, algstring)
        gennum+=1
        i+=1
    
def algorith2(string):
    chars = string.printable[:95]
    algstring = ''.join([randchar(chars) for i in xrange(len(strng))])
    gennum = 1
    

def randchar(charset):
    return charset[randint(0,len(charset)-1)]
    
def hammingDistance(s1, s2): 
    """taken from 
    https://en.wikipedia.org/wiki/Hamming_distance#Algorithm_example"""
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        print s1, s2
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))

def printgen(genum, fitness, curgen):
    print "Gen: %d | Fitness: %d | %s"%(genum,fitness,curgen)

if __name__ == "__main__":
    algorithm("Hello, world!")
    algorithm("I have no idea what I'm doing.")
