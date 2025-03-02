''''
Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.

Subsequence
A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.

Example subsequence
Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".
'''


def lcs(x, y):
    x_row = len(x)
    y_column = len(y)
    table = [[0 for x in range(y_column+ 1)] for y in range(x_row + 1)]


    for i in range(1,x_row + 1):
        for j in range(1, y_column + 1):
            if x[i - 1] == y[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]

            else:
                table[i][j] = max(table[i -1][j],table[i][j - 1])


    new_letter = []
    back_x = x_row
    back_y = y_column

    while back_y > 0 and back_x > 0:

        if x[back_x - 1] == y[back_y - 1]:
            new_letter.append(x[back_x - 1])
            back_x -= 1
            back_y -= 1

        elif table[back_x - 1][back_y] > table[back_x][back_y - 1]:
            back_x -= 1

        else:
            back_y -= 1

    rev = ''.join(reversed(new_letter))
    return rev












print(lcs("anothertest", "notatest"))