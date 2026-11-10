import time

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def sum_primes_naive(n):
    total = 0
    for x in range(2, n):
        prime = True
        if x < 2:
            prime = False
        for d in range(2, x):
            if x % d == 0:
                prime = False
                break
        if prime:
            total += x
    return total

def sum_primes_smaller_bound(n):
    total = 0
    for x in range(2, n):
        if is_prime(x):
            total += x
    return total

def sum_primes_sieve(n):
    if n <= 2:
        return 0

    sieve = [True] * n
    sieve[0] = sieve[1] = False

    p = 2
    while p * p < n:
        if sieve[p]:
            for multiple in range(p * p, n, p):
                sieve[multiple] = False
        p += 1

    return sum(i for i in range(2, n) if sieve[i])


if __name__ == "__main__":
    n = int(input("Enter N: "))

    start = time.time()
    print("Naive:", sum_primes_naive(n))
    print("Naive time:", time.time() - start)

    start = time.time()
    print("Smaller bound:", sum_primes_smaller_bound(n))
    print("Smaller bound time:", time.time() - start)

    start = time.time()
    print("Sieve:", sum_primes_sieve(n))
    print("Sieve time:", time.time() - start)
