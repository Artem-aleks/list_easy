def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_rshift_list(num):
    z = ft_len(num)
    n = 0
    while z - 1 > n:
        c = num[-z]
        num[-z] = num[-(z + 1)] = c
        n += 1
        z += 1
    return num
