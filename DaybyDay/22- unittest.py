import unittest

def add(x, y):
    return x + y

class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, -3), -5)

if __name__ == "__main__":
    unittest.main()