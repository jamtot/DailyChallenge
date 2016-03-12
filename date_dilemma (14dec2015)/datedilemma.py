input1 = """2/13/15
1-31-10
5 10 2015
2012 3 17
2001-01-01
2008/01/07"""

def getLines(input):
    return input.splitlines()

def reformat(date):
    # take date string and split
    datesp = date.replace('/',' ').replace('-',' ').strip().split(' ')
    # if date has more than 3, there are seperators
    # if 1st is 4 -> Y M D
    if len(datesp[0])==4: # Y M D
        year = datesp[0]
        month = datesp[1]
        day = datesp[2] 
    # if 1st isn't 4 - > M D Y           
    else: # M D Y
        year = datesp[2]
        month = datesp[0]
        day = datesp[1]
    if len(year) < 4: year = "20%s" % year
    if len(month) < 2: month = "0%s" % month
    if len(day) < 2: day = "0%s" % day
    
    # format back to Y M D
    return ('-').join([year,month,day])


def printDates(dates):
    for date in dates:
        print reformat(date)

dates = getLines(input1)
printDates(dates)

