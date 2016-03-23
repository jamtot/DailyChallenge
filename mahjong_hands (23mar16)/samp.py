input1="""14
Circle,4
Circle,5
Circle,6
Bamboo,1
Bamboo,2
Bamboo,3
Character,2
Character,2
Character,2
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9"""

input2="""14
Circle,4
Bamboo,1
Circle,5
Bamboo,2
Character,2
Bamboo,3
Character,2
Circle,6
Character,2
Circle,1
Bamboo,8
Circle,1
Bamboo,7
Bamboo,9"""

input3="""14
Circle,4
Circle,5
Circle,6
Circle,4
Circle,5
Circle,6
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9
Circle,4
Circle,5
Circle,6"""

# another users solution, which is not really working properly,
# was trying to help them out by pointing out the faults in the code

def handy(input):
    from collections import defaultdict
    hand_str=input.splitlines()[1:]
    hand = defaultdict(list)
    for suit, value in map(lambda x: str.split(x, ","),hand_str):
        hand[suit].append(int(value))
    print hand
    for value_lst in hand.values():
        value_lst.sort()
        print "Top",value_lst
        i =0
        while i <len(value_lst) -2:
            if value_lst[i] +2 == value_lst[i+1] + 1 == value_lst[i+2]:
                print "Removing",value_lst[i:i+3]          
                value_lst[i:i+3] = []
                i=0
            i += 1
            print value_lst
        i = 0
        while i < len(value_lst) -2:
            if value_lst[i] == value_lst[i+1]:
                if value_lst[i] == value_lst[i+2]:
                    print "Removing",value_lst[i]
                    value_lst[i] = []
                    i=0
                print "Removing",value_lst[i:i+2]
                value_lst[i:i+2] = []
            i += 1
            print value_lst
        print value_lst
        print len(value_lst)
        print hand
        if not len(value_lst):
            print len(value_lst)
            print("Not a winning hand")
            exit()
    print("Winning hand")

handy(input1)
handy(input2)
handy(input3)
