import matplotlib.pyplot as plt
import numpy as np

class Spline:
    
    #ds assumed to be list of ndarrays
    def __init__(self, us, ds):
        self.us = us
        self.ds = ds

    #antar att self.us är sorterad stigande och att ds är sorterad för att passa us
    def plot(self):
        dx, dy = zip(*self.ds)
        plt.plot(dx, dy, 'r--')
        plt.plot(dx, dy, 'ro')

        ss = [self(u) for u in self.us]
        ssx, ssy = zip(*ss)
        plt.plot(ssx, ssy, 'b+')

        u_interval = np.linspace(self.us[0], self.us[-1], 100).tolist()
        s_interval = [self(u) for u in u_interval]
        s_interval_x, s_interval_y = zip(*s_interval)
        plt.plot(s_interval_x, s_interval_y, 'b-')

        plt.show()
    
    def d(self, n, k, u):
        if n == 0:
            return self.ds[k]
        elif n >= 1:
            return self.alpha(n, k, u) * self.d(n-1, k-1, u) + (1-self.alpha(n, k, u)) * self.d(n-1, k, u)

    #need to figure out endpoints, multiplicity and index out of bounds
    def __call__(self, u):
        index = self.hot_index(u)
        return self.d(3, index, u)

    def hot_index(self, u):
        """
        From a given u find the hot index.
        :param u: given u
        :return: index
        """
        for i, gp in enumerate(self.us):
            if gp > u:
                return i

    def alpha(self, n, k, u):
        u_leftmost = self.us[k-1]
        u_rightmost = self.us[k+3-n]
        return ((u_rightmost-u)/(u_rightmost-u_leftmost))









us = np.linspace(0,1,8)
ds = [[0,0], [0,0], [0,0], [1,0], [1,1], [0,1], [0,1], [0,1]]
ds = [np.array(d) for d in ds]
larry = Spline(us, ds)
larry.plot()




