'''Print the elements of an array in the decreasing frequency 
if 2 numbers have the same frequency then print the one which came first'''

from merge_sort import merge_sort
from collections import defaultdict
def sorting(arr: list):
    arr = merge_sort(arr)
    set1 = set(arr)
    dict1 = {}
    newarr = [0] * len(arr)
    for i in set1:
        count = arr.count(i)
        dict1[i] = count
        
    dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))

        
        
    return dict1

# Python3 program for above approach



# Sort by Frequency


def sortByFreq(arr, n):
    # arr -> Array to be sorted
    # n   -> Length of Array

    # d is a hashmap(referred as dictionary in python)
    d = defaultdict(lambda: 0)
    for i in range(n):
        d[arr[i]] += 1

    # Sorting the array 'arr' where key
    # is the function based on which
    # the array is sorted
    # While sorting we want to give
    # first priority to Frequency
    # Then to value of item
    arr.sort(key=lambda x: (-d[x], x), reverse = True) 
    #require Updation:- reverse = True, to sort an array in descending order (Jayesh Verma)
    return (arr)


# Driver code
if __name__ == "__main__":
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    n = len(arr)

    # Function call
    solution = sortByFreq(arr, n)
    print(*solution)


arr = [2, 5, 2, 8, 5, 6, 8, 8]
res = sorting(arr)
print(res)