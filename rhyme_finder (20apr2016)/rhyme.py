import re

def get_dictionary(filename):
    """returns a dictionary with the word being the key to it's
        phonetic pronunciation"""
    rhymedict={}
    with open(filename) as wordfile:
        lines=wordfile.read().splitlines()
        for line in lines:
            line=line.split("  ")
            rhymedict[line[0]]=line[1].split()
    return rhymedict

def find_rhymes(word,rdict, stress=True, tofile=False):
    """finds words and how many phenomes match"""
    word = word.upper()
    if word in rdict:
        rhymes=[]
        phenomes = rdict[word]
        if not stress:
            phen = "*".join(phenomes)
            phen = re.sub("[0-9]", "", phen)
            phenomes = phen.split("*")
        for i in xrange(len(phenomes)):
            for keys in sorted(rdict):
                currhyme = len(phenomes)-i
                curphen = rdict[keys]
                if not stress:#in
                    phen = "*".join(rdict[keys])
                    phen = re.sub("[0-9]", "", phen)
                    curphen = phen.split("*")
                if phenomes[i:]==curphen[-currhyme:]:
                    if currhyme>1:
                        if (keys,rdict[keys]) not in rhymes:
                            rhymes.append((keys,rdict[keys]))
                            rhymetext="[%d] %s - %r"%(currhyme,keys,rdict[keys])
                            print rhymetext
                            if tofile:
                                with open(word+".txt", 'a') as rhymefile:
                                    rhymefile.write(rhymetext+'\n')
        return rhymes
    
    else:
        return "Sorry, we don't have a rhyme for this"

if __name__ == "__main__":
    rdict=get_dictionary("cmudict-0.7b_modded.txt")
    while True:
        #find_rhymes(raw_input("> "), rdict)
        #find_rhymes(raw_input("> "), rdict, False)
        find_rhymes(raw_input("> "), rdict, True, True)
