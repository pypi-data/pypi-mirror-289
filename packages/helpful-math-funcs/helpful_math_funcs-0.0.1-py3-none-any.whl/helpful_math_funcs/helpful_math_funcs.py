# helpful_math_funcs.py

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def prime_factors(n: int) -> list:
    """Return the prime factors of the given number."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def fibonacci(n: int) -> list:
    """Return a list of the first n Fibonacci numbers."""
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]