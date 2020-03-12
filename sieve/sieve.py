def primes(limit):
    cojunto = set(range(2, limit + 1))
    primos = {m for n in cojunto for m in range(2 * n, limit + 1, n)}
    return sorted(cojunto - primos)
