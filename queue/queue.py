"""
A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,”
Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:

    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        return self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)