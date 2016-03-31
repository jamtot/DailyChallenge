from itertools import product
from collections import defaultdict

def read_NOS(nos):
    form = '('*(len(nos))
    catchlast = 0
    for i in xrange(len(nos)):
        form+=str(i)
        form+=")"
        if nos[i] == "0":
            form+="+"
        elif nos[i] == "1":
            form+="-"
        elif nos[i] == "2":
            form+="*"
        catchlast = i
    form+=str(catchlast+1)
    return eval(form)

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

def find_NOS(num):
    for i in xrange(len(nos)):
        pass

    

def get_next_tern(i=1):
    while True:
        for x in product(range(3), repeat=i):
            y = "".join(map(str,list(x)))
            yield y 
        i+=1


def find_num(decnum):
    tern_gen = get_next_tern()
    i = next(tern_gen)
    while nos2dec(i) != decnum:
        i = next(tern_gen)
    return i

def get_nums_to(numto):
    for i in xrange(numto+1):
        print "%d = %s" %(i, find_num(i))


def gen_ternary_nums(max):
    nums = []
    for i in xrange(1,max+1):
    #i = 0
    #while nos2dec(nums[-1])<max:
        # using product to basically count up in ternary
        lines = "".join( map(str,list(product(range(3), repeat=i))))
        lines = lines.splitlines()
        for line in lines:
            line = ("".join("".join(line[1:-1].split(",")).split())).split(")(")
            #line = line.split(")(")
            nums+=[l for l in line]
        #i+=1
    return nums

if __name__ == "__main__":
    assert read_NOS("0000") == 10
    assert read_NOS("0220") == 10
    assert read_NOS("02212") == 10
    assert read_NOS("10020") == 21

    assert nos2dec("0000") == 10
    assert nos2dec("0220") == 10
    assert nos2dec("02212") == 10
    assert nos2dec("10020") == 21

    assert nos2dec("2") == 0

    #gen_nums(50)
    tnums = gen_ternary_nums(7)
    #print tnums
    nosdict = defaultdict(list)
    for num in tnums:
        nosdict[nos2dec(num)].append(num)

    for x in xrange(0,51):
        print "%d: %r" %(x,nosdict[x][0])
        

    assert find_num(20) == "0202"   
    get_nums_to(50)
    
