def garland(word):
    printy=0
    i=0
    while True:
        if word[i:] == word[:-i]:
            return len(word[:-i])
        i+=1

if __name__ == "__main__":
    assert garland("programmer") == 0
    assert garland("ceramic") == 1
    assert garland("onion") == 2
    assert garland("alfalfa") == 4
