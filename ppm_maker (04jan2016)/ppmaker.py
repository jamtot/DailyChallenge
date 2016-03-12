input1 = """5 3
point 0 0 255 0 0
line 100 100 100 0 2 2 4
rect 77 0 0 1 3 2 2"""

challengeInput = """400 300
rect 0 0 255 0 0 300 400
line 255 255 255 0 0 299 399
line 255 255 255 299 0 0 399
rect 200 200 0 100 150 100 100
point 0 0 0 150 200"""

def GetInputText(input):
    with open(input) as inputFile:
        return inputFile.read()

def GetDeets(input):
    inputLines = input.splitlines()
    picSize = (inputLines.pop(0)).split()
    #print picSize
    return picSize, inputLines
    
def processInputs(blankArray, inputLines, picSize):
    for line in inputLines:
        line = line.split()
        action = line.pop(0)
        if action == 'point':
            blankArray = point(line, picSize, blankArray)
        elif action == 'line':
            blankArray = bline(line, picSize, blankArray)
        elif action == 'rect':
            blankArray = rect(line, picSize, blankArray)
        else:
            pass

    return blankArray


def point(input, picSize, blankArray):
    # comes in the form [rgb][point] 0 0 255 1 1 [blue, @ point (1,1)]
    r, g, b = input.pop(0),input.pop(0),input.pop(0) 
    x,y = int(input.pop(0)),int(input.pop(0))
    width = int(picSize[0])
    index = (width*x)+y
    blankArray[index] = [r,g,b]
    return blankArray
    

def bline(input, picSize, blankArray):
    # draw line using bresenham's line algorithm
    r, g, b = input.pop(0),input.pop(0),input.pop(0) 
    x1,y1 = int(input.pop(0)),int(input.pop(0))
    x2,y2 = int(input.pop(0)),int(input.pop(0))
    dx,sx = abs(x2-x1), 1 if x1 < x2 else -1
    dy,sy = -abs(y2-y1), 1 if y1 < y2 else -1
    err = dx + dy
    width = int(picSize[0])
    while True:
        index = (width*(x1))+y1
        blankArray[index] = [r,g,b]
        if (x1 == x2 and y1 == y2):
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy

    return blankArray

def rect(input, picSize, blankArray):
    r, g, b = input.pop(0),input.pop(0),input.pop(0) 
    x,y = int(input.pop(0)),int(input.pop(0))
    w,h = int(input.pop(0)),int(input.pop(0))
    width = int(picSize[0])
    for i in xrange(w):
        for j in xrange(h):
            index = (width*(x+i))+(y+j)
            blankArray[index] = [r,g,b]
    return blankArray

def makeBlankArray(picSize):
    pixArray = list()
    for i in xrange( int(picSize[0])*(int(picSize[1])) ):
        pixArray.append(['0','0','0']) 
    return pixArray

def makeArrayString(pixelArray):
    stringArray = list()
    for i in xrange(len(pixelArray)):
        stringArray.append((' ').join(pixelArray[i]))
    stringArray = (' ').join(stringArray)
    return stringArray

def makeppm(picSize, stringArray, name):
    with open(name, 'w') as file:
        file.write("P3 %s %s 255 %s" % (picSize[0], picSize[1], stringArray))

def getOutput(input, outputName):
    picSize, inputLines = GetDeets(input)
    pixArray = makeBlankArray(picSize)
    pixArray = processInputs(pixArray, inputLines, picSize)
    stringArray = makeArrayString(pixArray)
    makeppm(picSize, stringArray, outputName)
    

if __name__ == '__main__':
    getOutput(input1, 'test1.ppm')
    getOutput(challengeInput, 'challenge1.ppm')
    
