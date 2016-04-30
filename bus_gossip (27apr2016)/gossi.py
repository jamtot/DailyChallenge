input0="""3 1 2 3
3 2 3 1 
4 2 3 4 5"""

input1="""2 1 2
5 2 8"""

input2="""7 11 2 2 4 8 2 2
3 0 11 8
5 11 8 10 3 11
5 9 2 5 0 3
7 4 8 2 8 1 0 5
3 6 8 9
4 2 11 3 3"""

input3="""12 23 15 2 8 20 21 3 23 3 27 20 0
21 14 8 20 10 0 23 3 24 23 0 19 14 12 10 9 12 12 11 6 27 5
8 18 27 10 11 22 29 23 14
13 7 14 1 9 14 16 12 0 10 13 19 16 17
24 25 21 4 6 19 1 3 26 11 22 28 14 14 27 7 20 8 7 4 1 8 10 18 21
13 20 26 22 6 5 6 23 26 2 21 16 26 24
6 7 17 2 22 23 21
23 14 22 28 10 23 7 21 3 20 24 23 8 8 21 13 15 6 9 17 27 17 13 14
23 13 1 15 5 16 7 26 22 29 17 3 14 16 16 18 6 10 3 14 10 17 27 25
25 28 5 21 8 10 27 21 23 28 7 20 6 6 9 29 27 26 24 3 12 10 21 10 12 17
26 22 26 13 10 19 3 15 2 3 25 29 25 19 19 24 1 26 22 10 17 19 28 11 22 2 13
8 4 25 15 20 9 11 3 19
24 29 4 17 2 0 8 19 11 28 13 4 16 5 15 25 16 5 6 1 0 19 7 4 6
16 25 15 17 20 27 1 11 1 18 14 23 27 25 26 17 1"""

class busdriver(object):
    def __init__(self, route, ID, totalgossips, bonus, gossips=1):
        self.route = route
        self.gossips = gossips
        self.ID = [ID]
        self.gossipsneeded=totalgossips
        self.stopindex = 0
        self.currentstop = self.route[self.stopindex]
        self.routelen = len(self.route)
        self.bonus = bonus
        self.waitone = False

    def gossip(self, otherID):
        for oID in otherID:
            if oID not in self.ID:
                self.ID.append(oID)
                self.gossips+=1
                if self.bonus:
                    self.waitone = True

    def details(self):
        print self.route, self.ID, self.currentstop, self.gossips

    def nextstop(self):
        self.stopindex+=1
        if self.waitone:
            self.stopindex-=1
            self.waitone = False
        self.stopindex%=self.routelen
        self.currentstop = self.route[self.stopindex]


    def gotthegoss(self):
        return self.gossips == self.gossipsneeded

    def stop(self, other):
        if self.currentstop == other.currentstop:
            self.gossip(other.ID)
        
 
def splitroutes(inpt):
    return [map(int,i.split()) for i in inpt.splitlines()]

def howmanystops(inpt, bonus=False):
    routes = splitroutes(inpt)
    drivers = []
    totaldrivers = len(routes)
    for i in xrange(totaldrivers):
        drivers.append(busdriver(routes[i], i, totaldrivers, bonus))
    stopsofar=0
    while (not all(d.gotthegoss()==True for d in drivers)) and (stopsofar<480):
        for i in xrange(totaldrivers):
            for j in xrange(totaldrivers):
                if i != j:
                    drivers[i].stop(drivers[j])
        for i in xrange(totaldrivers):
            drivers[i].nextstop()
        stopsofar+=1
    if stopsofar<480:
        return stopsofar
    else:
        return "never"
    
if __name__ == "__main__":
    assert howmanystops(input0) == 5
    assert howmanystops(input1) == "never"
    print howmanystops(input2)
    print howmanystops(input3)
    print "Bonuses:"
    # the bonus has drivers gossiping staying at their stop an extra min
    print howmanystops(input0, True)
    print howmanystops(input1, True)
    print howmanystops(input2, True)
    print howmanystops(input3, True)
