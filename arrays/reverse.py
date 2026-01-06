# we will be reversing an array

def reverse_arr(arr):
    n = len(arr)
    rev_arr = [0] * n
    for i in range(n):
        rev_arr[i] = arr[n-i-1]
    return rev_arr

arr = [2,4,6,8,10]

print(reverse_arr(arr))

# nice approach, can we do better?

print(arr[::-1])

# yes we can :p


