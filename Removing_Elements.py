def remove_every_other(my_list):
    result = []
    for item in range(len(my_list)):
        if item % 2 == 0:
            result.append(my_list[item])
    return result


print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
