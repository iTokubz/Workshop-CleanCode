def process_data(data):
    x = []
    y = []
    z = []
    for i in data:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    return x, y, z
