input = """chat.freenode.net:6667
carrot_chompa
carrot_chompa
Ed Sheeran"""

import socket

def make_connection(input):

    server, nick, user, name = input.splitlines()
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
        #print received
        if lines.startswith("PING"):
            pong = list(lines)        
            pong[1] = "O"
            pong = ("").join(pong)
            print pong
            s.send(pong+"\r\n")


make_connection(input)
