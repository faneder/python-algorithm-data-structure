import unittest
from linkedList import Node, LinkedList


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # Set up Nodes
        e1 = Node(1)
        e2 = Node(2)
        e3 = Node(3)

        # Start setting up a LinkedList
        self.ll = LinkedList(e1)
        self.ll.append(e2)
        self.ll.append(e3)

    def test_get_linkedlist_value(self):
        """
        Test linkedlist value between 1 and 3, should return value from 1 to 3
        """
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.head.next.value, 2)
        self.assertEqual(self.ll.head.next.next.value, 3)

    def test_node_not_in_list(self):
        self.assertEqual(self.ll.head.next.next.next, None)

    def test_get_position_value(self):
        """
        get_position will return the element at a certain position.
        """
        self.assertEqual(self.ll.get_position(1).value, 1)
        self.assertEqual(self.ll.get_position(2).value, 2)
        self.assertEqual(self.ll.get_position(3).value, 3)

    def test_insert_position(self):
        """
        insert function will add an element to a particular spot in the list.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        """
        e4 = Node(4)
        self.ll.insert(e4, 3)
        self.assertEqual(self.ll.get_position(3).value, 4)

    def test_delete_value(self):
        """
        delete will delete the first element with that particular value.
        """
        self.ll.delete(1)
        self.assertEqual(self.ll.get_position(1).value, 2)
        self.assertEqual(self.ll.get_position(2).value, 3)


if __name__ == '__main__':
    unittest.main()
