def getfiletext(filename):
    with open(filename) as openfile:
        return openfile.read()

if __name__ == "__main__":
    # get the csv data
    text = getfiletext("presidents.txt")
    
