import unittest
from stack import Stack, Element


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        e1 = Element(1)
        self.stack = Stack(e1)

    def test_push_element_to_stack(self):
        self.assertIsNone(self.stack.ll.head.next)
        self.assertEqual(self.stack.ll.head.value, 1)
        self.stack.push(Element(2))
        self.stack.push(Element(3))
        self.assertEqual(self.stack.ll.head.value, 3)

    def test_pop_element_from_stack(self):
        self.assertIsNone(self.stack.ll.head.next)
        self.stack.push(Element(2))
        self.stack.push(Element(3))
        self.stack.pop()
        self.assertEqual(self.stack.ll.head.value, 2)
        self.stack.pop()
        self.assertEqual(self.stack.ll.head.value, 1)


if __name__ == '__main__':
    unittest.main()
