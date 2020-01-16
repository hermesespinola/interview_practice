from typing import Union

Number = Union[float, int]
Token = Union[Number, str]

class Node:
    def __init__(self, val: Token, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root: Node) -> Number:
    token = root.val

    if not isinstance(token, str):
        return token

    left_side = evaluate(root.left)
    right_side = evaluate(root.right)

    if token == PLUS:
        return left_side + right_side
    elif token == MINUS:
        return left_side - right_side
    elif token == TIMES:
        return left_side * right_side
    elif token == DIVIDE:
        return left_side / right_side
    else:
        return 0
