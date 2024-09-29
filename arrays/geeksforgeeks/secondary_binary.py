'''Given two numbers A and B count all the number between the given range whose second least significant digit in the binary representation of the number is 1.'''

def find_digit(A, B):
    
    count = 0
    cos = (A//4) - 2
    if cos<0:
        cos=0
    num1 = 2+4*cos
    while num1 <= B:
        num1 = num1 + 4*cos
        num2 = num1 + 1
        print(num1,num2)
        if num1 >= A and num1 <= B :
            count += 1
        if num2 >= A and num2 <= B:
            count += 1
        cos += 1
    return count
A = 7
B = 11

res = find_digit(A, B)
print(res)