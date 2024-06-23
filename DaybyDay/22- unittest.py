import unittest
import re

def add(x, y):
    return x + y

class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, -3), -5)

def validate_email(email):
    return True if re.search(r'^\w+@\w+\.\w+', email) else False

class EmailTest(unittest.TestCase):
    def test_email(self):
        self.assertTrue(validate_email('ahmedtarek1754@gmail.com'))
        self.assertFalse(validate_email('ahmedtarek1754gmail.com'))
        self.assertFalse(validate_email('ahmedtarek1754@gmailcom'))

if __name__ == "__main__":
    unittest.main()