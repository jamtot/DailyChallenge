# solution presented by user fibonacci__ (https://www.reddit.com/user/fibonacci__)

def coconuts(n):
    if n == 2: return 11
    return n**n - n + 1 if n % 2 else (n - 1) * (n**n - 1)


print coconuts(2)
print coconuts(3)
print coconuts(4)
print coconuts(5)
print coconuts(6)
print coconuts(7)
