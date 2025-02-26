

def factorial(n):
    table = [1]
    for x in range(1, n + 1):
        table.append(x * table[x - 1])
    return table[n]


print(factorial(5))


