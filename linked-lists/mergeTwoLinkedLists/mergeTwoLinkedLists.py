class ListNode(object):
  def __init__(self, x, n = None):
    self.value = x
    self.next = n

def mergeTwoLinkedLists(l1, l2):
    res = c = ListNode(0)
    while l1 and l2:
        if l1.value < l2.value:
            c.next = ListNode(l1.value)
            l1 = l1.next
        else:
            c.next = ListNode(l2.value)
            l2 = l2.next
        c = c.next
    c.next = l1 or l2
    return res.next
