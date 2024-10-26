import unittest
import q1

class TestQ1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(q1.most_frequent_lengths(['a', 'ab', 'abc', 'cd', 'def', 'gh']), ['ab', 'cd', 'gh'])

    def test_2(self):
        self.assertEqual(q1.most_frequent_lengths(['apple', 'pie', 'banana', 'kiwi', 'orange']), ['banana', 'orange'])

    def test_3(self):
        self.assertEqual(q1.most_frequent_lengths(['a', 'aa', 'aaa', 'ab', 'lmao', 'ac']), ['aa', 'ab', 'ac'])

    def test_4(self):
        self.assertEqual(q1.most_frequent_lengths(['hello', 'world', 'python', 'code']), ['hello', 'world'])

    def test_5(self):
        self.assertEqual(q1.most_frequent_lengths(['one', 'two', 'three', 'four', 'five', 'six']), ['one', 'two', 'six'])


if __name__ == '__main__':
    unittest.main()