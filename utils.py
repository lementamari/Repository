def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

