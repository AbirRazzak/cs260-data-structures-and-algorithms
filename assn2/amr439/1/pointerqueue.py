#!/usr/bin/python3

# (10 points) Queues: one implementation, pointer (Textbook pages 57-60)
# Operations: FRONT, ENQUEUE, DEQUEUE, EMPTY, MAKENULL

class Cell:
    value = None
    next = None

    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt

class Queue:
    head = None
    tail = None

    def __init__(self, hd=None, tl=None):
        self.head = hd
        self.tail = tl

   # Inserts a new element to the end of the queue
    def enqueue(self, x):
        if self.head is None and self.tail is None:
            # Queue's empty
            self.head = x
            self.tail = x
            return
        else:
            # Add to end of queue
            self.tail.next = x
            self.tail = x

    # Deletes the first element on the queue
    def dequeue(self):
        if self.head.next is not None:
            self.head = self.head.next
        else:
            # Head is the only thing left
            self.head = None
            self.tail = None

    # Returns the first element on queue
    def front(self):
        return self.head

    # Returns true if and only if queue is empty
    def empty(self):
        return self.head is None and self.tail is None

    # Makes the queue an empty list
    def makenull(self):
        self.head = None
        self.tail = None

    def display(self):
        i = self.head
        while i is not None:
            print(i.value)
            i = i.next

if __name__ == '__main__':
    q = Queue()
    print("Inserting 5 and 7 into queue")
    print("Expected outputs: 5 7")
    q.enqueue(Cell(5))
    q.enqueue(Cell(7))
    q.display()

    print("")

    print("Getting first of queue")
    print("Expected output: 5")
    print(q.front().value)

    print("")

    print("Checking if queue is empty")
    print("Expected output: Not empty here.")
    if q.empty():
        print("Yikes, that's a problem.")
    else:
        print("Not empty here.")

    print("")

    print("Delete first element from queue")
    print("Expected output: 7")
    q.dequeue()
    q.display()

    print("")

    print("Make entire queue null")
    print("Expected output: Nothing here!")
    q.makenull()
    if q.empty():
        print("Nothing here!")
    else:
        print("Yeah... that's gonna be a problem...")
