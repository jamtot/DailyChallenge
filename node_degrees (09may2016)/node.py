from collections import defaultdict

input0="""3
1 2
1 3"""

input1="""16
1 2
1 3
2 3
1 4
3 4
1 5
2 5
1 6
2 6
3 6
3 7
5 7
6 7
3 8
4 8
6 8
7 8
2 9
5 9
6 9
2 10
9 10
6 11
7 11
8 11
9 11
10 11
1 12
6 12
7 12
8 12
11 12
6 13
7 13
9 13
10 13
11 13
5 14
8 14
12 14
13 14
1 15
2 15
5 15
9 15
10 15
11 15
12 15
13 15
1 16
2 16
5 16
6 16
11 16
12 16
13 16
14 16
15 16"""

def degrees(inpt):
    nodedict = defaultdict(list)
    inpt = inpt.splitlines()
    nodes = int(inpt.pop(0))
    inpt = [map(int,i.split()) for i in inpt]
    for i in inpt:
        nodedict[i[0]].append(i[1])
        nodedict[i[1]].append(i[0])
    for key in sorted(nodedict):
        print "Node %d has a degree of %d"%(key, len(nodedict[key]))
    print
    adjmatrix(nodes, nodedict)

def adjmatrix(nodes, nodedict):
    print "Adjacency matrix:"
    for y in xrange(1, nodes+1):
        for x in xrange(1, nodes+1):
            if x in nodedict[y]:
                print 1,
            else: print 0,
        print
                
        

if __name__ == "__main__":
    degrees(input0)
    print
    degrees(input1)
    
