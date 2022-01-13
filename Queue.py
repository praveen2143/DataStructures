class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, num):
        self.q.append(num)

    def dequeue(self):
        if len(self.q) < 0:
            print("Queue is empty")
        else:
            print("Dequeued Element is " + str(self.q.pop(0)))


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.q)
