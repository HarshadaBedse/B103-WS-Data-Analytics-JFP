class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca(root, p, q):
    if root is None or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left or right


root = Node(3)
root.left = Node(5)
root.right = Node(1)

p = root.left
q = root.right

result = lca(root, p, q)

print("Lowest Common Ancestor:", result.val)






"""Lowest Common Ancestor: 3"""