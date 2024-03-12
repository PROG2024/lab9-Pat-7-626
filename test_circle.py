"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest, pytest, math


class CircleTest(unittest.TestCase):
    """Tests of Circle"""

    def setUp(self):
        """Set up"""
        self.c1 = Circle(3)
        self.c2 = Circle(5)
        self.c3 = Circle(0)

    def test_add_area(self):
        """Typical case"""
        new1 = self.c1.add_area(self.c2)
        hy1 = math.hypot(3, 5)
        self.assertEqual(new1.get_radius(), hy1)
        self.assertEqual(new1.get_area(), math.pi*hy1*hy1)

        new2 = self.c2.add_area(self.c1)
        hy2 = math.hypot(5, 3)
        self.assertEqual(new2.get_radius(), hy2)
        self.assertEqual(new2.get_area(), math.pi*hy2*hy2)

        new3 = self.c1.add_area(self.c1)
        hy3 = math.hypot(3, 3)
        self.assertEqual(new3.get_radius(), hy3)
        self.assertEqual(new3.get_area(), math.pi*hy3*hy3)

        new4 = self.c2.add_area(self.c2)
        hy4 = math.hypot(5, 5)
        self.assertEqual(new4.get_radius(), hy4)
        self.assertEqual(new4.get_area(), math.pi*hy4*hy4)

    def test_add_area_zero(self):
        """Edge case"""
        new1 = self.c1.add_area(self.c3)
        hy1 = math.hypot(3, 0)
        self.assertEqual(new1.get_radius(), hy1)
        self.assertEqual(new1.get_area(), math.pi*hy1*hy1)

        new2 = self.c3.add_area(self.c1)
        hy2 = math.hypot(0, 3)
        self.assertEqual(new2.get_radius(), hy2)
        self.assertEqual(new2.get_area(), math.pi*hy2*hy2)

    def test_negative_radius(self):
        """Circle constructor raises exception if the radius is negative"""
        with pytest.raises(ValueError):
            self.new = Circle(-1)
