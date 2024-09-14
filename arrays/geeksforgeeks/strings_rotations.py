'''You are given two strings of equal lengths, 
s1 and s2. The task is to check if s2 is a 
rotated version of the string s1.

Note: The characters in the strings are in lowercase.'''

def are_rotate(s1, s2):
    a1 = [i for i in s1]
    a2 = [i for i in s2]

    k = 0
    n = len(a2)
    m = n - 1
    if len(s1) != len(s2):
        return False
    
    while k < len(a2):
        temp = a2[-1]
        while m >= 0:
            a2[m] = a2[m-1]
            m -= 1
        a2[0] = temp
        if a1 == a2:
            return True
        k += 1
        m = n - 1 
    return False

# Time Complexity:O(N*M)
# Auxiliary Space: O(M+N)

def areRotations(s1,s2):
        #code here
        a1 = [i for i in s1]
        a2 = [i for i in s2]
        k = 0
    
        if len(s1) != len(s2):
            return False
        
        while k < len(s1):
            a2.append(a2[0])
            a2.pop(0)
            if a1 == a2:
                return True
            k += 1
        return False

s1 = 'amazon'
s2 = 'onamaz'
res = are_rotate(s1, s2)
print(res)

# Time Complexity:O(M)
# Auxiliary Space: O(M+N)
