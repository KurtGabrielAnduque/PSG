
'''

You are given a knapsack with a maximum weight capacity of 10 kg. You also have 4 items, each with a specific weight and value.

'''


def knapsack_recursion(c,w,v,n,names,memo = {}):

    if n == 0 or c == 0:
        return 0,[]

    if w[n - 1] > c:
        return knapsack_recursion(c,w,v,n - 1,names,memo)


    if (c,n) in memo:
        return memo[(c,n)]


    value_max, item_max = knapsack_recursion(c - w[n - 1],w,v, n - 1,names,memo)
    value_max += v[n - 1]
    item_max =  item_max  + [names[n - 1]]

    value_min, item_min = knapsack_recursion(c,w,v,n - 1,names, memo)

    if value_max > value_min:
        memo[(c,n)] = (value_max,item_max)

    else:
        memo[(c,n)] = (value_min,item_min)


    return memo[(c,n)]



names = ["can","soda","rice","keyboard"]
weights = [2,3,4,5]
Values = [40,50,100,60]
constraint = 10
n = len(weights)

print(knapsack_recursion(constraint,weights,Values,n,names))
