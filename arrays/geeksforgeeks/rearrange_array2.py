'''Given an array of elements arr[] with indices ranging from 0 to arr.size() - 1, 
your task is to write a program that rearranges the elements of the array such 
that arr[i] = i. If an element i is not present in the array, -1 should be 
placed at the corresponding index.'''

def rearrange_array(arr: list):
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        if arr[i] != i:
            arr[i] = -1
    return arr

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
res = rearrange_array(arr)
print(res)