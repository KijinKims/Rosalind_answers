def Rabbits(n, k):
    if n == 1 or n == 2:
        ans = 1
    else:
        ans = Rabbits(n - 1, k) + k * Rabbits(n - 2, k)
    return ans


print(Rabbits(34, 5))
