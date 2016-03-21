# no error detection

input0="7851"
input1="219.45.143.143"

keypad = [["1","2","3"],
          ["4","5","6"],
          ["7","8","9"],
          [".","0"]]

def get_pos(key):
    for y in xrange(len(keypad)):
        for x in xrange(len(keypad[y])):
            if key == keypad[y][x]:
                return x,y

def get_dist(input):
    dist=0
    for i in xrange(len(input)-1):
        x1,y1 = get_pos(input[i])
        x2,y2 = get_pos(input[i+1])
        dist+=((x2-x1)**2+(y2-y1)**2)**0.5
    return round(dist,2)

print get_dist(input0)
print get_dist(input1)
