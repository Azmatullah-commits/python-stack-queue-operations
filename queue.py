
class Queue:

    def __init__(self):
        self.items = []

    # Add an element to the queue
    def enqueue(self, value):
        self.items.append(value)
        print(value, "added to queue")

    # Remove the first element
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            removed = self.items.pop(0)
            print(removed, "removed from queue")

    # Show the first element
    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element:", self.items[0])

    # Check whether queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display all elements
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.items)


# Main program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
q.front()

q.dequeue()
q.display()
