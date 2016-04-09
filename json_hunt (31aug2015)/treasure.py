import json
from pprint import pprint
from collections import defaultdict

def GetData(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

def SearchData(data, term, path):
    if type(data) is dict:
        for key in data.keys():
            found = SearchData(data[key], term, path)
            if found: 
                path.append(key)
                return True
    elif type(data) is list:
        for i in xrange(len(data)):
            found = SearchData(data[i], term, path)
            if found: 
                path.append(i)
                return True
    else:
        if term == data:
            return True
    return False

def GetPath(term, filename):
    path = []
    SearchData(GetData(filename), term, path)
    if path == []: 
        print "Term not found."
    else:
        print "".join([" -> "+str(s) for s in reversed(path)])

if __name__ == "__main__":
    GetPath("dailyprogrammer","input0.json")
    GetPath("dailyprogrammer","input1.json")
    GetPath("dailyprogrammer","challenge1.json")
    GetPath("dailyprogrammer","challenge2.json")
    GetPath("non-existant","challenge2.json")

    """ outputs
     -> favoriteWebsites -> 1
     -> caki -> cyd -> qembsejm -> 1
     -> axvjf -> tskgrsi -> 0 -> ozr -> 0 -> 1 -> 0
     -> myutkqsfzw -> 4 -> fxeu -> 1 -> 0 -> 1 -> 2 -> 7 -> ocjcjokh -> xqfbrz -> 0
    Term not found.
    """
