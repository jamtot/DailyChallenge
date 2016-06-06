from sys import argv
from collections import defaultdict
import re

filename='todo'
if len(argv)>1:
    filename=argv[1]

def addItem(item, *cats):
    with open(filename+".txt", 'r+') as todfile:
        text = todfile.read()
        if len(text) > 0:
            todict = eval(text.replace("<type 'list'>", 'list'))
        else:
            todict = defaultdict(list)
        for cat in cats:
            todict[cat].append(item)    
        todfile.seek(0)
        todfile.write(str(todict))
        todfile.truncate()

def deleteItem(item):
    with open(filename+".txt", 'r+') as todfile:
        text = todfile.read()
        text = re.sub("'"+item+"'"+'[,]?', '', text)
        todict = eval(text.replace("<type 'list'>", 'list'))
        torem = []
        for cat in todict:
              if len(todict[cat]) < 1:
                    torem.append(cat)
        if torem:
            for cat in torem:
                todict.pop(cat, None)
        todfile.seek(0)
        todfile.write(str(todict))
        todfile.truncate()
        
def updateItem(item, newItem):
    with open(filename+".txt", 'r+') as todfile:
        text = todfile.read()
        text = re.sub(item, newItem, text)
        todfile.seek(0)
        todfile.write(text)
        todfile.truncate()

def viewList(*args):
    with open(filename+".txt") as todfile:
        
        text = todfile.read()
        todict = eval(text.replace("<type 'list'>", 'list'))

        if not args:
            for cat in todict:
                print '%s'%cat
                for todo in todict[cat]:
                    print '- '+todo
        else:
            cats = [cat for cat in todict if cat in args]
            todos = []
            for cat in cats:
                for tds in todict[cat]:
                    if tds not in todos:
                        todos.append(tds)
            catitle = ''
            for cat in cats: 
                catitle+="%s & "%cat
            catitle=catitle[:-3] # removes the ' & ' on the last cat
            print catitle
            for td in todos:
                print '- '+td
            
def clearList():
    with open(filename+".txt", 'w') as todfile:
        text = ''
        todfile.seek(0)
        todfile.write(text)
        todfile.truncate()

        
if __name__ == "__main__":
    clearList()
    addItem('Go to work','Programming')
    addItem('Create Sine Waves in C', 'Music', 'Programming')
    addItem('A pixel is not a pixel is not a pixel','Programming')
    addItem('The Scheme Programming Language', 'Programming')
    addItem('Memory in C', 'Programming')
    addItem('This will be removed', 'ToRemove')
    addItem('The Scheme Programming Language', 'Programming')
    addItem('Haskell\'s School of Music', 'Programming', 'Music')
    addItem('Algorithmic Symphonies from one line of code','Music', 'Programming')
    addItem('Modes in Folk Music', 'Music')
    addItem('The use of the Melodic Minor Scale', 'Music')
    print
    viewList()
    updateItem('Create Sine Waves in C', 'Create Sine Waves in Python')
    deleteItem('This will be removed')
    print
    viewList('Programming')
    print
    viewList('Music')
    print
    viewList('Programming','Music')
    print
    viewList()
