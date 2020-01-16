def firstDuplicate(a):
    for i in range(len(a)):
        if a[abs(a[i]) - 1] > 0:
            a[abs(a[i]) - 1] *= -1
        else:
            return abs(a[i])
    return -1
