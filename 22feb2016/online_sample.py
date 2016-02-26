# a python solution presented by user fibonacci__ (https://www.reddit.com/user/fibonacci__)

import time

input1 = '''10
3 6
0 4
7 3
9 9'''

input2 = '''1000
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

with open('lots_of_switches.txt') as file:
    input3 = ''.join(file.readlines())

def switched(input):
    input = input.split('\n')[1:]
    lights = set()
    for i in input:
        i = map(int, i.split())
        lights.symmetric_difference_update(xrange(min(i), max(i) + 1))
    return len(lights)

def switched_bonus(input):
    start = time.clock()
    input = map(lambda x: sorted(map(int, x.split())), input.strip().split('\n')[1:])
    input = sorted([j for i in input for j in [(i[0], 0), (i[1], 1)]])
    total = 0
    for i, j in zip(input[::2], input[1::2]):
        #print "i is %r, j is %r" % (i, j)
        total += j[0] - i[0] + j[1] - i[1]
    end = time.clock()
    print end-start
    return total

print switched_bonus(input1)
print switched_bonus(input2)
print switched_bonus(input3)

"""
someone commented asking for explanation:

Can you explain the thought process behind the bonus speed optimizations please? I'm a bit confused on why you sorted the intervals, then subtracted the evens+1 from the odds.


fibonacci__ replied:

The idea is to find the difference between pairs of intervals of start and end indices. The intuition is that pairs of ranges will cancel out except at the ends where only one of the ranges will toggle the lights.
For example, [0,4] and [2,4] will toggle only [0,1] since the toggling of [2,4] will cancel out. Therefore, the number of lights toggled is (1 + 1) - 0 = 2. Similarly, [0,4] and [1,3] will only toggle [0,0] and [4,4]. The number of lights toggled is 1 - 0 + (4 + 1) - (3 + 1) = 2. The reason for adding 1 to the end of each range is to convert from a closed interval to a half-open interval for correct counting of lights, so [1,3] contains (3 + 1) - 1 = 3 lights instead of 3 - 1 = 2 lights which is incorrect.
Sorting the start and end indices is essential as it allows pairs to be processed at the non-overlapping ends of the ranges and to be processed in order from left to right so each range edge pair is accounted for at most once.
permalinkparent

reply:

That makes a lot of sense. In my head it's similar to a "NOT AND" statement in binary logic. I think you could remove your last zip and speed things up very slightly. Thank you!

light_input = [sorted([i for i in map(int, row.split())]) for row in txt.strip().split('\n')[1:]]   

my_input = sorted([j for i in light_input for j in [i[0], i[1]+1]])

print(sum(my_input[1::2]) - sum(my_input[::2]))
"""
