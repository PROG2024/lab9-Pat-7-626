"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
import pytest
from counter import Counter


class CounterTest(unittest.TestCase):
    """Tests of the Counter class."""

    def setUp(self):
        self.c1 = Counter()
        self.c2 = Counter()

    def test_singleton1(self):
        self.c1.increment()
        self.assertEqual(self.c1.count, self.c2.count)

    def test_singleton2(self):
        self.assertEqual(id(self.c1), id(self.c2))
