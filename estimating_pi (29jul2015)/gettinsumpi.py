from pygame import image

def getmypi(filename):
    circpic=image.load(filename)
    picdimensions=circpic.get_size()
    x1,x2=picdimensions[0],0
    y1,y2=picdimensions[1],0
    areainpix=0
    for x in xrange(picdimensions[0]):
        for y in xrange(picdimensions[1]):
            if circpic.get_at((x,y)) == (0,0,0,255):
                areainpix+=1
                if x<x1: x1=x
                if x>x2: x2=x
                if y<y1: y1=y
                if y>y2: y2=y
        
    #pi = area/r^2
    rad1=(float(x2)-float(x1))/2.0
    rad2=(float(y2)-float(y1))/2.0
    mypi = float(areainpix)/(rad1*rad2)
    return mypi

if __name__ == "__main__":
    print getmypi("CIRCLE1.png")
    print getmypi("CIRCLE2.png")
    # challenge part not implemented
    # print getmypi("TRICKYDICKY.png")
