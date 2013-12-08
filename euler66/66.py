def prime(n):
    if n < 2: return []

    sieve = [True] * n
    p = 3

    while p ** 2 < n:
        if sieve[p]:
            i = p ** 2
            for j in xrange(i, n, 2 * p):
                sieve[j] = False
        p += 2
    primes = [2]
    for i in xrange(3, len(sieve), 2):
        if sieve[i]: primes.append(i)
    return primes

def pells(d):
    p = 1
    k = 1
    x1 = 1
    y = 0
    sqrtD = d ** (.5)

    while k != 1 or y == 0:
        p = k * (p / k + 1) - p
        p = p - int((p - sqrtD) / k) * k
        x = (p * x1 + d * y) / abs(k)
        y = (p * y + x1) / abs(k)
        k = (p * p - d) / k

        x1 = x
    return x

limit = 1000

print max([(pells(D),D) for D in prime(limit)])

