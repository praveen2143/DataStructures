class Node:
    def __init__(self, n):
        self.item = n
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    LL = LinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    LL.head = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    while LL.head is not None:
        print(LL.head.item, end=" ")
        LL.head = LL.head.next
