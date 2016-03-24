# author user: fibonacci__
# https://www.reddit.com/user/fibonacci__

from collections import defaultdict

input1 = '''Circle,4
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
Bamboo,9'''

input2 = '''Circle,4
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
Bamboo,9'''

input3 = '''Circle,4
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
Circle,6'''

input4 = '''Circle,4
Circle,5
Circle,6
Bamboo,1
Bamboo,2
Bamboo,3
Character,2
Character,2
Character,2
Character,2
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9'''

input5 = '''Circle,4
Circle,5
Circle,6
Bamboo,1
Bamboo,2
Bamboo,3
Character,2
Character,2
Character,2
Character,2
Circle,1
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9'''

input6 = '''Circle,4
Circle,5
Circle,6
Bamboo,1
Bamboo,2
Bamboo,3
Red Dragon
Red Dragon
Red Dragon
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9'''

input7 = '''Circle,4
Circle,5
Circle,6
Bamboo,1
Bamboo,2
Bamboo,3
Red Dragon
Green Dragon
White Dragon
Circle,1
Circle,1
Bamboo,7
Bamboo,8
Bamboo,9'''

input8 = '''Circle,4
Circle,4
Character,5
Character,5
Bamboo,5
Bamboo,5
Circle,5
Circle,5
Circle,7
Circle,7
Circle,9
Circle,9
Circle,9
Circle,9'''

input9 = '''Circle,1
Circle,1
Circle,1
Circle,2
Circle,3
Circle,4
Bamboo,1
Bamboo,2
Bamboo,3
Bamboo,3
Bamboo,3
Bamboo,3
Bamboo,4
Bamboo,5'''

input10 = '''Circle,4
Circle,4
Character,5
Character,5
Bamboo,5
Bamboo,5
Circle,5
Circle,5
Circle,7
Circle,7
Circle,8
Circle,8
Circle,9
Circle,9'''

input11 = '''Circle,1
Circle,2
Circle,2
Circle,3
Circle,3
Circle,4
Circle,5
Circle,6
Circle,7
Circle,8
Circle,8
Circle,8
Circle,9
Circle,9
'''

def mahjong(input):
    input = input.split()
    suits = defaultdict(list)
    for i in input:
        suit, value = i.split(',') if ',' in i else (i, '0')
        suits[suit] += [int(value)]

    pair, quad = 0, 0
    for values in suits.values():
        values.sort()
        print "VALUES",values
        while True:
            temp = sorted(values, key = lambda x: values.count(x))
            print "TEMP",temp
            for v in temp:
                if any(i not in values for i in xrange(v, v + 3)):
                    continue
                for i in xrange(v, v + 3):
                    print "REMOVING",i
                    values.remove(i)
                temp = sorted(values, key = lambda x: values.count(x))
                break
            if not temp or v == temp[-1]:
                break
        for v in list(set(values)):
            print "V",v
            v_count = values.count(v)
            if not v_count:
                continue
            if v == 0 and v_count not in [2, 3]:
                return 'Not a winning hand'
            if v_count == 2:
                pair += 1
            elif v_count == 4:
                quad += 1
            if v_count in [2, 3, 4]:
                values = [i for i in values if i != v]
        if values:
            return 'Not a winning hand'
    if quad and pair not in [1, 7 - quad * 2]:
        return 'Not a winning hand'
    return 'Winning hand'

print mahjong(input1)
print mahjong(input2)
print mahjong(input3)
print mahjong(input4)
print mahjong(input5), ',not winning'
print mahjong(input6)
print mahjong(input7), ',not winning'
print mahjong(input8)
print mahjong(input9)
print mahjong(input10)
print mahjong(input11)
