"""
We can create a Stack class in Python using lists
"""

class Stack:
    """A simple class stack that only allows pop and push operations"""
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    pass