class Node:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None


def InOrderTraversal(root):
    if root:
        InOrderTraversal(root.left)
        print(str(root.key) + "->", end=" ")
        InOrderTraversal(root.right)


def PreOrderTraversal(root):
    if root:
        print(str(root.key) + "->", end=" ")
        PreOrderTraversal(root.left)
        PreOrderTraversal(root.right)


def PostOrderTraversal(root):
    if root:
        PostOrderTraversal(root.left)
        PostOrderTraversal(root.right)
        print(str(root.key) + "->", end=" ")


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    InOrderTraversal(root)
    print()
    PreOrderTraversal(root)
    print()
    PostOrderTraversal(root)
