primes = []
lista = [i for i in range(23 + 1)]
print(lista)
lista[0] = lista[1] = 0
count = 0
for i in range(23 + 1):
    if lista[i]:
        primes.append(i)
        count += 1
        h = 2
        while i * h < 23:
            lista[i*h] = 0
            h += 1


print(primes)
print(count)
