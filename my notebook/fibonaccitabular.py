def Fibonnaci(n):
    table = [0,1]
    for x in range(2, n + 1):
        table.append(table[x - 1] + table[x - 2])
    return table[n]

print(Fibonnaci(1))
