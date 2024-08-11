# tests/test_sample.py

import unittest
from my_sample_module.sample import greet

class TestSample(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
