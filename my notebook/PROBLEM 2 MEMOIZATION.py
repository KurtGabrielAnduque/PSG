'''
Problem: Named Coin Change (Minimum Coins)
You are given an array of coin denominations,
their corresponding names, and a total amount.
Your task is to determine the minimum number of coins needed to make up that amount,
long with the names of the selected coins. If it's not possible, return -1.

'''


def memo_knapsack(a,c,v,nm,n,memo = {}):


    if a == 0 or n == 0:
        return 0, []


    if c[n - 1] > a:
        return memo_knapsack(a,c,v,nm,n - 1,memo)


    if (a, n) in memo:
        return memo[(a,n)]


    value_max,item_max = memo_knapsack(a - c[n - 1],c,v,nm,n - 1, memo)
    value_max += v[n - 1]
    item_max = item_max + [nm[n - 1]]

    value_min, item_min = memo_knapsack(a,c,v,nm, n - 1, memo)


    if value_max > value_min:
        memo[(a,n)] = (value_max, item_max)
    else:
        memo[(a,n)] = (value_min,item_min)

    return memo[(a,n)]

value = [1, 2 ,5, 10, 20]
coins = [1, 2, 5, 10, 20]
names = ["penny", "nickel", "dime", "quarter", "half-dollar"]
amount = 27
n = len(coins)

print(memo_knapsack(amount,coins,value,names,n))



