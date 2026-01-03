import math

def divisors(n):
    divs = []
    for i in range(1, math.ceil(n/2)+1):
        if n%i==0:
            divs.append(i)
    divs.append(n)
    return divs

print(divisors(36))