'''Given a number N. Find if it can be expressed as sum of two prime numbers.'''

def primes_sum(N: int):
    def get_primes(N: int):
        primes = []
        lista = [i for i in range(N + 1)]
        print(lista)
        lista[0] = 0
        lista[1] = 0
        count = 0
        for i in range(N + 1):
            if lista[i]:
                primes.append(i)
                count += 1
                h = 2
                while i * h <= N:
                    lista[i*h] = 0
                    h += 1
        return primes
    p = get_primes(N)
    i = 0
    j = len(p) - 1
    while i <= j:
        if p[i] + p[j] > N:
            j -= 1
        elif p[i] + p[j] == N: 
            return True
        else:
            i += 1
    return False


N = 23

res = primes_sum(N)
print(res)