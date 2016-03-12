input1= """3
abcd
qwer
hjklo"""

input2= """4
edcf
bnik
poil
vybu"""

def getwordlist(filename):
    with open(filename) as file:
        return (file.read()).splitlines()

def process_input(input):
    input = input.splitlines()
    amount = int(input.pop(0))
    letters = input[:amount]

    return letters

def find_words(letters, wordlist):
    found_word = []
    #letters=list(letters)
    for word in wordlist:
        typable = True
        #split = list(word)
        for letter in word:
            if letter not in letters:
                typable = False
            
        if typable: found_word+=[word]

    return found_word
                
        
def find_biggest(words):
    largest = -1
    largest_list = []
    for word in words:
        if len(word) > largest: largest = len(word)

    for word in words:
        if len(word) == largest:
            largest_list.append(word)

    return largest_list

def broken_keyboard(working_keys, words_to_search):

    wordlist= getwordlist(words_to_search)
    letterlists = process_input(working_keys)

    typable_words = []
    for letters in letterlists:
        typable_words += [find_words(letters, wordlist)]

    print typable_words
    biggest = []
    for thingy in typable_words:
        biggest += find_biggest(thingy)
        
    print biggest

    output = []
    for i in xrange(0,len(letterlists)):
        output ="""With a broken keyboard that only has 
the letters '%s' working, you can type the following:
%r
The longest word/s being: 
%r""" %(letterlists[i], typable_words[i], biggest[i])

        write_output(str(output), "outputs/%s.txt"%letterlists[i])

def write_output(stuff_to_output, output_file):
    with open(output_file, 'w') as out_file:
        out_file.write(stuff_to_output)

if __name__ == "__main__":

    broken_keyboard(input1, "enable1.txt")
    broken_keyboard(input2, "enable1.txt")

