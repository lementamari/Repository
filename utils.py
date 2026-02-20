def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def fibonacci(n):
if n <= 0:
return 0
if n == 1:
return 1
a, b = 0, 1
for _ in range(2, n + 1):
a, b = b, a + b
return b


def gcd(a, b):
while b:
a, b = b, a % b
return a

