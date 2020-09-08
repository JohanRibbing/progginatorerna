from matplotlib.pyplot import *
import numpy as np
import csv
from spline import Spline

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
    return d_s

ds1 = np.array(read_Data('Data.csv'))
#us = numpy.linspace(0,1,5)
#s = Spline(ds,us)

ds2 = np.genfromtxt("control.csv", dtype=float, delimiter=",")
us = np.linspace(0, 1, 26)
us[ 1] = us[ 2] = us[ 0]
us[-3] = us[-2] = us[-1]
print(us)

siv = Spline(us, ds2)
print(siv(0.2))
siv.plot()
#Något som läser in d:na från fil (tar in filnamn som string och returnerar en lista med tuples)

#Instansierar splinen med listan med tuples
#kallar på plotfunktionen
#Seamus
