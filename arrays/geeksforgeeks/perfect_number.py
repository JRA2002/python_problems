'''Given a number N, check if a number is perfect or not. 
A number is said to be perfect if sum of all its factors 
excluding the number itself is equal to the number. 
Return 1 if the number is Perfect otherwise return 0.'''

def is_perfect(N):
    suma = 0

    for i in range(1, N):
        if N%i == 0:
            suma += i
    if suma == N:
        return 1
    return 0

#optimal approach
def is_perfect1(N):
    pass

N = 10
res = is_perfect((N))
print((res))
