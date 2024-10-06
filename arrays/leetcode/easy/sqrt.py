'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.'''

def mysqrt(x):
        i = 1
        while i * i <= x:
            i += 1
        return i - 1
# optimal approach

def mysqrt2(x):
    i = 0
    j = x
    while i <= j:
        midd = (i + j)//2
        print(midd)
        if midd * midd == x:
             return midd
        elif midd * midd > x:
             j = midd - 1
        else:
             i = midd + 1
    return midd
x = 19
res = mysqrt2(x)
print(res)