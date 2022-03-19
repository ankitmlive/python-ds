"""
A Stack implementation using custom Linked List in Python
List in python are actually an Stack implementation, but we can create it using linked list.
Stack follows LIFO: Last In, First Out
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value, end=" ")
            temp = temp.next

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element
        
    def delete_first(self):
        "Delete the first (head) element in the LinkedList and return it"
        if self.head:
            deleted = self.head
            self.head = deleted.next
            return deleted
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
    
    def viewStack(self):
        self.ll.print_list()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

# Start setting up a Stack
stack = Stack(e1)
stack.push(e2)
stack.push(e3)
# should print: 3,2,1,None
print(stack.viewStack())

print("removing from stack", stack.pop().value)
print("removing from stack", stack.pop().value)
print("removing from stack", stack.pop().value)
# should print: 3,2,1,None
print(stack.viewStack())
stack.push(e4)
stack.push(e5)
print("removing from stack", stack.pop().value)
# should print: 4,None
print(stack.viewStack())
