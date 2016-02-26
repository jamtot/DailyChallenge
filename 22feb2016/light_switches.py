"""
When you were a little kid, was indiscriminately flicking light switches super fun? I know it was for me. Let's tap into that and try to recall that feeling with today's challenge.
Imagine a row of N light switches, each attached to a light bulb. All the bulbs are off to start with. You are going to release your inner child so they can run back and forth along this row of light switches, flipping bunches of switches from on to off or vice versa. The challenge will be to figure out the state of the lights after this fun happens.
"""

import time

exampleInput = """10
3 6
0 4
7 3
9 9"""

challengeInput = '''1000
616 293
344 942
27 524
716 291
860 284
74 928
970 594
832 772
343 301
194 882
948 912
533 654
242 792
408 34
162 249
852 693
526 365
869 303
7 992
200 487
961 885
678 828
441 152
394 453'''

bonusFile = open("lots_of_switches.txt")
bonusInput = bonusFile.read()

def switched(input):
    start = time.clock()
    linesProcessed = 0
    lightlist = input.split('\n')[:1]
    lights = int(lightlist[0])
    switches = [False] * lights
    #print switches
    
    inputLines = input.split('\n')[1:]
    for line in inputLines:
        linesProcessed+=1
        #print line
        nums = [int(n) for n in line.split()]
        minimum = min(nums)
        maximum = max(nums)
        #print "Min is %s and max is %s." % (mininum, maximum)
        for light in range(minimum,maximum+1): # inclusive to the upper range
            switches[light] = not switches[light] # change to what you're not
        #print switches
        print linesProcessed 

    sum = 0
    for bulb in switches:
        if bulb:
            sum+=1
    print "There are %d lights on." % sum
    end = time.clock()
    print end-start
    return sum

switched(exampleInput)
switched(challengeInput)
switched(bonusInput)
