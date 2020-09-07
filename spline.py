from scipy import *
from matplotlib.pyplot import *

class Spline:


    def __init__(self, us, ds):
        self.us = us
        self.ds = ds

    def plot(self):
        return

    def call(self,u):
        return
        #return (x,y)

    def hot_index(self,u):
        return
        #return index

    def alpha(self, u, n, k):
        u_leftmost = self.us[k-1]
        u_rightmost = self.us[k+3-n]
        return ((u_rightmost-u)/(u_rightmost-u_leftmost))
        #return alpha

