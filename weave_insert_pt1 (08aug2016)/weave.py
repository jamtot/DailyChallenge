def insWeave(array1, array2):
    i=0
    lenarray1=len(array1)
    lenarray2=len(array2)
    weaved=[]
    while i < lenarray2:
        weaved.append(array2[i])
        if i < lenarray2-1:
            weaved.append(array1[i%lenarray1])
        i+=1
    return weaved

def insBracket(string, pairs):
    pairlen=len(pairs)/2
    strlen=len(string)
    maxlen=max(pairlen,strlen)
    bracketed=[]
    i,j,k=0,0,0
    while i < maxlen:
        bracketed.append(pairs[k]+string[j]+pairs[k+1])
        i+=1
        j=(j+1)%strlen
        k=(k+2)%pairlen
    return bracketed

if __name__ == "__main__":
    print insWeave([11], [0,1,2,3])
    print insWeave([11,12], [0, 1, 2, 3])  
    print insWeave([11,12,13], [0, 1])
    print insBracket ('abc'  , '()' )
