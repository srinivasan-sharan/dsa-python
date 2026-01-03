import math
def prime(n):
    for i in range(2, math.ceil(n/2)+1):
        if n%i==0:
            return False
    return True
    
print(prime(4))