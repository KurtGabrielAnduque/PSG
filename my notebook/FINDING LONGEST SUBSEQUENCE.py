def lcs(string1, string2):
    rows = len(string1)
    columns = len(string2)

    table = [[0 for y in range(columns + 1)] for x in range(rows + 1)]


    for row in range(1,rows + 1):
        for column in range(1,columns  + 1):

            if string1[row - 1] == string2[column -1]:
                table[row][column] = 1 + table[row -1][column - 1]

            else:
                table[row][column] = max(table[row - 1][column],table[row][column - 1])


    sublist = []
    rowx = rows
    columny = columns

    while rowx > 0 and columny > 0:
        if string1[rowx - 1] == string2[columny - 1]:
            sublist.append(string1[rowx - 1])
            rowx -= 1
            columny -= 1

        elif table[rowx - 1][columny] > table[rowx][columny -1]:
            rowx -= 1

        else:
            columny -= 1

    return ''.join(reversed(sublist)),table[rows][columns]


string1 = "abcdefghijklmnopq"
string2 = "apcdefghijklmnobq"
print(lcs(string1, string2))