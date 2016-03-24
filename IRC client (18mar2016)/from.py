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

        elif line[1]=="JOIN":
            hellomsg="PRIVMSG %s :%s"%(line[2],message)#the channel
            send(s, hellomsg)

        elif line[0] == "PING":
            pong = "PONG %s"%line[1]
            send(s, pong)
        
        #:GeekDude!G33kDude@192-168-1-42.isp.com PRIVMSG #rdp :GeekBot: mult 5 4 3 2 1 
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
        elif ":lol" in line[3:] or "lol" in line[3:]:
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
                chefmsg = "PRIVMSG %s :Chef? 86%% on Rotten Tomatoes, baby!"%(line[2])
                send(s, chefmsg) 



make_connection(input)
