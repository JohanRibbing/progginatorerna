from spline import Spline
from scipy import *
from matplotlib.pyplot import *
import numpy

ds = 2, 3, 4, 5
us = numpy.linspace(0,1,5)
s = Spline(ds,us)

#Något som läser in d:na från fil (tar in filnamn som string och returnerar en lista med tuples)
#Instansierar splinen med listan med tuples
#kallar på plotfunktionen
#Seamus