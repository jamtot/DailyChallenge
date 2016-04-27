input1="""billowy
biopsy
chinos
defaced
chintz
sponged
bijoux
abhors
fiddle
begins
chimps
wronged"""

def alpahbetical(word):
    reversal = (ord(word[0]) > ord(word[1]))
    if word == ''.join( sorted(list(word), reverse=reversal) ):
        if reversal:
            return "%s REVERSE ORDER"%word
        else:
            return "%s IN ORDER"%word
    return "%s NOT IN ORDER"%word

if __name__ == "__main__":
    words = input1.splitlines()
    for word in words:
        print alpahbetical(word)

""" output
billowy IN ORDER
biopsy IN ORDER
chinos IN ORDER
defaced NOT IN ORDER
chintz IN ORDER
sponged REVERSE ORDER
bijoux IN ORDER
abhors IN ORDER
fiddle NOT IN ORDER
begins IN ORDER
chimps IN ORDER
wronged REVERSE ORDER
"""
