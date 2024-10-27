import unittest
from src.app import get_message

class TestApp(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Hello, Jenkins!")

if __name__ == '__main__':
    unittest.main()

