def get_average(marks):
    sum = 0
    for mark in marks:
        sum += mark
    return int(sum / len(marks))


print(get_average([1, 5, 87, 45, 8, 8]))
