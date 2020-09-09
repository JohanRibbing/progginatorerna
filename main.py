from matplotlib.pyplot import *
import numpy as np
import csv
from spline import Spline

#Function that reads a csv-file and returns a numpy array of control points
def read_Data(filename):
    d_s = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 0
        for row in csv_reader:
            if row_count == 0:
                row_count += 1
            else:
                d_s.append(tuple(float(x) for x in row))
                row_count += 1
    return np.array(d_s)

#Function that takes a numpy array of control points and returns a list of Knots (u_i)
def create_Knot(d_array):
    u_len = len(d_array) + 2
    us = np.linspace(0,1,u_len)
    us[1] = us[2] = us[0]
    us[-3] = us[-2] = us[-1]
    return us

#Setup: reads data files and creates lists of Knots
ds1 = read_Data('Data.csv')
us1 = create_Knot(ds1)
ds2 = np.genfromtxt("control.csv", dtype=float, delimiter=",")
us2 = create_Knot(ds2)

#Creation of splines
s1 = Spline(us1, ds1)
s2 = Spline(us2, ds2)

#Plot of splines
print(s1(0.2))
s1.plot(3)
#print(s2(0.2))
#s2.plot(3)
