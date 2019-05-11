"""
Linked List is a linear data structure where each element is a separate object.
Unlike arrays, linked list elements are not stored at contiguous location; the elements are linked using pointers.

llist.head         second              third
     |                |                  |
     |                |                  |
+----+------+     +----+------+     +----+------+
| 1  |  o-------->| 2  |  o-------->|  3 | null |
+----+------+     +----+------+     +----+------+

Representation:
A linked list is represented by a pointer to the first node of the linked list.
The first node is called head.
If the linked list is empty, then value of head is NULL.
The last node has a reference to null.

Each node in a list consists of at least two parts:
1) data
2) Pointer (Or Reference) to the next node

Advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion

Drawbacks:
1) Random access is not allowed. We have to access elements sequentially starting from the first node.
So we cannot do binary search with linked lists efficiently with its default implementation.
2) Extra memory space for a pointer is required with each element of the list.
3) Not cache friendly. Since array elements are contiguous locations,
there is locality of reference which is not there in case of linked lists.
"""


class Node(object):
    # Function to initialise the node object
    def __init__(self, value):
        self.value = value  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList(object):
    # Function to initialize head
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

    def get_position(self, position):
        current = self.head
        counter = 1

        if position < 1:
            return None

        while current:
            if counter == position:
                return current
            current = current.next
            counter += 1

        return None

    def insert(self, new_element, position):
        current = self.head
        counter = 1

        if position > 1:
            while current:
                if counter == position -1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter+=1

        elif position == 1:
            new_element.next = current
            current = new_element

    def delete(self, value):
        current = self.head
        previous = None

        while current.value != value and current.next:
            previous = current
            current = current.next

        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
