from main import Node, evaluate

tree = Node('*')
tree.left = Node('+')
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node('+')
tree.right.left = Node(4)
tree.right.right = Node(5)

res = evaluate(tree)
print(res)
# 45
assert(res == 45)
