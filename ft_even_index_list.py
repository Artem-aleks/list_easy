def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_even_index_list(num):
    a = []
    for i in range(0, ft_len(num), 2):
        a.append(num[i])
    return a
