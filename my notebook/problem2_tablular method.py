
'''
Problem: Named Coin Change (Minimum Coins)
You are given an array of coin denominations,
their corresponding names, and a total amount.
Your task is to determine the minimum number of coins needed to make up that amount,
long with the names of the selected coins. If it's not possible, return -1.

'''


def DP_REC(a,c,v,nm,n):

    table = [[0 for x in range(a + 1)] for y in range(n + 1)]


    for items in range(n + 1):
        for coins in range(a + 1):
            if items == 0 or coins == 0:
                table[items][coins] = 0

            elif c[items - 1] <= coins:
                table[items][coins] = max(
                    value[items - 1] + table[items - 1][coins- c[items - 1]],
                    table[items - 1][coins]
                                          )
            else:
                table[items][coins] = table[items - 1][coins]


    selecte_coins = []
    remaining_amount = a

    for coin in range(n, 0, -1):
        if table[coin][remaining_amount] != table[coin - 1][remaining_amount]:
            selecte_coins.append(nm[coin - 1])
            remaining_amount -= c[coin - 1]

    return table[n][a],selecte_coins






value = [1, 2, 5, 10, 20]
coins = [1, 2, 5, 10, 20]
names = ["penny", "nickel", "dime", "quarter", "half-dollar"]
amount = 27
n = len(coins)

print(DP_REC(amount,coins,value,names,n))