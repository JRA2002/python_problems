'''Given a string in roman form, the task is to convert this given roman string into an integer'''

def convert(s):
    romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
    
    end = len(s)
    start = end - 2
    num = 0

    while end > 0:
        a = s[start:end]
        if len(a) == 1:
            num = num + romans[a[0]]
        
        elif a[0] < a[1]:
            num = num + (romans[a[1]] - romans[a[0]])
        elif a[0] >= a[1]:
            num = num + (romans[a[1]] + romans[a[0]])

        end = start
        start = end - 2
        if start < 0:
            start = 0
    
    return num
    
s = 'XCVIII'
res = convert(s)
print(res)
