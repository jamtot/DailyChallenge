def place(n):
    if n%10 == 1 and str(n)[-2:]!='11':
        print "%dst"%n
    elif n%10 == 2 and str(n)[-2:]!='12':
        print "%dnd"%n
    elif n%10 == 3 and str(n)[-2:]!='13':
        print "%drd"%n
    else:
        print "%dth"%n

if __name__ == "__main__":
    for i in xrange(201):
        place(i)
