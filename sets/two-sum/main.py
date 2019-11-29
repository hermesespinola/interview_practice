def two_sum(numbers, k):
    complements = set()
    for x in numbers:
        if x in complements:
            return True
        complements.add(k - x)
    return False

print(two_sum([4,7,1,-3,2], 5))
# True

print(two_sum([5,7,1,-3,2], 5))
# False

print(two_sum([5,7,1,-2,2], 5))
# True
