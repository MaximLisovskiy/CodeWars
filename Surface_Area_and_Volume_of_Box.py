def get_size(w, h, d):
    result = []
    volume = w * h * d
    area = 2 * (w * h + w * d + h * d)
    result.append(area)
    result.append(volume)
    return result


print(get_size(4, 2, 6))
