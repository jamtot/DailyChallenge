input = """chat.freenode.net:6667
chefbot
chefbot
Ed Sheeran
#rdpPONG,#gg
Hi, have you seen Chef?"""
#,#botters-test,#reddit-dailyprogrammer

import socket
import random

def send(socket,msg):
    print "out->", msg
    socket.send(msg+"\r\n")

lols = ["lol", "kek", "lel", "zozzle", "bazinga", "topkek",
            "zim zam flim flam", "olo", "lols", "wew lad", "memes", "loooool",
        "lolololol", "boingy"]

chefs = ["Did I hear Chef?", "86% on Rotten Tomatoes, baby!", "Jon Favreau, son!",
            "El Jefe!", "I will buy a food truck!", "I own Chef on Blu-Ray.", "Move over Iron Man, Chef's here.", "Chef's pretty good."]

# using an iterative factorial so there's no deptherror
def ifac(n):
    minus = False
    if n < 0:
        n=n*-1
        minus=True
    for i in xrange(n-1, 1, -1):
        n*=i
    if minus:
        n*=-1
    return n

# this will only go 998 deep, usually 999 deep
def fac(n):
    if n < 0:
        n=n*-1
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def make_connection(input):

    server, nick, user, name, channels, message = input.splitlines()
    chans = channels.split(",") if "," in channels else channels 
    
    server, port = server.split(":")
    server_name = "*"
    user_mode = 0
    s = socket.socket()
    s.connect((server, int(port)))
    print "connected"

    nickmsg = "NICK %s" % nick
    usermsg = "USER %s %d %s :%s" % (user, user_mode, server_name, name)  
    send(s, nickmsg)
    send(s, usermsg)
    print "initial details sent"
    received = ""
    while True:
        if "\r\n" not in received:
            received += s.recv(512)
        line, received = received.split("\r\n", 1)
        print line
        line = line.split()

        if line[1] == "376":
            joinmsg="JOIN %s"%channels
            send(s, joinmsg)

        elif line[1]=="JOIN" and line[0].split("!")[0][1:] == nick:
            hellomsg="PRIVMSG %s :%s"%(line[2],message)#the channel
            send(s, hellomsg)

        elif ":knivesdown" in line[3:]:
                chefmsg = "PRIVMSG %s :COOKED UP A STROM"%(line[2])
                send(s, chefmsg) 
                send("QUIT") 
                socket.close()

        # if "PRIVMSG ... nick:"           
        elif line[1] == "PRIVMSG" and nick + ":" in line[3]:
            # split off the name, then remove the ':' before it
            sender = line[0].split("!")[0][1:]
            if line[2] in chans or line[2] in nick:
                to = line[2] if line[2] in chans else sender
                if len(line)>4:
                    if line[4] == "sum":
                        try:
                            total = sum(map(int, line[5:]))
                            summsg = "PRIVMSG %s :%s: The sum is: %d"%(to, sender, total)
                            send(s, summsg)
                        except ValueError:
                            errormsg = "PRIVMSG %s :%s: ValueError"%(to, sender)
                            send(s, errormsg)
                    elif line[4] == "diff":
                        try:
                            total = reduce(lambda x,y: x-y, map(int,line[5:]))
                            diffmsg = "PRIVMSG %s :%s: The diff is: %d"%(to, sender, total)
                            send(s, diffmsg)
                        except ValueError:
                            errormsg = "PRIVMSG %s :%s: ValueError"%(to, sender)
                            send(s, errormsg)
                    elif line[4] == "mult":
                        try:
                            total = reduce(lambda x,y: x*y, map(int,line[5:]))
                            multmsg = "PRIVMSG %s :%s: The mult is: %d"%(to, sender, total)
                            send(s, multmsg)
                        except ValueError:
                            errormsg = "PRIVMSG %s :%s: ValueError"%(to, sender)
                            send(s, errormsg)
                    elif line[4] == "div":
                        try:
                            total = reduce(lambda x,y: x/y, map(int,line[5:]))
                            divmsg = "PRIVMSG %s :%s: The div is: %d"%(to, sender, total)
                            send(s, divmsg)
                        except ValueError:
                            errormsg = "PRIVMSG %s :%s: ValueError"%(to, sender)
                            send(s, errormsg)
                        except ZeroDivisionError:
                            errormsg = "PRIVMSG %s :%s: SUCK IT!"%(to, sender)
                            send(s, errormsg)

                    elif line[4] == "lol":
                        randlol = random.randint(0, len(lols)-1)
                        lolmsg = "PRIVMSG %s :%s: %s"%(to, sender, lols[randlol])
                        send(s, lolmsg)
                    elif line[4] == "fac":
                        try:
                            total = ifac(int(line[5]))
                            facmsg = "PRIVMSG %s :%s: The factorial of %s is: %d"%(to, sender, line[5], total)
                            send(s, facmsg)
                        except ValueError:
                            errormsg = "PRIVMSG %s :%s: ValueError"%(to, sender)
                            send(s, errormsg) 
                    elif line[4] == "commands":
                        cmdmsg = "PRIVMSG %s :%s: fac #, recfac #, sum # #.., div # #.., mult # #.., diff # #.."%(to, sender)
                        send(s, cmdmsg)
                    elif line[4] == "recfac":
                        try:
                            total = fac(int(line[5]))
                            facmsg = "PRIVMSG %s :%s: The recursive factorial of %s is: %d"%(to, sender, line[5], total)
                            send(s, facmsg)
                        except ValueError:
                            errormsg = "PRIVMSG %s :%s: ValueError"%(to, sender)
                            send(s, errormsg) 
                        except RuntimeError:
                            errormsg = "PRIVMSG %s :%s: RuntimeError, 2DEEP4ME"%(to, sender)
                            send(s, errormsg) 
                            
                    elif line[4] == "VERSION":
                        vmsg = "PRIVMSG %s :%s: Version? I don't know. v0.00002?"%(to, sender) 
                        send(s,vmsg)             
                    else:
                        mssg = 'PRIVMSG %s :%s: %s' % (to, sender, ' '.join(line[4:]))
                        send(s, mssg)
        elif len(line)>3 and line[3][1:] in lols:
            if line[2] in chans:
                randlol = random.randint(0, len(lols)-1)
                lolmsg = "PRIVMSG %s :%s"%(line[2], lols[randlol])
                send(s, lolmsg)       
        elif (":stop" in line[3:] or "stop" in line[3:]) and "that" in line[4:]:
            if line[2] in chans:
                nomsg = "PRIVMSG %s :no u"%(line[2])
                send(s, nomsg)               
        elif (":no" in line[3:] or "no" in line[3:]) and "u" in line[4:]:
            if line[2] in chans:
                stopmsg = "PRIVMSG %s :stop that"%(line[2])
                send(s, stopmsg)               
        elif ":chef" in line[3:] or "chef" in line[3:] or "Chef" in line[3:]:
            if line[2] in chans:
                randchef = random.randint(0, len(chefs)-1)
                chefmsg = "PRIVMSG %s :%s"%(line[2], chefs[randchef])
                send(s, chefmsg) 
        elif ":GTFO" in line[3:] and "CHEFLOVER" in line[4:]:
            chefmsg = "PRIVMSG %s :ok.. sorry senpai"%(line[2])
            send(s, chefmsg) 
            send(s, "QUIT") 
            s.close()
        elif line[0] == "PING":
            pong = "PONG %s"%line[1]
            send(s, pong)


make_connection(input)
