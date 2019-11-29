#!/usr/local/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        longestLen = 0
        start = 0
        seen = set()
        end = 0
        for end, c in enumerate(s):
            code = ord(c)
            if code in seen:
                checkChar = ord(s[start])
                start += 1
                while start < end and checkChar != code:
                    seen.remove(checkChar)
                    checkChar = ord(s[start])
                    start += 1

            if end - start > longestLen - 1:
                longestLen = end - start + 1
            seen.add(code)

        return longestLen

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10

print(Solution().lengthOfLongestSubstring("abcabcbb"))
# 3

print(Solution().lengthOfLongestSubstring("pwwkew"))
# 3

print(Solution().lengthOfLongestSubstring("dvdf"))
# 3
