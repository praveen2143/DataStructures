class graph:
    def __init__(self, n):
        self.size = n
        self.adjacencyMatrix = []
        for i in range(n):
            self.adjacencyMatrix.append([0 for i in range(n)])

    def addedge(self, start, end):
        self.adjacencyMatrix[start][end] = 1
        self.adjacencyMatrix[end][start] = 1

    def printgraph(self):
        for row in self.adjacencyMatrix:
            for item in row:
                print(item,end=" ")
            print()


if __name__ == '__main__':
    g = graph(5)
    g.addedge(1,2)
    g.addedge(0, 1)
    g.addedge(2 , 3)
    g.addedge(3, 4)
    g.printgraph()