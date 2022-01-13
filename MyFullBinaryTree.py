class Node:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None


def isfullbinarytree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return isfullbinarytree(root.left) and isfullbinarytree(root.right)

    return False


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
#root.left.right = Node(4)
root.right = Node(5)
if isfullbinarytree(root):
    print("Tree is a Full Binary tree")
else:
    print("Tree is Not a Full Binary tree")