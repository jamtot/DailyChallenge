comp_input="""64 64
 abcdefghijklmnopqrstuvwxyz.,ABCDEFGHIJKLMNOPQRSTUVWXYZ-()"';:/?!1234567890@%+*^#<>{}[]&_`|\\"""

input1="44 47 55 68 126 indexes in the ascii table are:"

base64indextable="""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"""

padding_symbol = '='

input2="""Man is distinguished, not only by his reason, but by this singular passion from
other animals, which is a lust of the mind, that by a perseverance of delight
in the continued and indefatigable generation of knowledge, exceeds the short
vehemence of any carnal pleasure."""

def encode(input_text, index_table, padder):
    output = ""
    pads=0
    for i in xrange(0, len(input_text), 3):
        curbin = ""
        for l in input_text[i:i+3]:
            binletter8 = ("{0:b}".format(ord(l)).zfill(8))
            curbin+=(binletter8)

        for i in xrange(0, len(curbin), 6):
            while len(curbin[i: i+6]) < 6:
                curbin+='0'
            index = int(curbin[i: i+6], 2)
            output+=index_table[index]

        pads+=4-(len(curbin)/6)
    output+=padder*pads

    return output
        
if __name__ == "__main__":
    print encode(input2, base64indextable, padding_symbol)
    
