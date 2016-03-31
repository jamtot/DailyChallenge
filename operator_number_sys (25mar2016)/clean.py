from itertools import product

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def getnext(n=0):
    while True:
        yield n
        n+=1

def nos2dec(nos):
    i = getnext()
    return reduce(lambda x,y: [add, sub, mult][y](x, next(i)), map(int, nos), next(i))

# counts up in ternary
def tern_gen(i=1):
    while True:
        for x in product(range(3), repeat=i):
            y = "".join(map(str,list(x)))
            yield y 
        i+=1

def find_num(decnum):
    t_gen = tern_gen()
    i = next(t_gen)
    while nos2dec(i) != decnum:
        i = next(t_gen)
    return i

def get_nums_to(n):
    for i in xrange(n+1):
        print "%d = %s" %(i, find_num(i))

if __name__ == "__main__":  
    get_nums_to(50)
