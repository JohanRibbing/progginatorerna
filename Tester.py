from spline import Spline
from main import read_Data, create_Knot
import unittest
import numpy as np

class TestIdentity(unittest.TestCase):
    def test(self):
        ds = read_Data("Data.csv")
        us = create_Knot(ds)
        s = Spline(us, ds)
        u_interval = np.linspace(0,1,100).tolist()
        s_blossoms = [s(u) for u in u_interval]
        s_basis = [s.spline_basis_representation(u) for u in u_interval]
        result = s_blossoms
        expected = s_basis
        for i in range(0,len(u_interval) - 1):
            self.assertAlmostEqual(result[i][0], expected[i][0])
            self.assertAlmostEqual(result[i][1], expected[i][1])

if __name__=='__main__':
    unittest.main()