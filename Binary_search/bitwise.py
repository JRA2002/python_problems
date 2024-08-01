def set_bit(x, position):
    mask = 1 << position
    return x | mask

def clear_bit(x, position):
    mask = 1 << position
    return x & ~mask

def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask

def find_minimum(x, y):
    res = y ^ ((x ^ y) & -(x < y))
    return res

def find_maximun(x, y):
    res = x ^ ((x ^ y) & -(x < y))
    return res

def power_of_two(v):
    res = (v & (v - 1)) == 0
    return res

bin = bin(30)
print(bin)
integer = int('0b1111', base=0)
print(integer)