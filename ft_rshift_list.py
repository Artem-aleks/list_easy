def ft_len(v):
    b = 0
    for i in v:
        b += 1
    return b


def ft_rshift_list(num):
    w = ft_len(num)
    w = w - 1
    q = []
    i = 1
    q.append(num[w - 1])
    w = w - 1
    for i in range(w):
        q.append(num[i])
        i = i + 1
    return q
