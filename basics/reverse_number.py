# Input: N = 12345
# Output:54321
# Explanation: The reverse of 12345 is 54321.

# Input: N = 7789                
# Output: 9877
# Explanation: The reverse of number 7789 is 9877.

def reverse_num(n):
    rev = 0
    while n>0:
        last = n%10
        # print(last)
        rev = rev*10 + last
        n = n//10
    return print(rev)

reverse_num(n=12345)
reverse_num(7789)