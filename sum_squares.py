def sum_squares(num):
    result = 0
    for n in range(num,0,-1):
        print(f"soy {n}")
        result = result + (n-1)**2
    return result

print(sum_squares(5))