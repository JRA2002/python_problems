'''Given an array having positive and negative numbers, our task 
is to arrange them in an alternate fashion such that every positive
number is followed by a negative number and vice-versa maintaining 
the order of appearance. The number of positive and negative numbers 
need not to be equal. If there are more positive numbers then they have 
to appear at the end of the array , same condition for negative numbers also .'''

def rearrange(arr: list):
    neg = []
    pos = []
    final = []
    for i in range(len(arr)):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    i = 0
    if len(neg) < len(pos):
        while i < len(neg):
            final.append(neg[i])
            final.append(pos[i])
            i += 1
        while  i < len(pos):
            final.append(arr[i])
            i += 1        

    return final           

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
res = rearrange(arr)
print(res)
