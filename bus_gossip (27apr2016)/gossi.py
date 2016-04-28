input0="""3 1 2 3
3 2 3 1 
4 2 3 4 5"""

input1="""2 1 2
5 2 8"""

class busdriver(object):
    def __init__(self, route, ID, gossip=1):
        self.route = route
        self.gossip = gossip
        self.ID = [ID]

    def gossip(self, otherID):
        for oID in otherID:
            if oID not in self.ID:
                self.ID.append(oID)
                self.gossip+=1

    def details():
        print self.route, self.ID

    def nextstop():
        pass
        

def splitroutes(inpt):
    return [map(int,i.split()) for i in inpt.splitlines()]

def howmanystops(inpt):
    routes = splitroutes(inpt)
    drivers = []
    for i in xrange(len(routes)):
        drivers.append(busdriver(routes[i], i))
    
    
if __name__ == "__main__":
    howmanystops(input0)
