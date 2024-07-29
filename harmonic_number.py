
def harmonic_sum(n):
    if n == 1:
        return 1
    return 1/harmonic_sum(n - 1) + round((1/n), 2)