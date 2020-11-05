def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_positive_list(num):
    f = ft_len(num)
    k = 0
    x = 0
    for x in range(f):
        if num[x] > 0:
            k += 1
        x += 1
    return k
