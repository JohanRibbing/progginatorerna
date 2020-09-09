from spline import Spline
from matplotlib.pyplot import *
import numpy as np

def create_Knot(d_array):
    u_len = len(d_array) + 2
    us = np.linspace(0,1,u_len)
    us[1] = us[2] = us[0]
    us[-3] = us[-2] = us[-1]
    return us

ds2 = np.genfromtxt("control.csv", dtype=float, delimiter=",")
us2 = create_Knot(ds2)

s2 = Spline(us2, ds2)

xys = [s2.spline_basis_representation(z) for z in np.linspace(0.05, 0.95, 100)]

xs, ys = zip(*xys)

scatter(xs, ys)

show()