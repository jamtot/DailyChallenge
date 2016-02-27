class funnyPlant(object):

    def __init__(self):
        self.fruits = 0

    def weekPass(self):
        self.fruits+=1

    def getFruit(self):
        return self.fruits

def feedPeeps(people, initialPlants):
    week = 1
    fruits = 0
    plants = []
    for i in range(initialPlants):
        plants.append(funnyPlant())

    while fruits < people:
        week+=1
        fruits = 0
        for i in range(len(plants)):
            plants[i].weekPass()
            fruits += plants[i].getFruit()
        for i in range(fruits):
            plants.append(funnyPlant())
    return week

print feedPeeps(15, 1)
print feedPeeps(200, 15)
print feedPeeps(50000, 1)
print feedPeeps(150000, 250)

# simplified version of the above version
def fnyPlnt(ppl, plnts):
    frts = 0
    wks = 1
    while frts < ppl:
        frts+=plnts
        plnts+=frts
        wks+=1
    return wks


print fnyPlnt(15, 1)
print fnyPlnt(200, 15)
print fnyPlnt(50000, 1)
print fnyPlnt(150000, 250)
