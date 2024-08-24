'''Given an unsorted array of integers, sort the array into a
 wave array. An array arr[0..n-1] is sorted in wave form if:
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..'''

def wave(arr):
    for i in range(0, len(arr) - 2, 2):
        
            if arr[i] <= arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            if arr[i+1] >= arr[i+2]:
                arr[i+1], arr[i+2] = arr[i+2], arr[i+1]

    return arr

arr = [20, 10, 8, 6, 4, 2]
res = wave(arr)
print(res)

# Time Complexity: O(N)
# Auxiliary Space: O(1)