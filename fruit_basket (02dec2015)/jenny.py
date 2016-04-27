input0="""banana 32
kiwi 41
mango 97
papaya 254
pineapple 399"""

input1="""apple 59
banana 32
coconut 155
grapefruit 128
jackfruit 1100
kiwi 41
lemon 70
mango 97
orange 73
papaya 254
pear 37
pineapple 399
watermelon 500"""

def parse(inp):
    lines = inp.splitlines()
    return dict([(int(x.split()[1]),x.split()[0]) for x in lines])

def outputans(bought, fdict):
    bought=map(int, sorted(bought.split()))
    cur=bought[0]
    count=0
    ans=''
    for b in bought:
        if cur == b:
            count+=1
        else:
            if count > 1:
                # the pluralisation is basic, doesn't
                # account for berry->berries, mango->mangoes
                # it just adds an s.
                ans+="%d %ss, "%(count, fdict[cur])
            else:
                ans+="%d %s, "%(count, fdict[cur])
            cur = b
            count=1
    else:
        if count > 1:
            ans+="%d %ss"%(count, fdict[cur])
        else:
            ans+="%d %s"%(count, fdict[cur])
        cur = b
        count=1
    return ans
        

def buyfruit(anslist, money, fdict, plist, fruitbought=''):
    if money == 0:
        ans = outputans(fruitbought, fdict)
        if ans not in anslist:
            anslist.append(ans)
        return
    if money < 0:
        #spent too much
        return
    if money > 0:
        for i in plist:
            if i <= money:
                buyfruit(anslist, money-i, fdict, plist, fruitbought+str(i)+' ')
            else:
                continue
        return

def findfruits(inputname, monies):
    answerlist=[]
    fruitdict = parse(inputname)
    pricelist = [i for i in fruitdict]
    buyfruit(answerlist, monies, fruitdict, pricelist)
    for answer in answerlist:
        print answer
    print "%d solutions found."%len(answerlist)
    
if __name__ == "__main__":
    findfruits(input0, 500)
    print
    # very slow to run, as it has to go VERY deep
    #finds 180/181 solutions
    findfruits(input1, 500)

