def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_rshift_list(num):
    s = 1
    x = 0
    while x < ft_len(num) - 1:
        c = num[-s]
        num[-s] = num[-(s + 1)]
        num[-(s + 1)] = c
        x += 1
        s += 1
    return num
