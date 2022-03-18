"""
A number queue is a queue created in Python using numbers.

A queue is an object (an abstract data structure - ADT) that allows the following operations:
Enqueue: Add an element to the end of the queue
Dequeue: Remove an element from the front of the queue
IsEmpty: Check if the queue is empty
IsFull: Check if the queue is full
Peek: Get the value of the front of the queue without removing it
"""

class Queue:
    """A Queue implementation using the list """
    def __init__(self, head=None):
        # list can be used as a storage structure because it is ordered but only for demonstation,
        # use deque from collection for production use case
        self.queue = [head]
    
    def enqueue(self, value):
        if value:
            self.queue.append(value)

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
        else:
            print("Queue is empty for now")
        
    def viewQueue(self):
        print(self.queue)

if __name__ == "__main__":
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    # should be [1,2,3]
    q.viewQueue()

    # should be [2,3]
    q.dequeue()
    q.viewQueue()

    # should be [3]
    q.dequeue()
    q.viewQueue()

    # should print "Queue is empty for now"
    q.dequeue()
    q.dequeue()
