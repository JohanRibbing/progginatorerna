import matplotlib.pyplot as plt
import numpy as np
import scipy

class Spline:

    def __init__(self, us, ds):
        self.us = us
        self.ds = ds

    #antar att self.us är sorterad stigande och att ds är sorterad för att passa us
    def plot(self):
        dx, dy = zip(*ds)
        plt.plot(dx, dy, 'r--')
        plt.plot(dx, dy, 'ro')

        ss = [self.call(u) for u in self.us]
        ssx, ssy = zip(*ss)
        plt.plot(ssx, ssy, 'b+')

        u_interval = np.linspace(us[0], us[-1], 100).tolist()
        s_interval = [self.call(u) for u in u_interval]
        s_interval_x, s_interval_y = zip(*s_interval)
        plt.plot(s_interval_x, s_interval_y, 'b-')

        plt.show()


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
        u_leftmost = self.us[k-1]
        u_rightmost = self.us[k+3-n]
        return ((u_rightmost-u)/(u_rightmost-u_leftmost))
        #return alpha
