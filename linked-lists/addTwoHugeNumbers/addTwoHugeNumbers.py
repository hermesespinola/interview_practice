class ListNode(object):
  def __init__(self, x, n = None):
    self.value = x
    self.next = n

def addTwoHugeNumbers(a, b):
    A, B = [], []
    while a:
        A.append(a.value)
        a = a.next
    while b:
        B.append(b.value)
        b = b.next

    res = None
    carry = 0
    while A or B or carry:
        # next number from right to left
        # calculate sum with carry
        x = (A.pop() if A else 0) + (B.pop() if B else 0) + carry
        node = ListNode(x % 10000)
        node.next = res
        res = node
        carry = x / 10000
    return res
