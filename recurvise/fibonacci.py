def fibonacci(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fibonacci(num - 2)  + fibonacci(num - 1)

num = fibonacci(7)
print(num)