def printNum(i,n):
    if (i<1):
        return
    printNum(i-1, n)
    print(i)

#printNum(5,5)

def printNum2(n):
    if (n<1):
        return
    print(n)
    printNum2(n-1)
    

printNum2(10)
