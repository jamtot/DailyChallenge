input0="""2
1/6
3/10"""

input1="""3
1/3
1/4
1/12"""

input2="""5
2/9
4/35
7/34
1/2
16/33"""

input3="""10
1/7
35/192
61/124
90/31
5/168
31/51
69/179
32/5
15/188
10/17"""

input4c="""100
28/6
6/34
16/13
8/23
24/9
23/23
26/17
13/39
19/14
2/9
28/16
27/27
34/29
6/17
16/34
11/36
5/28
24/8
31/2
2/20
16/37
27/38
37/39
16/10
30/13
21/40
18/19
8/20
1/23
38/31
16/12
32/10
24/4
8/21
11/35
15/40
6/32
4/1
40/8
36/23
33/39
16/18
23/17
25/6
2/27
26/21
19/9
33/40
36/10
11/10
11/34
37/24
4/30
38/13
30/19
3/5
34/32
30/10
34/40
31/6
29/17
12/24
9/14
38/29
34/9
39/7
17/17
12/39
32/40
21/19
33/23
17/38
27/40
39/39
4/38
11/33
9/37
40/8
8/3
11/6
39/33
29/30
37/35
40/28
22/37
37/17
28/14
12/17
30/35
2/10
2/15
12/25
32/8
38/35
17/25
29/32
1/1
31/7
8/18
37/38"""

def gcd(a, b):
    """gets the greatest common divisor"""
    while b:   
        a, b = b, a % b
    return a

def lcm(a, b):
    """for finding lowest common multiple"""
    return a * b // gcd(a, b)


def lcmm(listlcm):
    """finding lcm of a list"""
    return reduce(lcm, listlcm)

def processinput(inpt):
    inpt = inpt.splitlines()
    amount = int(inpt.pop(0))
    return inpt[:amount]

def addfracs(inp):
    fracs = processinput(inp)
    numerators,denominators=[],[]
    for f in fracs:
        f=f.split('/')
        numerators+=[int(f[0])]
        denominators+=[int(f[1])]
    lowestcm=lcmm(denominators)
    for i in xrange(len(denominators)):
        numerators[i]*=(lowestcm/denominators[i])
    numer=reduce(lambda x,y: x+y, numerators)
    divisor=gcd(numer, lowestcm)
    numer/=divisor
    lowestcm/=divisor
    return "%d/%d"%(numer,lowestcm)

if __name__ == "__main__":
    assert addfracs(input0) == "7/15"
    assert addfracs(input1) == "2/3"
    print addfracs(input2) # 89962/58905
    print addfracs(input3) # 351910816163/29794134720
    print addfracs(input4c) # 844188866140108057/5342931457063200
