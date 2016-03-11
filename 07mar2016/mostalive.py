def getfiletext(filename):
    with open(filename) as openfile:
        return openfile.read()

if __name__ == "__main__":
    # get the csv data
    text = getfiletext("presidents.txt")
    textlines = text.splitlines()
    # remove the top line, stating what the values are
    infoline = textlines.pop(0)
    presidents, births, deaths = [], [], []
    for line in textlines:
        currentline = line.split(',')
        presidents.append(currentline[0])
        births.append((currentline[1].split())[-1])
        if len(currentline[3].split()) > 2:
            deaths.append((currentline[3].split())[-1])
        else: deaths.append("2016") # not dead yet

    yearDict = {}
    countDict = {}
    earliest = latest = 2016
    for year in births:
        earliest = min(earliest, int(year))
    
    for x in xrange(earliest, latest+1):
        yearDict['%d' % x] = []
        countDict['%d' % x] = 0

    index = 0
    for pres in presidents:
        for x in xrange(int(births[index]), int(deaths[index])+1):
            yearDict['%d'%x].append(pres)
            countDict['%d'%x]+=1
        index+=1

    maxcount = 0
    for num in countDict:
        maxcount = max(countDict[num], maxcount)

    print "Years with most (%d) presidents:" % maxcount
    for num in sorted(countDict):
        if maxcount == countDict[num]:
            print num,
    
