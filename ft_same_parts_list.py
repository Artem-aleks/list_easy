def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_same_parts_list(num):
    i = 1
    while i != ft_len(num):
        if (num[i - 1] > 0 and num[i] > 0) or (num[i - 1] < 0 and num[i] < 0):
            i += 1
            return True
    return False
