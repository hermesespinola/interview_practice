"""
Given a pattern and a string input - find if the string follows the same pattern
and return 0 or 1.
Examples:
1) Pattern : "abab", input: "redblueredblue" should return 1.
2) Pattern: "aaaa", input: "asdasdasdasd" should return 1.
3) Pattern: "aabb", input: "xyzabcxzyabc" should return 0.
"""
from copy import copy as copy

def find_all(a_str, sub):
    step = len(sub)
    start = 0
    idxs = []
    idx = 0
    while idx != -1:
        idx = a_str.find(sub, start)
        if idx != -1:
            start = idx + len(sub)
            idxs.append(idx)
    return idxs

def patternMatches(pattern, string):
    simbol_count = {}
    for simbol in pattern:
        simbol_count[simbol] = simbol_count.get(simbol, 0) + 1
    print (simbol_count)

    def helper(pattern, string):

        # Resolve first simbol in pattern
        simbol = pattern[0]
        sub_end = 1
        sub = string[:sub_end]
        start_idxs = find_all(string, sub)

        # increment the substring of the simbol
        while len(start_idxs) > simbol_count[simbol]:
            sub_range[1] += 1
            sub = string[:sub_end]
            start_idxs = find_all(string, sub)

        # Impossible to have less substrings than simbols in pattern
        if len(start_idxs) < simbol_count[simbol]:
            return False

        # len(start_idxs) == simbol_count[simbol]
        # Maybe a pattern, check recursively for the next simbol
        new_string = '|'.join(string.split(sub))
        new_pattern = '|'.join(pattern.split(simbol))
        simbol_count.pop(simbol)
        return helper(new_pattern, new_string)

    return helper(pattern, string)



# def patternMatches(p,s):
#
#     # mapping is a dictionary that maps a character in p to a
#     # substring of s
#     def helper(p, s, mapping):
#         # pattern is longer than provided string. not possible
#         if len(p) > len(s):
#             return False
#         # both pattern and string ran out at the same time. yay
#         if len(p) == 0 and len(s) == 0:
#             return True
#         # pattern ran out but not the string. boo
#         if len(p) == 0:
#             return False
#
#         # current key we're considering
#         key = p[0]
#         # if key is already included in our mapping, check if s indeed
#         # begins with the value of this key. if not, then we can't
#         # continue with this particular set of mapping
#         if key in mapping:
#             mapped = mapping[key]
#             if s.startswith(mapped):
#                 return helper(p[1:],s[len(mapped):],mapping)
#             else:
#                 return False
#         # if key doesn't exist in our mapping, then we brute-force-ly
#         # guess all substrings of s to be the value of this key and
#         # recursively call patternMatches on each map
#         else:
#             for i in range(1,len(s)):
#                 guess = s[:i]
#                 #this guess_mapping is very important. it allows us to
#                 #try different keys in the recursive calls w/o affecting
#                 #our original mapping
#                 guess_mapping = copy(mapping)
#                 guess_mapping[key] = guess
#                 if helper(p[1:],s[len(guess):],guess_mapping):
#                    return True
#
#         return False
#
#     return helper(p,s,{})

print(patternMatches("abab", "redblueredblue"))
print(patternMatches("aaaa", "asdasdasdasd"))
print(patternMatches("abab", "xyzabcxzyabc"))
print(patternMatches("abcb", "xyzabcxzyabc"))
