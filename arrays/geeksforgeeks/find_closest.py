'''Given a sorted array arr[] of positive integers.
 The task is to find the closest value in the array 
 to the given number k. The array may contain duplicate values.

Note: If the difference with k is the same for two values 
in the array return the greater value.'''

def find_closest(n, k, arr):
    for i in range(n):
        arr[i] = abs(k - arr[i])
    print(arr)


k = 4
arr = [1, 3, 6, 7]
n =  len(arr)

res = find_closest(n, k, arr)
print(res)