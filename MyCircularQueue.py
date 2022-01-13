class MyCircularQueue:
    def __init__(self, n):
        self.front = -1
        self.rear = -1
        self.k = n
        self.q = [None] * n

    def QueueEnqueue(self, n):
        if (self.rear + 1) % self.k == self.front:
            print("Circular queue is Full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.q[self.rear] = n
        else:
            self.rear = (self.rear + 1) % self.k
            self.q[self.rear] = n

    def QueueDequeue(self):
        if self.front == -1:
            print("Circular Queue is Empty..")
        elif self.front == self.rear:
            print("Element popped is " + str(self.q[self.front]))
            self.front = -1
            self.rear = -1
        else:
            print("Element popped is " + str(self.q[self.front]))
            self.front = (self.front + 1) % self.k


q = MyCircularQueue(5)
q.QueueEnqueue(1)
print(q.q)
q.QueueEnqueue(2)
print(q.q)
q.QueueEnqueue(3)
print(q.q)
q.QueueEnqueue(4)
print(q.q)
q.QueueEnqueue(5)
print(q.q)
q.QueueDequeue()
q.QueueDequeue()
q.QueueDequeue()
q.QueueEnqueue(6)
print(q.q)
