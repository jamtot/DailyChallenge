import re

def name_game(name):
    if len(name)<2: return "Stop that!"
    print
    #removes them pesky excamation points
    while name.endswith("!"):
        name=name[:-1]
    #makes sure name is displayed nicely
    name = name[0].upper()+name[1:].lower()
    
    return """%s, %s bo%s,
Bonana fanna fo%s,
Fee fy mo%s,
%s!"""%(name,name,change(name,"B"),change(name,"F"),change(name,"M"),name)

def change(name,letter):
    
    if name.startswith(letter):
        return "-"+name[1:]
    # add space to stop losing the front if vowel
    name = re.sub(r"[AEIOU].*", " "+name.lower(), name)
    return " "+letter+name[1:]

if __name__ == "__main__":
    print "Ctrl-Z to close."
    while True:
        print "Enter name to play the game: "
        print name_game(raw_input())
        print
