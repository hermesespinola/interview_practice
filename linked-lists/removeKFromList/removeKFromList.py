class ListNode(object):
  def __init__(self, x, n = None):
    self.value = x
    self.next = n

def removeKFromList(l, k):
    current = l
    while current:
        if current.next and current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next
    return l.next if l and l.next.value == k else l

l = ListNode(3, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
removed = removeKFromList(l, 3)
while removed != None:
    print removed.value,
    removed = removed.next
