input = """chat.freenode.net:6667
carrot_chompa
carrot_chompa
Ed Sheeran
#reddit-dailyprogrammer,#rdp,#botters-test
Hello World!"""

import socket

def make_connection(input):

    server, nick, user, name, channels, message = input.splitlines()
    chans = channels.split(",")
    server, port = server.split(":")
    server_name = "*"
    user_mode = 0
    s = socket.socket()
    s.connect((server, int(port)))
    print "connected"

    nickmsg = "NICK %s" % nick
    usermsg = "USER %s %d %s :%s\r\n" % (user, user_mode, server_name, name)
    print nickmsg
    print usermsg    
    s.send(nickmsg+"\r\n")
    s.send(usermsg+"\r\n")
    print "initial details sent"
    received = ""
    while True:
        if "\r\n" not in received:
            received += s.recv(512)
        lines, received = received.split("\r\n", 1)
        print lines

        if "376" in lines:
            joinmsg="JOIN %s"%channels
            s.send(joinmsg+"\r\n")
            print joinmsg

        for chan in chans:
            if "JOIN" in lines and chan in lines:
                hellomsg="PRIVMSG %s :Hello World!"%chan
                s.send(hellomsg+"\r\n")
                print hellomsg

        if nick in lines:
            command = lines.split(nick)
            command = command[1]
            
        if "PRIVMSG" in lines and nick in lines:
            content = lines.split()   
            chann=content[2]
            sender=content[3]
            if nick in chann:
                chann=sender
            stuff=(" ").join(content[4:])
            print content
            print chann
            print sender
            privmsg="PRIVMSG %s %s can't yet handle \"%s\""%(
                chann,sender,stuff)
            s.send(privmsg+"\r\n")
            print privmsg
             

        if lines.startswith("PING"):
            pong = list(lines)        
            pong[1] = "O"
            pong = ("").join(pong)
            print pong
            s.send(pong+"\r\n")


make_connection(input)
