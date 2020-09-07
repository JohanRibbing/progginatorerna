import numpy

class Spline:
    
    def __init__(self, us, ds):
        self.us = us
        self.ds = ds

    def plot(self):
        return

    def call(self, u):
        return
        #return (x,y)

    def hot_index(self, u):
        """
        From a given u find the hot index.
        :param u: given u
        :return: index
        """
        for i, gp in enumerate(self.us):
            if gp > u:
                return i, gp

    def alpha(self, u, n, k):
        return 
        #return alpha

