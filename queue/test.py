import unittest
from queue import Queue


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.q = Queue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

    def test_peek_an_element_to_queue(self):
        self.assertEqual(self.q.peek(), 1)

    def test_enqueue_an_element_to_queue(self):
        self.assertEqual(len(self.q.storage), 3)
        self.q.enqueue(4)
        self.assertEqual(len(self.q.storage), 4)
        self.assertEqual(self.q.storage[-1], 4)

    def test_dequeue_an_element_from_queue(self):
        self.assertEqual(len(self.q.storage), 3)
        self.q.dequeue()
        self.assertEqual(len(self.q.storage), 2)
        self.assertEqual(self.q.storage[0], 2)


if __name__ == '__main__':
    unittest.main()
