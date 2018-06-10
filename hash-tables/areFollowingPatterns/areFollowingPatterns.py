def areFollowingPatterns(strings: list, patterns: list):
    pattern2str = dict()
    str2pattern = dict()
    for s, p in zip(strings, patterns):
        s2 = pattern2str.get(p)
        p2 = str2pattern.get(s)
        if not s2 and not p2:
            pattern2str[p] = s
            str2pattern[s] = p
        elif s != s2 or p != p2:
            return False
    return True

