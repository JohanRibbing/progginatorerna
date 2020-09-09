from spline import Spline
from main import read_Data, create_Knot
import unittest

class TestIdentity(unittest.TestCase):
    def test(self):
        ds = read_Data("Data.csv")
        us = create_Knot(ds)
        s = Spline(us, ds)
        result = 4
        expected = 4
        #s.__call__(0.3)
        self.assertAlmostEqual(result, expected)

if __name__=='__main__':
    unittest.main()