def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_sl_list(num):
    x = 0
    i = 1
    while i != ft_len(num):
        if num[i - 1] < num[i]:
            x = x + 1
            i += 1
    return x
