"""
A stack is a conceptual data type that serves as a collection of elements
and is based on the principle of last in first out (LIFO).

For example,
When you go to a japanese restaurant and have nice Sushis.
After you eat each of Sushi, you put the latest dish to previous one.
Then you're going to pay the bills, the server will come and check how many dishes you have.
Server will count the dishes from the lastest one to oldest one.
It's a stack way in our real life.

                        ------------                ------------  ------------  ------------
           last in ->   -3. salmon - -> first out    1. salmon  ->  2. tuna   ->  3. shrimp
                        ------------                ------------  ------------  ------------
                        -2. tuna  --
                        ------------
                        -1. shrimp -
                        ------------

Why didn't we just come up with a function for removing the last element and call it a day?
Every operation on a linked list must start with the head.
append() thus traverses the whole list, taking O(n).

Any operation on the last element requires us to traverse everything,
so even though we had to write a new method our code will run much faster if we push/pop from the first element in a linked list.
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """take o(n)"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        """take o(1)"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
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