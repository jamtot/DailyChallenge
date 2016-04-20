def fizzbuzz(n):
    for i in xrange(1,n+1):
        out=''
        if not i%3:
            out+="Fizz"
        if not i%5:
            out+="Buzz"
        if out=='':
            out+=str(i)
        print out

if __name__=="__main__":
    while True:
        try:
            fizzbuzz(int(raw_input("> ")))  
        except ValueError:
            print "ValueError"          
