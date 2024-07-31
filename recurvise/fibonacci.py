def fibonacci(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fibonacci(num - 2)  + fibonacci(num - 1)

for i in range(7):
    print(fibonacci(i))
print(bin(10))
print(int('1010', base=0))