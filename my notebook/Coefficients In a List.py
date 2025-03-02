def calc_poly(pol_list, x): #If polynomial degree == 3

    n = len(pol_list) - 1
    lst = []
    text = []
    for y in range(len(pol_list)):

        if pol_list[y] != 0:
            if pol_list[y] == 1 and n > 0:
                text.append(f'x^{n}')

            elif n > 1:
                text.append(f'{pol_list[y]}*x^{n}')

            elif n == 1 or n == -1:
                text.append(f'{pol_list[y]}*x')

            else:
                text.append(f'{pol_list[y]}')

        lst.append(pol_list[y] * (x**n))

        n -= 1

    poly = ' + '.join(text).replace('+ -','- ')

    return f'For {poly} with x = {x} the value is {sum(lst)}'

print(calc_poly([6, 3, 5, -4], 4))