primes = []
lista = [i for i in range(8)]
print(lista)
lista[0] = lista[1] = 0
for i in range(8):
    if lista[i]:
        primes.append(i)
        h = 2
        while i * h < 8:
            lista[i*h] = 0
            h += 1


print(primes)
