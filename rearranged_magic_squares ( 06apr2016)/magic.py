input1 = """15 14  1  4
12  6  9  7
2 11  8 13
5  3 16 10"""

input2= """20 19 38 30 31 36 64 22
8 16 61 53 1 55 32 34
33 60 25 9 26 50 13 44
37 59 51 4 41 6 23 39
58 35 2 48 10 40 46 21
62 11 54 47 45 7 5 29
18 57 17 27 63 14 49 15
24 3 12 42 43 52 28 56"""

input3= """23 27 31 42 45 1 32 59
61 33 14 17 60 56 4 15
7 57 37 6 25 18 63 47
40 55 22 20 9 44 46 24
21 10 3 49 62 11 50 54
19 35 36 52 5 43 29 41
51 13 64 16 26 48 34 8
38 30 53 58 28 39 2 12"""
 
input4= """111 129 27 38 119 73 30 11 123 144 6 59
33 22 118 102 51 121 79 132 15 50 42 105
14 91 41 7 85 116 60 125 128 70 71 62
69 92 87 142 4 28 103 43 37 112 76 77
136 84 115 55 137 97 17 32 13 35 16 133
2 46 68 78 141 94 47 80 81 82 58 93
108 36 20 1 65 45 143 64 113 109 56 110
99 18 12 49 100 114 72 66 107 5 138 90
95 83 57 135 67 53 31 19 39 126 140 25
8 86 130 88 44 21 131 63 101 29 117 52
89 61 75 48 54 74 23 96 104 98 124 24
106 122 120 127 3 34 134 139 9 10 26 40"""
 
input5= """38 55 128 137 24 60 62 25 54 27 119 141
81 111 51 18 73 82 64 94 19 133 29 115
72 11 59 61 124 136 95 65 76 66 101 4
44 12 126 112 30 74 88 58 79 127 49 71
102 97 125 28 67 23 48 68 142 32 122 16
21 14 103 87 139 45 107 77 36 131 109 1
52 118 34 96 63 6 33 120 104 13 121 110
113 143 10 35 53 46 5 89 123 138 37 78
99 15 86 42 41 92 100 69 90 3 93 140
132 57 40 50 7 117 83 39 84 75 56 130
85 129 106 134 114 98 80 22 20 9 26 47
31 108 2 70 135 91 105 144 43 116 8 17"""

from itertools import permutations

def gettinglines(sqr):
    sqr = sqr.splitlines()
    lines = [line.split() for line in sqr]
    return lines

def getmagic(sqr):
    sqrows = gettinglines(sqr)
    rowlen = len(sqrows)# cos it's a square
    perms = range(rowlen)
    sum2get = sum(map(int,sqrows[0]))
    goodpers = []
    for per in permutations(perms):
        sum1 = 0
        sum2 = 0
        i = 0
        for p in per:
            sum1+=int(sqrows[p][i])
            sum2+=int(sqrows[p][(rowlen-1)-i])
            i+=1
        if sum1 == sum2 == sum2get:
            goodpers.append(per)

    print "There are %d ways to make magic."%len(goodpers)
    squares = []
    for per in goodpers:
        squares.append("MAAAAAAGIIIIIIIIC"+"\n".join(["".join(str(sqrows[p])) for p in per]))
    return squares
    

if __name__ == "__main__":
    print getmagic(input1)
    print getmagic(input2)
    print getmagic(input3)
    #print getmagic(input4)
    #print getmagic(input5)

