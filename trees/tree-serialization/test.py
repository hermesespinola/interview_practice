from main import Node, serialize, deserialize

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

res = serialize(tree)
expected = '1 3 2 # # 5 # # 4 # 7 # #'
print('result: ' + res)
print('expected: ' + expected)
assert(res == expected)

res = deserialize(expected)
print('result: ' + str(res))
print('expected: ' + str(tree))
assert(res.val == 1)
assert(res.left.val == 3)
assert(res.left.left.val == 2)
assert(res.left.right.val == 5)
assert(res.right.val == 4)
assert(res.right.right.val == 7)
# 132547
