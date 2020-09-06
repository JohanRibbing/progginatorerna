from scipy import *
from matplotlib.pyplot import *

class Spline:

    def __init__(self, d):
        self.d = d
        self.us = linspace(0,1,10)

    def display(self):
        return self.d
    
