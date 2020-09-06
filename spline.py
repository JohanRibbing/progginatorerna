from scipy import *
from matplotlib.pyplot import *

class Spline:

    def __init__(self, d):
        self.d = d
        self.us = linspace(0,1,10)

    def display(self):
        return self.d
    
#Vad vi behöver
#init: tuple/lista med tuples (d)
#plot: plotta olika s(u) (Johan)
#call - rekursiv funktion (tar in ett givet u - ger en coordinat som en tuple (x,y))
#hot interval och välj d-punkter (tar in u och(genom att hitta två tabelltider) ger en lista med fyra d-tupl (hot interval)
#alpha(u) tar in två hållplatser och u och ger en siffra (Seamus)