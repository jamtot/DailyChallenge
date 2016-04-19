from math import log
from collections import Counter

def entropy(string):
    # returns a dictionary of each character
    # and it's frequency
    counter = Counter(string) 
    return -1 * sum(i/float(len(string)) * log(i/float(len(string)),2) for i in counter.values())

if __name__ == "__main__":
    assert float("%.5f"%entropy("1223334444"))==1.84644
    assert float("%.5f"%entropy("Hello, world!"))==3.18083

    print entropy("122333444455555666666777777788888888")
    print entropy("563881467447538846567288767728553786")
    print entropy("https://www.reddit.com/r/dailyprogrammer")
    print entropy("int main(int argc, char *argv[])")


