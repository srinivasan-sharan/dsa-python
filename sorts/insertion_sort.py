import numpy, time

def insertion_sort(arr: list[int]) -> list[int]:
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i>0 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key

    return arr

arr = numpy.random.randint(0, 10000, 5)
arr_test = numpy.random.randint(0, 10000, 10000)

print("Array before sorting:", arr)
sorted_arr = insertion_sort(arr)
print("Array post sorting:", sorted_arr)


start = time.time()
insertion_sort(arr_test)
end = time.time()
print(round(end-start, 2))

