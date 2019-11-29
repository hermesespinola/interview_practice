#!/usr/local/bin/python3

class Solution:
    def longestPalindrome(self, s):
        isPalindrome = lambda s: s == s[::-1]
        longest = ''
        for idx in range(len(s)):
            # Odd length
            left_range = range(idx, -1, -1)
            right_range = range(idx + 1, (idx * 2) + 2)
            for i, j in zip(left_range, right_range):
                substrEven = s[i:j]
                print("test subs:", substrEven)
                if isPalindrome(substrEven) and len(substrEven) > len(longest):
                    print('found:', substrEven)
                    longest = substrEven

                substrOdd = s[i:j+1]
                if isPalindrome(substrOdd) and len(substrOdd) > len(longest):
                    print('found:', substrOdd)
                    longest = substrOdd

        return longest

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar

s = "123anitalavalatina"
print(str(Solution().longestPalindrome(s)))
# anitalavalatina


s = "abbasss"
print(str(Solution().longestPalindrome(s)))
# abba
