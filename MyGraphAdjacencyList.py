class AdjNode:
    def __init__(self, n):
        self.vertex = n
        self.next = None


class Graph:
    def __init__(self, n):
        self.size = n
        self.adjlist = [AdjNode(i) for i in range(n)]

    def add_edge(self,start,end):
        newnode1 = AdjNode(end)
        newnode1.next = self.adjlist[start].next
        self.adjlist[start].next = newnode1

        newnode = AdjNode(start)
        newnode.next = self.adjlist[end].next
        self.adjlist[end].next = newnode

    def print_graph(self):
        for node in self.adjlist:
            print("%d->" % node.vertex, end=" ")
            while node.next is not None:
                node = node.next
                print(node.vertex,end=" ")
            print()


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.print_graph()


