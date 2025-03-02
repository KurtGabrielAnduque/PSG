def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    list = []
    current_list = []
    for num in arr:
        if num > current_sum + num:
            current_list = [num]
            current_sum = num


        else:
            current_sum = current_sum + num
            current_list.append(num)


        if max_sum < current_sum:
            max_sum = current_sum
            list = current_list[:]

    return max_sum,list


arr = [-1,-2,3,4,8,-6,7,-9,11,12,13]
print(max_sequence(arr))


