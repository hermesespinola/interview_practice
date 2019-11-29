class Solution: 
    def getRange(self, arr, target):
        first, last = -1, -1
        found = False
        for i, x in enumerate(arr):
            if not found and x == target:
                first = i
                found = True
            elif found and x != target:
                last = i - 1
                return first, last
        # If the first is present but the last is not,
        # the target is present until the end of the array
        if first != -1:
            return first, len(arr) - 1
        return -1

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))

arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))

arr = [1, 1, 1, 5, 5, 5]
x = 1
print(Solution().getRange(arr, x))

x = 5
print(Solution().getRange(arr, x))

arr = [2, 2, 2, 2]
x = 2
print(Solution().getRange(arr, x))