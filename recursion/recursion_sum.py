#honestly, happy that this was done by self
def sum_rec(n):
    if n < 1:
        return 0
    return n + sum_rec(n-1)

#print(sum_rec(100))

#this is most definitely the recursion i know
def fact_rec(n):
    if n < 1:
        return 1
    return n * sum_rec(n-1)

#print(fact_rec(4))

def print_n21(n):
    if n == 1:
        return 1
    print(n)
    return print_n21(n-1)

# print(print_n21(4))

def print_12n(n):
    if n < 1:
        return 1
    print_12n(n-1)
    print(n)
    
print_12n(4)

#ok this code is much better, atleast compared to the others