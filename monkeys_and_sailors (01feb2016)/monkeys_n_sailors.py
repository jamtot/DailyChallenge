
def monkeys_n_sailors(n):
    if n == 2: return 11    
    return (n**n) - (n-1)

print monkeys_n_sailors(5)
