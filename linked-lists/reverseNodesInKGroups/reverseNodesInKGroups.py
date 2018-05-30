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

def reverseK(l, k):
    prev, last = l, l
    for i in xrange(k):
        if not prev:
            return None, last, None
        prev = prev.next
    c = l
    for i in xrange(k):
        if not c: break
        nxt = c.next
        c.next = prev
        prev = c
        c = nxt
    # return last and first
    # element of reversed list
    return c, prev, last

def reverseNodesInKGroups(l, k):
    c, l, last = reverseK(l, k)
    while (c):
        c, last.next, last = reverseK(c, k)
    return l
