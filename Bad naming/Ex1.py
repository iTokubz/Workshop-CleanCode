def fn(a, b):
    r = 0
    for i in range(a):
        for j in range(b):
            r += i * j
    return r
