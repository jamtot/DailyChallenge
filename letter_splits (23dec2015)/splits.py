def makedict():
    #create a dictionary that matches numbers to corresponding letters
    return dict([(str(i-64), chr(i)) for i in xrange(ord('A'), ord('Z')+1)])
    
def getwords():
    with open("enable1.txt") as wordfile:
        words = wordfile.read().upper().splitlines()
        return words

def validate(lnput, wlist):
    minlen = 3 # MIN LENGTH FOR 'WORD'
    if lnput == '':#you're at the end
        return True
    for i in xrange(minlen, len(lnput)+1):
        if lnput[:i] in wlist:
            if validate(lnput[i:], wlist):
                return True
       
def search(ldict, wlist, lnput, validating=False, output=''):
    if lnput == '':# if you're at the end
        if validating:
            if validate(output, wlist):
                print output
        else:
            print output
        return
    if lnput[0] in ldict:
        search(ldict, wlist, lnput[1:], validating, output+ ldict[lnput[0]])
    if len(lnput) > 1 and lnput [0:2] in ldict:
        search(ldict, wlist, lnput[2:], validating, output + ldict[lnput[0:2]])

if __name__ == "__main__":
    letterdict = makedict()
    wordlist = getwords()
    search(letterdict, wordlist, "1234")
    search(letterdict, wordlist, "1234567899876543210")
    search(letterdict, wordlist, "10520")
    search(letterdict, wordlist, "1321205", True)
    search(letterdict, wordlist, "1252020518", True)
    search(letterdict, wordlist, "85121215231518124", True)
    #takes a veeeery long time
    #search(letterdict, wordlist, "81161625815129412519419122516181571811313518", True)
