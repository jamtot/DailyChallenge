input0="""1530 1600
1555 1645
1600 1630
1635 1715"""

input1="""1530 1600
1605 1630
1645 1725
1700 1730
1700 1745
1705 1745
1720 1815
1725 1810"""

input2="""1555 1630
1600 1635
1600 1640
1610 1640
1625 1720
1635 1720
1645 1740
1650 1720
1710 1730
1715 1810
1720 1740
1725 1810"""

input3="""1535 1610 Pokemon
1610 1705 Law & Order
1615 1635 ER
1615 1635 Ellen
1615 1705 Family Matters
1725 1810 The Fresh Prince of Bel-Air"""

input4="""1530 1600 Late Night With Conan O'Brien
1540 1620 Space Ghost Coast to Coast
1550 1610 3rd Rock from the Sun
1550 1630 Friends
1610 1705 Chicago Hope
1615 1705 Beavis and Butt-head
1625 1700 The Ren & Stimpy Show
1630 1655 Freaks and Geeks
1700 1720 Mad About You
1715 1745 Babylon 5
1720 1750 Married... with Children
1720 1750 Martin
1720 1805 seaQuest DSV
1725 1750 Walker, Texas Ranger"""

input5="""1535 1555 Batman: The Animated Series
1545 1605 The Magic School Bus
1645 1720 Dawson's Creek
1650 1745 Star Trek: Voyager
1710 1730 Space Ghost Coast to Coast
1715 1735 ER
1720 1745 Law & Order
1725 1755 Sports Night
1725 1755 Mad About You
1725 1815 Everybody Loves Raymond"""


def parseinput(inp):# with name
    """returns the times as a tuple of (start, end, name) in ints"""
    inp=inp.splitlines()
    if len(inp[0].split())>2:
        return [(int(i.split()[0]), int(i.split()[1]), ''.join(i.split(" ",2)[2:])) for i in inp]
    else:
        return [(int(i.split()[0]), int(i.split()[1])) for i in inp]


def findmost(shows, named=False, show=None, string='', 
                recordable='', recorded=0):
    """originally 2 seperate functions, but I smashed them together,
        doesn't take into account the amount recorded, just the 
        first best answer"""
    if len(shows)<1: # if you're out of shows
        if named:
            if len(string.splitlines()) > len(recordable.splitlines()): 
                recordable = string[:-1]
            return recordable
        else:
            recorded=max(recorded, len(string[:-1].split('%')))
            return recorded
    elif show==None: # if you haven't started yet
        for i in xrange(len(shows)):
            if named:
                recordable=findmost(shows[i:], named, shows[i],
                    string+str(shows[i][2])+'\n', recordable)
            else:
                recorded=findmost(shows[i:], named, shows[i], 
                    string+str(shows[i])+'%', recordable, recorded)
    elif show != None: # if you've got a previous show, add another
        for i in xrange(len(shows)):
            if show[1] <= shows[i][0]:
                if named:
                    recordable=findmost(shows[i+1:], named, 
                        shows[i], string+str(shows[i][2])+'\n', 
                        recordable, recorded)
                else:
                    recorded=findmost(shows[i+1:], named, 
                        shows[i], string+str(shows[i])+'%', 
                        recordable, recorded)

    if named:
        if len(string.splitlines()) > len(recordable.splitlines()): 
            recordable = string[:-1]
        return recordable
    else:
        recorded=max(recorded, len(string[:-1].split('%')))
        return recorded

if __name__ == "__main__":
    print findmost(parseinput(input0))
    print findmost(parseinput(input1))
    print findmost(parseinput(input2))
    print "-------"
    print findmost(parseinput(input3), True)
    print
    print findmost(parseinput(input4), True)
    print
    print findmost(parseinput(input5), True)
