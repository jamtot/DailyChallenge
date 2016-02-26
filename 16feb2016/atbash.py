def cipher(input):
    output = ''
    for char in input:
        charOrd = ord(char) # get the numeric value of the character
        asciiCase = 0

        if (charOrd > 96 and charOrd < 123) or ( # if lowercase letter
                charOrd > 64 and charOrd < 91): # or uppercase letter
            if charOrd > 96: asciiCase = 97
            else: asciiCase = 65
            newAlphaPos = 25-(charOrd - asciiCase)
            newCharOrd = newAlphaPos + asciiPos
            char = chr(newCharOrd) # get the character using the new value
    
        output+=char # add the character to the output string
    print output

cipher("foobar")
cipher("wizard")
cipher("/r/dailyprogrammer")
cipher("gsrh rh zm vcznkov lu gsv zgyzhs xrksvi")
cipher("Gsrh Rh Kivhviezgrlm!")
