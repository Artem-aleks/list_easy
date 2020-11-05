def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_rev_list(a):
    i = 0
    while i != ft_len(a) // 2:
        a[i], a[-i - 1] = a[-i - 1], a[i]
        i += 1
    return a
