def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_rev_par_list(num):
    if ft_len(num) % 2 == 0:
        i = 0
        while i != ft_len(num):
            num[i], num[i + 1] = num[i + 1], num[i]
            i += 2
        return num
    else:
        i = 0
        while i != ft_len(num) - 1:
            num[i], num[i + 1] = num[i + 1], num[i]
            i += 2
        return num
