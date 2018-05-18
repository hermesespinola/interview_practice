# IDEA: use generators

def sudoku2(grid):
    # map of elements seen in each row, col and subgrid
    seen = [[set(), set(), set()] for _ in xrange(9)]
    for i in xrange(9):
        for j in xrange(9):
            n = grid[i][j]
            if n != '.':
                subgrid = i / 3 + j / 3 * 3
                if n in seen[i][0] or n in seen[j][1] or n in seen[subgrid][2]:
                    return False
                seen[i][0].add(n)
                seen[j][1].add(n)
                seen[subgrid][2].add(n)
    return True
