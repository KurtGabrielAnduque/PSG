def factorial (n , memo = {}):

    if n == 1:
        return 1
    if not n in memo:
        memo[n] = n * factorial(n - 1)
    return memo[n]



print(factorial(7))



