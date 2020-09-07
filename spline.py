import matplotlib.pyplot as plt
import numpy as np

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
        From a given u find the hot index, meaning the surrounding u indexes.
        :param u: given u
        :return: indexes
        """


        return

    def alpha(self, u, n, k):
        return 
        #return alpha

print(111)
us = np.linspace(0,1,4)
ds = [(0,0), (1,0), (1,1), (0,1)]

larry = Spline(us, ds)
print(222)
larry.plot()
print(333)
