from spline import Spline
from main import read_Data, create_Knot
import unittest

class TestIdentity(unittest.TestCase):
    def test(self):
        ds = read_Data(Data.csv)
        us = create_Knot(ds)
        s = Spline(us, ds)
        #result =
        #expected =
        #self.assertAlmostEqual(result, expected)