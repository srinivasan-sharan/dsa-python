# def gcd(n,m):
#     gcd = 1

#     for i in range(1,min(n,m)+1):
#         if ((n%i)==0) and ((m%i)==0):
#             gcd=i
#     return gcd

def gcd(n,m):
    while m>0 and n>0:
        if m>n:
            m = m%n
        else:
            n = n%m
    if m == 0:
        return n
    return m

print(gcd(9,12))