class ListNode(object):
  def __init__(self, x, n = None):
    self.value = x
    self.next = n

def printList(l):
    c = l
    while c:
        print c.value,
        c = c.next
    print

def isListPalindrome(l):
    slow, fast = l, l
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # If fast is None the list size is even
    curr, prev = slow.next if fast else slow, None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    slow = prev

    while slow:
        if slow.value != l.value:
            return False
        l = l.next
        slow = slow.next
    return True

l = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
printList(l)
print isListPalindrome(l)
l = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2)))))
printList(l)
print isListPalindrome(l)
l = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
printList(l)
print isListPalindrome(l)
