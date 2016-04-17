def looknsay(n, seed):
    result=''
    num = str(seed)
    cur,count=num[0],0
    for digit in num:
        if digit==cur:
            count+=1
        else:
            result+=str(count)+cur
            cur=digit
            count=1
    else:
        result+=str(count)+cur

    print result
    if n==1:
        return result
    else: 
        return looknsay(n-1, result)

if __name__=="__main__":
    looknsay(10,23)
    looknsay(10,22)# 22 describes itself as 22, so is the same each time
