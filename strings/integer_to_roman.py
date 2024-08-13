'''Given a number, find its corresponding Roman numeral.'''

def romans(res):
    if res == 1:
        return 'I'
    elif res == 5:
        return 'V'
    elif res == 10:
        return 'X'
    elif res == 50:
        return 'L'
    elif res == 1000:
        return 'M'
    return 'Q'
def convert_roman(num):
  
    lenght = len(num) - 1
    i = 0
    string = ''
    while i < len(num):
        res = int(num[i]) * 10 ** (lenght)
        st = romans(res)
        string += st
        
        i += 1
        lenght -= 1
        print(res)
    print(string)

    

convert_roman('1092')

