# Example 1:
# Input:N = 4554
# Output:Palindrome Number
# Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number
                                        
# Example 2:
# Input:N = 7789          
# Output: Not Palindrome
# Explanation: The reverse of number 7789 is 9877 and therefore it is not palindrome

def palindrome(n):
    if reverse_num(n) == n:
        return print("palindrome")
    else:
        return print("not palindrome")

def reverse_num(n):
    rev = 0
    while n>0:
        last = n%10
        # print(last)
        rev = rev*10 + last
        n = n//10
    return rev

palindrome(1234)
palindrome(1234321)
palindrome(65456)