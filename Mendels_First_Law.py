import math


def ncr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def Calculate(k, m, n):
    numerator = (1 * ncr(k, 2)
                 + 3 / 4 * ncr(m, 2)
                 + 0 * ncr(n, 2)
                 + 1 * ncr(k, 1) * ncr(m, 1)
                 + 1 / 2 * ncr(m, 1)
                 + 1 * ncr(k, 1) * ncr(n, 1))
    denominator = ncr(k + m + n, 2)
    print(numerator)
    print(denominator)
    print(numerator / denominator)


Calculate(15, 22, 24)
