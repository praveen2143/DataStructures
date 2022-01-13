class Node:
    def __init__(self, n):
        self.value = n
        self.left = None
        self.right = None


def calculateDepth(root):
    depth = 0
    while root is not None:
        depth = depth + 1
        root = root.left
    return depth


def isPerfectBinaryTree(root, depth, level=0):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return depth == level + 1

    if root.left is not None and root.right is not None:
        return (isPerfectBinaryTree(root.left, depth, level + 1) and isPerfectBinaryTree(root.right, depth, level + 1))

    return False


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(4)
    root.right.right = Node(5)
    d = calculateDepth(root)
    if isPerfectBinaryTree(root, d, 0):
        print("It is a Perfect Binary tree")
    else:
        print("It is not a Perfect Binary tree")
