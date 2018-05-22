def isCryptSolution(crypt, solution):
    d = { sol[0]: sol[1] for sol in solution }
    decoded = ["".join([d[c] for c in word]) for word in crypt]
    hasNoLeadingZeroes = [len(s) == 1 or s[0] != '0' for s in decoded]
    return all(hasNoLeadingZeroes) and int(decoded[0]) + int(decoded[1]) == int(decoded[2])
