comp_input="""64 64
 abcdefghijklmnopqrstuvwxyz.,ABCDEFGHIJKLMNOPQRSTUVWXYZ-()"';:/?!1234567890@%+*^#<>{}[]&_`|\\"""

input1="44 47 55 68 126 indexes in the ascii table are:"

base64indextable="""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"""

padding_symbol = '='

to_encode="""Man is distinguished, not only by his reason, but by this singular passion from
other animals, which is a lust of the mind, that by a perseverance of delight
in the continued and indefatigable generation of knowledge, exceeds the short
vehemence of any carnal pleasure."""

to_decode="""TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbQpvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodAppbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydAp2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="""

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

def decode(encoded_text, index_table, padder):
    output = ""
    if (len(encoded_text)%4!=0):
        print "Not a valid input, compadre."
    else:
        for i in xrange(0, len(encoded_text), 4):
            curbin = ""

            for l in encoded_text[i:i+4]:
                if l != padder:
                    binletter6 = "{0:b}".format(index_table.index(l)).zfill(6)
                    curbin+=binletter6

            for i in xrange(0, len(curbin), 8):
                output+=chr(int(curbin[i: i+8], 2))

    return output
        
if __name__ == "__main__":
    print encode(to_encode, base64indextable, padding_symbol)
    print decode(to_decode, base64indextable, padding_symbol)
    
