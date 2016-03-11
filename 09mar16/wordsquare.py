from collections import defaultdict

input0 = "4 eeeeddoonnnsssrv"
input1 = "4 aaccdeeeemmnnnoo"
input2 = "5 aaaeeeefhhmoonssrrrrttttw"
input3 = "5 aabbeeeeeeeehmosrrrruttvv"
input4 = "7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy"

#-----------HARD MODE-----------
# (words might not be in dictionary)
hInput1 = "8 aaaaaaaabbccccddeeeeeeeeeeeiiiillllnnooooprrrrrrrrsssssssssstttv"
hInput2 = "8 aaaaaaabbceeeeeeeeeeeeiiiiiilllllmmnnnnrrrrrrsssssssstttttttwwyy"
hInput3 = "8 aaaaddddeeeeeeeeeeeeeeeeeeggiiiiiimmnnnnnooprrrrrrssssssssttttzz"
hInput4 = "8 aaaaccddddeeeeeeeeeeeeeeeeeeiiiiiilmmnnnnooprrrrrrssssssstttttzz"
hInput5 = "8 aaaaddddeeeeeeeeeeeeeeeeeeiiiiiimmnnnnnooprrrrrrssssssstttttvvzz"

"""
1) carboras, aperient, recaller, brassica, oilseeds, relievos, anecdote, strasses
2) crabwise, ratlines, atlantes, blastema, winterly, intertie, seemlier, essayers
3) nereides, energise, resonate, erotized, igniters, diazepam, esterase, seedsmen
4) nereides, eternise, relocate, erotized, inciters, diazepam, esterase, seedsmen
5) nereides, eternise, renovate, erotized, inviters, diazepam, esterase, seedsmen
"""
#------END HARD MODE------------

def can_remove(word, letter_list):
    can = True
    for letter in word:
        if letter in letter_list:
            # good
            pass
        else: can = False
    return can

def remove_word(word, letter_list):
    remove_list = letter_list[:]
    for letter in word:
        if letter in remove_list:
            remove_list.remove(letter)
    return remove_list

def filter_list(letter_list, word_list):
    filter_list = []    
    for word in word_list:
        good = True
        for letter in word:
            if letter not in letter_list:
                good = False
        if good: filter_list.append(word)
    return filter_list

def recurse(baseword, word, words, letters, previous = []):
    # copy the letters
    index = len(previous)+1
    words_to_use = words[ baseword[index] ]
    words_to_use = filter_list(letters, words_to_use)
    muh_letters = letters[:]
    #print muh_letters
    output = []
    for w in words_to_use:
        #if can_remove(w, muh_letters):
        #    muh_letters = remove_word(w, muh_letters)
        #else: break
        if (w == word):continue
        if index == len(word)-1:
            output+=[[word]+[w]]
        else:
            search = recurse(baseword, w, words, muh_letters, previous+[word])
            output+=[[word] + result for result in search]
    return output
            
def wordsquare(input, dictfile):
    # loading the wordlist by size    
    words_by_length = defaultdict(list)
    with open(dictfile, 'r') as file:
        words = [line.strip() for line in file]

    for word in words:
        words_by_length[len(word)].append(word)

    # taking in the input
    split_input = input.split()
    square_size = int(split_input[0])
    letters_to_use = list(split_input[1])

    filtered_list = filter_list(letters_to_use, words_by_length[square_size])

    words_by_letters = defaultdict(list)
    for word in filtered_list:
        words_by_letters[word[0]].append(word)

    start_letters = []
    for x in words_by_letters:
        start_letters += [x]

    trys = []
    for word in filtered_list:
        baseword = word[:]
        trys += recurse(baseword, word, words_by_letters, letters_to_use)
    #print trys
     
    output = []  
    letters = ("").join(sorted(("").join(letters_to_use)))
    #print letters
    for t in trys:
        if ("").join(sorted(("").join(t))) == letters: 
            output += [t]
    #print output 

    for l in output:
        listy = []

        for elem in l:
            listy+=[list(elem)]

        zippy = zip(*listy)
        zisty = []
        for i in xrange(len(zippy)):
            zisty+=[list(zippy[i])]

        if listy==zisty:
            print listy


wordsquare(input0, "enable1.txt")
wordsquare(input1, "enable1.txt")

# ----- crashes (runs out of memory) ------
#wordsquare(input2, "enable1.txt")
#wordsquare(input3, "enable1.txt")
#wordsquare(input4, "enable1.txt")
