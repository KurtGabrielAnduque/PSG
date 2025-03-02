def count_change(money, coins):
    rows = len(coins)

    table = [[0 for y in range(money + 1)] for x in range(rows + 1)]

    #1 way in exchangin 0

    for row in range(rows + 1):
        table[row][0] = 1

    for row in range(1, rows + 1):
        for column in range(1, money + 1):

            table[row][column] = table[row - 1][column]


            if coins[row - 1] <= column:
                table[row][column] += table[row][column - coins[row - 1]]

    return table[rows][money]




money = 4
coins = [1,2]


print(count_change(money, coins))

