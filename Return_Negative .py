def make_negative(number):
    if number < 0:
        return number
    if number > 0:
        return -number
    if number == 0:
        return 0

print(make_negative(0))