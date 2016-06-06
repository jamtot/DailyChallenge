# serial (in a row) 
# [A]--(x)--[B]--(y)--[C]   resistance = x + y

# parallel
#      +--(x)--+
#      |       |
# [A]--+--(y)--+--[B]
#      |       |
#      +--(z)--+            resistance = 1 / (1/x + 1/y + 1/z)

input1="""A B C
A B 10
A B 30
B C 50"""

input2="""A B C D E F
A C 5
A B 10
D A 5
D E 10
C E 10
E F 15
B F 20"""

#     AB+BF             30                  30
#                                                 1/(1/30+1/22.5) = 12.857
#    /AC+CE\    
#   |------|+EF 1/(1/5+1/15)+15=7.5+15    22.5  
#   \AD+DE/

from collections import defaultdict


def parse(inp):
    inp = inp.splitlines()
    nodes = inp.pop(0).split()
    resdict = defaultdict(list)
    for iput in inp:
        iput=iput.split()
        resdict[''.join(sorted(iput[:2]))].append(int(iput[2]))
    for key in resdict:
        if len(resdict[key]) > 1:
            resdict[key]=1./(reduce(lambda x,y: (1./x +1./y),resdict[key]))
        else:
            resdict[key]=resdict[key][0]
    resdict2 = defaultdict(int)
    for key in resdict:
        resdict2[key] = resdict[key]
    print resdict2
    return resdict2
       
def res(nodes):
    print nodes
    newdict = defaultdict(int)
    if len(nodes) == 1:
        print nodes
        for key in nodes:
            print key, nodes[key]        
        return nodes
    for key in nodes:
        for otherkey in nodes:
            if key!=otherkey:
                if key[0] == otherkey[0] and key[-1] == otherkey[-1]:
                    newdict[key[0]+otherkey[-1]]=1./(1./nodes[key]+1./nodes[otherkey])
                    print "parallel",key[0]+key[-1],newdict[key[0]+key[-1]]
                elif key[-1] == otherkey[0] and (ord(key[0]) < ord(otherkey[-1])):
                    if not any(ovvrkey[-1]==key[-1] for ovvrkey in nodes if ovvrkey!=key and ovvrkey!=otherkey):
                        newdict[key+otherkey]=nodes[key]+nodes[otherkey]
                        print "serial",key+otherkey,newdict[key+otherkey]
                #elif key not in newdict:
                #    newdict[key]=nodes[key]
    newdict = res(newdict)


def calculateresistance(inp):
    resdict = parse(inp)
    res(resdict)

if __name__ == "__main__":
    calculateresistance(input1)
    #calculateresistance(input2)
