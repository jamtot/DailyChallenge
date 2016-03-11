from collections import defaultdict, deque

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

def remove_word(word, letter_list):
    remove_list = letter_list
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

def recurse(word, words, letters, previous = []):
    # copy the letters
    muh_letters = letters[:]

    if len(previous)<1:
        ww = word
    else:
        ww = previous[0]

    # get the range for the letters beginning with 
    depth = len(previous)+1
    found = False
    
    start_index = 0
    end_index = len(words)
    for i in xrange(len(words)):
        if not found and ww[depth]==(words[i])[0]:
            start_index = i
            found = True
        elif found and ww[depth]!=(words[i])[0]:
            end_index = i
            break
 
    if end_index > len(words): end_index = len(words)
    

    # get the list of possible words
    words_to_use = []
    for i in xrange(start_index, end_index):
        words_to_use+=[words[i]]

    potentials = filter_list(muh_letters, words)
    #print potentials
    output = []
    for w in potentials:
        try:
            muh_letters = remove_word(w, muh_letters)
        except: break
        if (w == word):continue
        if len(word) == len(previous)+2:
            output+=[[word]+[w]]
        else:
            search = recurse(w, words, muh_letters, previous+[word])
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
    
    #print square_size
    #print letters_to_use

    filtered_list = filter_list(letters_to_use, words_by_length[square_size])
    #print filtered_list
    attemptys = []
    for word in filtered_list:
        attemptys += recurse(word, filtered_list, letters_to_use)
     
    output = []  
    letters = ("").join(letters_to_use)
    for attempt in attemptys:
        if ("").join(sorted(("").join(attempt))) == letters: 
            output += [attempt]
    print output        

#wordsquare("4 eeeeddoonnnsssrv", "enable1.txt")
wordsquare(input1, "enable1.txt")
#wordsquare(input2, "enable1.txt")
#wordsquare(input3, "enable1.txt")
#wordsquare(input4, "enable1.txt")
