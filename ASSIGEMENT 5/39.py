class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def serialize(root):
    if not root:
        return "None"

    return (str(root.val) + "," +
            serialize(root.left) + "," +
            serialize(root.right))


def deserialize(data):
    values = iter(data.split(","))

    def build():
        val = next(values)

        if val == "None":
            return None

        node = Node(int(val))
        node.left = build()
        node.right = build()

        return node

    return build()


root = Node(1)
root.left = Node(2)
root.right = Node(3)

data = serialize(root)
print("Serialized:", data)

new_root = deserialize(data)
print("Root:", new_root.val)






"""Serialized: 1,2,None,None,3,None,None
Root: 1"""