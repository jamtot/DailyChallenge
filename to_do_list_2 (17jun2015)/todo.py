from sys import argv
from collections import defaultdict
import re
todict = defaultdict(str)

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

def updateItem(item, newItem):
    with open(filename+".txt", 'r+') as todfile:
        text = todfile.read()
        text = re.sub(item+'\n', newItem+'\n', text)
        todfile.seek(0)
        todfile.write(text)
        todfile.truncate()

def viewList(*args):
    with open(filename+".txt") as todfile:
        lines = todfile.read().splitlines()
        for line in lines:
            print line

def clearList():
    with open(filename+".txt", 'w') as todfile:
        text = ''
        todfile.seek(0)
        todfile.write(text)
        todfile.truncate()

        
if __name__ == "__main__":
    clearList()
    addItem('Take a shower')
    addItem('Go to work')
    addItem('Buy a new phone')
    updateItem('Go to work', 'Go to work on time')
    viewList()
