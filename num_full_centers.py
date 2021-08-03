def num_full(centers):
    full = 0
    num = centers.values()
    for i in num:
        if i == 100:
            full += 1
    return full