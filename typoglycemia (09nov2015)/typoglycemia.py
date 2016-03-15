input = """According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, 
the only important thing is that the first and last letter be in the right place. 
The rest can be a total mess and you can still read it without a problem.
This is because the human mind does not read every letter by itself, but the word as a whole. 
Such a condition is appropriately called Typoglycemia."""

import random

def typoglyceme(input):
    """takes a word and scrambles it between the first and last letter"""
    if "'" in input:
        split = input.split("'")
        scrambled = []
        for s in split:
            scrambled += [typoglyceme(s)]
        return ("'").join(scrambled)
    elif "ypoglycemia" in input:
    # don't scramble that word
        return input
    elif "," in input:
        commaless = input.split(",")
        commaless = typoglyceme(commaless.pop(0))
        return ("").join([str(commaless), ","])
    elif "." in input:
        commaless = input.split(".")
        commaless = typoglyceme(commaless.pop(0))
        return ("").join([str(commaless), "."])
    else:
        if len(input) > 3:
            jumbled = []
            #take the first letter
            input = list(input)
            # take first letter
            jumbled.append(input.pop(0))
            length = len(input)
            for i in xrange(length-1):
                rand = random.randint(0,len(input)-2)
                # make sure no letter is placed where it started
                while rand==i:
                    rand = random.randint(0,len(input)-2)
                # pop out of input, and append to jumbled
                jumbled.append(input.pop(rand))
            # take last letter
            jumbled.append(input.pop(0))
            # join em up
            jumbled = ("").join(jumbled)
            return jumbled
        else: return input
            
def split_input(input):
    input = input.splitlines()
    output = []
    for line in input:
        line = line.split()
        processed = map(typoglyceme, line)
        processed = (" ").join(processed)
        output+=processed+"\n"
        output = ("").join(output)
    return output
        
"""print typoglyceme("condition")
print typoglyceme("According")
print typoglyceme("University,")
print typoglyceme("doesn't")       
print typoglyceme("team")""" 

print "INPUT:"
print input
print "-------"
print "OUTPUT:"
print split_input(input)
