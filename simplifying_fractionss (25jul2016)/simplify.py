input0="""4 8
1536 78360
51478 5536
46410 119340
7673 4729
4096 1024"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
    """while b!=0:
        t=b
        b=a%b
        a=t
    return a"""

if __name__ == "__main__":
    for line in input0.splitlines():
        l=map(int,line.split())
        divisor=gcd(l[0],l[1])
        print l[0]/divisor, l[1]/divisor
