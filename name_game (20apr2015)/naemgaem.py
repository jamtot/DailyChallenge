import re
import subprocess

#got from http://stackoverflow.com/a/19058023/5991253
def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

def name_game(name):
    if len(name)<2: return "Stop that!"
    print
    #removes them pesky excamation points
    while name.endswith("!"):
        name=name[:-1]
    #makes sure name is displayed nicely
    name = name[0].upper()+name[1:].lower()
    
    return """%s %s bo%s,
Bonana fanna fo%s,
Fee fy mo%s,
%s!"""%(name,name,change(name,"B"),change(name,"F"),change(name,"M"),name)

def change(name,letter):
    if name.startswith(letter):
        return "-"+name[1:]
    if re.match(r"[AEIOU].*",name): name = name.lower()
    else:
        # remove front consonants
        while re.match(r"[^aeiouy].*",name):
            name=name[1:]
    return " "+letter+name

if __name__ == "__main__":
    print "Ctrl-Z to close."
    while True:
        print "Enter name to play the game: "
        gaem = name_game(raw_input())
        print gaem
        execute_unix("espeak '%s'"%gaem)
        print
