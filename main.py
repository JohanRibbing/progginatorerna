from spline import Spline
from scipy import *
from matplotlib.pyplot import *

d = 2, 3, 4, 5
s = Spline(d)
print(s.display())

#Något som läser in d:na från fil (tar in filnamn som string och returnerar en lista med tuples)
#Instansierar splinen med listan med tuples
#kallar på plotfunktionen
#Seamus