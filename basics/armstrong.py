def armstrong(n):
    sum=0
    n_cop=n
    power=countDigits(n)
    while n>0:
        sum += pow(n%10, power)
        n = n//10
    if sum == n_cop:
        return ("Armstrong number ahhh")
    else:
        return ("Not armstrong")

    

def countDigits(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count


print(armstrong(111))