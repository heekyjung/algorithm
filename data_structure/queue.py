class Queue:
    # CreateQueue
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.rear == -1

    def is_full(self):
        return self.rear == self.size - 1

    def add(self, element):
        if self.is_full():
            print("Queue is full.")
            return
        else:
            self.rear += 1
            self.queue[self.rear] = element
            return

    def delete(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        else:
            self.front += 1
            element = self.queue[self.front]
            return element

    def display(self):
        print(self.queue[self.front+1:self.rear+1])
        return


queue = Queue(3)
queue.delete()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.delete()
queue.display()
