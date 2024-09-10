'''Given an unsorted array arr[] of size n. Rotate the array to 
the left (counter-clockwise direction) by d steps, where d is a 
positive integer. '''

def rotate_array(A : list, D, N):
    for _ in range(D):
        A.append(A[0])
        A.pop(0)
    return A

A = [1,2,3,4,5]
D = 2
N = len(A)
res = rotate_array(A, D , N)
print(res)