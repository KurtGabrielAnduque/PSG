def square_digits_sequence(n):
    number = n
    elements = []
    lst = []

    while number not in elements:
        elements.append(number)
        lst = [int(digit) ** 2 for digit in str(number)]
        print(lst)
        print(elements)
        number = sum(lst)

    elements.append(number)
    return len(elements)

print(square_digits_sequence(16))