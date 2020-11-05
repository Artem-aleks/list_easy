def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_even_parts_list(num):
    a = []
    for i in range(1, ft_len(num), 2):
        a.append(num[i])
    return a
