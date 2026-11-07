
class Stack:

    def __init__(self):
        self.items = []

    # Add an element to the stack
    def push(self, value):
        self.items.append(value)
        print(value, "added to stack")

    # Remove the top element
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            removed = self.items.pop()
            print(removed, "removed from stack")

    # Show the top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.items[-1])

    # Check whether stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display all elements
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack:", self.items)


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()

s.pop()
s.display()
