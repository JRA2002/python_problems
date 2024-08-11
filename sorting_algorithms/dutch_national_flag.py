'''Given an array A[] consisting of only 0s, 1s, and 2s. The task is to sort 
the array, i.e., put all 0s first, then all 1s and all 2s in last'''

def national_flag(arr: list):
    arr.sort()
    return arr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
res = national_flag(arr)
print(res)