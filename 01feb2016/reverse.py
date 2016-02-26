def reverse(coconuts, sailors):
    curnuts = coconuts
    print "We start with %d coconuts, and %d sailors. And a monkey." % (coconuts, sailors)
    for i in range(sailors):
        sailor_takes = curnuts / 5
        print "The sailor takes %d for himself." % sailor_takes
        remainder = curnuts % 5
        print "The amount left over after the split is %d." % remainder 
        #remainder-=1 
        print "The monkey gets one."
        curnuts = (curnuts - sailor_takes) - remainder # for the monkey
        print "The amount left over for the other sailors is %d." % curnuts
    if curnuts % sailors == 0:
        curnuts /= sailors
        print "The end amount splits evenly. %d each." % curnuts
    else:
        print "It doesn't split %d ways: %d / %d = %d with remainder %d" % (sailors, curnuts, sailors, curnuts / sailors, curnuts % sailors)

reverse(11, 2)
reverse(25, 3)
reverse(253, 4)
reverse(3121, 5)
reverse(46651, 6)
reverse(823537, 7)


