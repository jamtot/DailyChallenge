import math

def radial(a,b,x,y,r,stringy):
    gridly = [[stringy[-1] for i in xrange(a)] for j in xrange(b)]
    stringy = stringy[:-1]
    grads = float(len(stringy))
    gradlen = r/grads
    for i in xrange(len(gridly)):
        for j in xrange(len(gridly[0])):
            dist = math.sqrt((i-x)**2+(j-y)**2)
            if dist<r:
                gridly[i][j]=stringy[int(dist/gradlen)]
            print gridly[i][j],
        print

def linear(a,b,x1,y1,x2,y2,stringy):
    minX,maxX = min(x1,x2),max(x1,x2)
    minY,maxY = min(y1,y2),max(y1,y2)
    gridly = [[" " for i in xrange(a)] for j in xrange(b)]
    grads = float(len(stringy))
    totes=math.sqrt((x1-x2)**2+(y1-y2)**2)
    gradlen = totes/grads
    for i in xrange(len(gridly)):
        for j in xrange(len(gridly[0])):
            x3=float(i)
            y3=float(j)
            k = ((y2-y1) * (x3-x1) - (x2-x1) * (y3-y1)) / ((y2-y1)**2 + (x2-x1)**2)
            xL = x3 - k * (y2-y1)
            yL = y3 + k * (x2-x1)
            dist = math.sqrt((x1-xL)**2+(y1-yL)**2)
            if dist<totes and (minX<=xL<=maxX) and (minY<=yL<=maxY):
                gridly[i][j]=stringy[int(dist/gradlen)]
            print gridly[i][j],
        print

if __name__ == "__main__":
    radial(40, 30, 20, 15, 20," .,:;xX&@")
    radial(40, 40,-10, 20, 60, "aaabcccdeeefggg")
    linear(60,30,30,30,0,0," '\"^+$")
    #radial(41, 41, 20, 20, 8,"nahtanoj ")
