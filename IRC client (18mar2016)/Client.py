input = """chat.freenode.net:6667
eljefe
eljefe
Jon Favreau"""

import socket
import threading
import random
import datetime
import readline
import sys
from collections import defaultdict

lols = ["lol", "kek", "lel", "zozzle", "bazinga", "topkek",
            "zim zam flim flam", "olo", "lols", "wew lad"]

# using an iterative factorial so there's no deptherror
def ifac(n):
    if n < 0:
        n=n*-1
    for i in xrange(n-1, 1, -1):
        n*=i
    return n

# this will only go 998 deep, usually 999 deep
def fac(n):
    if n < 0:
        n=n*-1
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

class Client(object):
    def __init__(self, server, nick, user, name, bg_visible=False):
        self.server, self.port = server.split(":")
        self.nick = nick
        self.user = user
        self.name = name
        self.server_name = "*"
        self.user_mode = 0
        self.socky = socket.socket()
        self.received = "" # buffer
        self.current_channel = ''
        self.channels = []
        self.bg_visible = bg_visible
        self.nicknames = defaultdict(list)

    def connect(self):
        
        self.socky.connect((self.server, int(self.port)))
        print "Connected."

    def setup(self):
        nickmsg = "NICK %s" % self.nick
        usermsg = "USER %s %d %s :%s" % (self.user, self.user_mode, self.server_name, self.name)
        self.send(nickmsg)
        self.send(usermsg)
        print "Initial details sent."

    def send(self,msg):
        if self.bg_visible:
            print "->", msg
        self.socky.send(msg+"\r\n")

    def recv(self):
        print "STARTING RECV THREAD"
        while True:
            if "\r\n" not in self.received:
                self.received += self.socky.recv(512)
            line, self.received = self.received.split("\r\n", 1)

            line = line.split()

            if line[1] == "PRIVMSG":
                now = datetime.datetime.now()
                nowtime = "[%r:%r:%r]" % (now.hour, now.minute, now.second)
                sender = line[0].split("!")[0][1:]
                msg = " ".join(line[3:])[1:]# loses the ':' at the start
                # saves the current input, when incoming text interupts
                sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
                print "%s %s <%s> %s"% (nowtime,line[2],sender,msg)
                sys.stdout.write(readline.get_line_buffer())
                sys.stdout.flush()
                
                
            elif line[0] == "PING":
                if self.bg_visible:
                    print " ".join(line)
                pong = "PONG %s"%line[1]
                self.send(pong)
            else: 
                sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
                print " ".join(line)
                sys.stdout.write(readline.get_line_buffer())
                sys.stdout.flush()                

            if line[1] == "376":
                if self.bg_visible:
                    print "MOTD done, you can join now."

            elif line[1] == "353":
                print line[4], line[5:]
                self.nicknames[line[4]] = [line[5:]]

            
            

    def out(self):
        print "STARTING SEND TRHEAD"
        while True:
            t_input = raw_input()
            if not t_input:
                continue
            if "/quit" in t_input:
                # kind of errors on the closing (due to second thread)
                msg = "PRIVMSG %s :%s: %s OUT!"%(self.current_channel,t_input[1],self.nick)
                self.send(msg)
                self.send("QUIT")
                self.socky.close()  
                exit(1)
            elif "/join" in t_input:
                t_input = t_input.split("/join")
                self.current_channel = t_input[1]
                print "Joining %s"% self.current_channel
                joinmsg="JOIN %s"%self.current_channel
                if self.current_channel not in self.channels:
                    self.channels.append(self.current_channel)
                self.send(joinmsg)
            elif "/msg" in t_input:
                if self.current_channel != "":
                    t_input = t_input.split("/msg")
                    msg = "PRIVMSG %s :%s: %s"%(self.current_channel,t_input[1], " ".join(t_input[2:]))
                    self.send(msg) 
            elif "/lch" in t_input:
                if self.current_channel != "":
                    print "Channels you are in:",
                    for chan in self.channels:
                        print chan,
            elif "/commands" in t_input:
                if self.current_channel != "":
                    print "Channels you are in:",
            elif "/ch" in t_input:
                t_input = t_input.split("/ch")
                if t_input[1] in self.channels:
                    print "Switching to %s" % t_input[1]
                    self.current_channel = t_input[1]
                else:
                    print "Not in %s, joining." % t_input[1]
                    self.current_channel=t_input[1]
                    joinmsg="JOIN %s"%self.current_channel
                    self.channels.append(t_input[1])
                    self.send(joinmsg)
            elif "/users" in t_input:
                print self.nicknames[self.current_channel]
                for name in self.nicknames[self.current_channel]:
                    print name,
            elif "/nick" in t_input:
                # no handling of taken nicknames
                t_input = t_input.split("/nick")
                if len(t_input[1])>0:
                    print "changing nick to %s" % t_input[1]
                    self.nick = t_input[1]
                    self.send("NICK %s"% t_input[1])
            else:
                if self.current_channel != "":
                    # used to remove the input and write over where it was
                    print "\033[A                             \033[A" 
                    now = datetime.datetime.now()
                    nowtime = "[%r:%r:%r]" % (now.hour, now.minute, now.second)
                    print "%s %s <%s> %s"% (nowtime,self.current_channel,self.nick,t_input)
                    msg = "PRIVMSG %s :%s"%(self.current_channel,t_input)
                    self.send(msg) 

if __name__=="__main__":
    server, nick, user, name = input.splitlines()
    myClient = Client(server, nick, user, name)
    myClient.connect()
    myClient.setup()
    recv_thread = threading.Thread(target = myClient.recv)
    out_thread = threading.Thread(target = myClient.out)
    recv_thread.start()
    out_thread.start()
