from random import randint

def shuffle(shufflist):
    shufflist = shufflist.split()
    newlist = []
    while len(shufflist) > 0:
        newlist.append(shufflist.pop(randint(0,len(shufflist)-1)))
    return newlist

if __name__ == "__main__":
    print shuffle("1 2 3 4 5 6 7 8 ")
    print shuffle("apple blackberry cherry dragonfruit grapefruit kumquat mango nectarine persimmon raspberry raspberry")
    print shuffle("a e i o u")
