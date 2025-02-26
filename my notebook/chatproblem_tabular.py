
'''

You are given a knapsack with a maximum weight capacity of 10 kg. You also have 4 items, each with a specific weight and value.

'''


def DP_knapsack(c,w,v,n):

    table = [[0 for x in range(c + 1)] for y in range(n + 1)]

    for x in table:
        print(x)


    for x in range(n + 1):
        for y in range(c + 1):
            if x == 0 or y == 0:
                table[x][y] = 0

            elif w[x - 1] <= y:
                table[x][y] = max(v[x - 1] + table[x - 1][y  - w[x -1]], table[x - 1][y])
            else:
                table[x][y] = table[x - 1][y]

    return table[n][c]




weights = [2, 3, 4, 5]
Values = [40, 50, 100, 60]
constraint = 10
n = len(weights)

print(DP_knapsack(constraint,weights,Values,n))