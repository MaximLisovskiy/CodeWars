def divisible_by(numbers, divisor):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result


print(divisible_by([0, 1, 2, 3, 4, 5, 6], 4))
