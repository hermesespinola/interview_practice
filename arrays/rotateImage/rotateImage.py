def rotateImage(a):
    n = len(a)

    for i in range(n / 2): # each section
        for j in range(i, n - i - 1): # count all
            row, col = i, j
            # store the element being replaced
            tmp = a[i][j]
            for _ in range(4):
                # calculate the 90 deg rotation
                row, col = col, n - row - 1
                # swap tmp and next element
                a[row][col], tmp = tmp, a[row][col]
    return a

# Much functional
# Very programming
rotateImage2 = lambda a: zip(*a[::-1])
