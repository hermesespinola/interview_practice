hist = [0] * 26
order = []

def firstNotRepeatingCharacter(s):
    for c in s:
        if hist[ord(c) - ord('a')] == 0:
            order.append(c)
        hist[ord(c) - ord('a')] += 1

    for c in order:
        if hist[ord(c) - ord('a')] == 1:
            return c

    return '_'
