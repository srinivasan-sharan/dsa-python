# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.
                        
# Example 2:
# Input:N = 7789              
# Output: 4
# Explanation: The number 7789 has 4 digits.  

n = 12345678

def countDigits(n):
    count_digits = 0
    while n>0:
        n = n//10
        count_digits+=1
    return count_digits

print(countDigits(n))