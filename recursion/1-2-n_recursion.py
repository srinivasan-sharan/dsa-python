#print 1->n
def printN(i, n):
    if i>n:
        return
    print(i)
    printN(i+1, n)

i=1
n=5

#print n->1
def revPrintN(i, n):
    if i<1:
        return
    print(i)
    revPrintN(i-1, n)


def print1N(n):
    if n<1:
        return
    print1N(n-1)
    print(n)

print1N(4)



def foo(i, n):
    if i>n:
        return
    print(i)
    foo(i+1, n)

def oof(i, n):
    if i>0:
        return
    print(i)
    oof(i-1, n)