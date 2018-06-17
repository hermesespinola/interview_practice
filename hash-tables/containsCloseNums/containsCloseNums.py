def containsCloseNums(nums, k):
    last = dict()
    for i, n in enumerate(nums):
        if n in last and -k <= i - last[n] <= k:
                return True
        last[n] = i
    return False

nums = [0, 1, 2, 3, 5, 2]
k = 3
print(containsCloseNums(nums, k))
