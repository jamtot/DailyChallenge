import re

def dec2bin(dec):
    bn = ''
    count,n=1,1
    while n*2 < dec:
        n*=2
        count+=1

    while n >= 1:
        if dec/n > 0:
            dec%=n
            bn+='1'
        else: bn+='0'
        n/=2
    return bn

# using 10 = 02 and 20 = 12
def dec2hyp(dec):
    hyperbinarys = [dec2bin(dec)]

    b10 = re.compile('10')
    b20 = re.compile('20')
    
    for hybi in hyperbinarys:
        for match in b10.finditer(hybi):
            hb = hybi[:match.start()] + '02' + hybi[match.end():]
            while hb[0] == '0':
                hb = hb[1:]
            if hb not in hyperbinarys:
                hyperbinarys.append(hb)
        for match in b20.finditer(hybi):
            hb = hybi[:match.start()] + '12' + hybi[match.end():]
            if hb not in hyperbinarys:
                hyperbinarys.append(hb)
        print hybi
    return len(hyperbinarys)
    
if __name__ == "__main__":
    print dec2hyp(18)
    print dec2hyp(73)
    # dec2hyp(12345678910) # gives 106851 after a while
