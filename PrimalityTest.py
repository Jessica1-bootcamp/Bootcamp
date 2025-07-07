from random import randrange
import math

def is_prime_trial_division(n):
    """Simple primality test for small numbers using trial division"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_probably_prime_miller_rabin(n, k=5):
    """Miller-Rabin probabilistic primality test"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def is_prime(n):
    """Uses trial division for small n, Miller-Rabin for large n"""
    if n < 1_000_000:
        return is_prime_trial_division(n)
    else:
        return is_probably_prime_miller_rabin(n)