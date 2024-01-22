def sum_mix(arr):
    new_arr = []
    for num in arr:
        if type(num) == str:
            num = int(num)
        new_arr.append(num)
    return sum(new_arr)

print(sum_mix([9, 3, '7', '3']))
