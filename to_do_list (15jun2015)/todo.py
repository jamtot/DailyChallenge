from sys import argv
import re

filename='todo'
if len(argv)>1:
    filename=argv[1]

def addItem(item):
    with open(filename+".txt", 'a') as todfile:
        todfile.write(item+'\n')

def deleteItem(item):
    with open(filename+".txt", 'r+') as todfile:
        text = todfile.read()
        text = re.sub(item+'\n', '', text,1)
        todfile.seek(0)
        todfile.write(text)
        todfile.truncate()

def deleteAllItem(item):
    with open(filename+".txt", 'r+') as todfile:
        text = todfile.read()
        text = re.sub(item+'\n', '', text)
        todfile.seek(0)
        todfile.write(text)
        todfile.truncate()

def viewList():
    with open(filename+".txt") as todfile:
        lines = todfile.read().splitlines()
        for line in lines:
            print line
        

if __name__ == "__main__":
    addItem('Take a shower')
    addItem('Go to work')
    viewList()
    addItem('Buy a new phone')
    deleteItem('Go to work')
    viewList()
