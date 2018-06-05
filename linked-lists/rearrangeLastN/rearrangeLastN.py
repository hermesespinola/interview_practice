class ListNode(object):
  def __init__(self, x, n = None):
    self.value = x
    self.next = n

def rearrangeLastN(l, n):
    if not l or n == 0: 
        return l
        
    new_last, last = l, l
    for _ in range(n):
        last = last.next
    if not last:
        return l

    while last.next:
        last = last.next
        new_last = new_last.next
    
    # bind last node with first node
    last.next = l
    new_head = new_last.next
    new_last.next = None

    return new_head
