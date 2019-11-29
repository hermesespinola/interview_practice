# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        left, right = l1, l2
        root = ListNode(-1)
        current = root
        while left or right or c:
            left_val = left.val if left else 0
            right_val = right.val if right else 0
            res = left_val + right_val + c
            c = 1 if res > 9 else 0
            print(res, c)
            current.next = ListNode(res % 10)
            current = current.next
            if left:
                left = left.next
            if right:
                right = right.next
        return root.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print (result.val, end='')
    result = result.next
print()
# 7 0 8

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print (result.val, end='')
    result = result.next
print()
# 8 9 9 1

l1 = ListNode(1)
l1.next = ListNode(1)

l2 = ListNode(2)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print (result.val, end='')
    result = result.next
print()
# 3 1
