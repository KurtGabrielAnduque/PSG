

def Fibonnaci(n, memo = {}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if not n in memo:
        memo[n] = Fibonnaci(n - 1) + Fibonnaci(n - 2)
    return memo[n]


print(Fibonnaci(7))