def printName(n):
    while n>1:
        n-=1
        printName(n)
    print("Sharan")

printName(5)