from matplotlib.pyplot import *
import numpy as np
from spline import Spline

ds = np.genfromtxt("control.csv", dtype=float, delimiter=",")
print(ds)
#Seamus fixar us så att det blir robust
us = np.linspace(0, 1, 26)
us[ 1] = us[ 2] = us[ 0]
us[-3] = us[-2] = us[-1]
print(us)

siv = Spline(us, ds)
print(siv(0.2))
siv.plot()
#Något som läser in d:na från fil (tar in filnamn som string och returnerar en lista med tuples)

#Instansierar splinen med listan med tuples
#kallar på plotfunktionen
#Seamus
