def print1(n):
    for r in range(n):
        for c in range(n):
            print("* ", end="")
        print()

def print2(n):
    for r in range(n):
        for c in range(r):
            print("* ", end="")
        print()

def print3(n):
    for r in range(n):
        for c in range(r+1):
            print(c+1, end="")
        print()

def print4(n):
    for r in range(n):
        for c in range(r+1):
            print(r+1, end="")
        print()
 
def print5(n):
    for i in range(n):
        for j in range(n-i):
            print("* ", end="")
        print()
 
def print6(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end="")
        print()
 


def driver_func():
    n=5
    print6(n)

driver_func()