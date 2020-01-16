class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

def serialize(root: Node) -> str:
    def serialize_helper(root: Node) -> str:
        result = str(root.val) + ' '
        if root.left:
            result += serialize_helper(root.left)
        else:
            result += '# '
        if root.right:
            result += serialize_helper(root.right)
        else:
            result += '# '
        return result

    return serialize_helper(root).strip()

def deserialize(data: str) -> Node:
    def deserialize_helper(data: str, i: int) -> (Node, int):
        if i >= len(data):
            return None, i

        symbol = data[i]
        if symbol == ' ':
            raise 'Wrong serialized data'

        if symbol == '#':
            return None, i

        val = int(symbol)

        left_node, left_end = deserialize_helper(data, i + 2)
        right_node, right_end = deserialize_helper(data, left_end + 2)

        return Node(val, left_node, right_node), right_end

    deserialized, _ = deserialize_helper(data, 0)
    return deserialized
