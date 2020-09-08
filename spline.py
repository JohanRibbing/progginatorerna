import matplotlib.pyplot as plt
import numpy as np

class Spline:
    
    #ds assumed to be list of ndarrays
    def __init__(self, us, ds):
        self.us = us
        self.ds = ds

    #antar att self.us är sorterad stigande och att ds är sorterad för att passa us
    def plot(self):
        print("us: ", self.us)


        us_no_extra = self.us[2:-2]
        print("us_no_extra: ", us_no_extra)


        u_interval = np.linspace(us_no_extra[0], us_no_extra[-1], 100).tolist()
        print("u_interval: ", u_interval)


        dx, dy = zip(*self.ds)
        plt.plot(dx, dy, 'r--')
        plt.plot(dx, dy, 'ro')

        ss = [self(u) for u in us_no_extra]
        ssx, ssy = zip(*ss)
        plt.plot(ssx, ssy, 'b+')

        s_interval = [self(u) for u in u_interval]
        s_interval_x, s_interval_y = zip(*s_interval)
        plt.plot(s_interval_x, s_interval_y, 'b-')

        plt.show()
    
    def d(self, n, k, u):
        if n == 0:
            return self.ds[k]
        elif n >= 1:
            return self.alpha(n, k, u) * self.d(n-1, k-1, u) + (1-self.alpha(n, k, u)) * self.d(n-1, k, u)

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
        return len(self.us) - 3

    def alpha(self, n, k, u):
        u_leftmost = self.us[k-1]
        u_rightmost = self.us[k+3-n]
        return ((u_rightmost-u)/(u_rightmost-u_leftmost))
        #return alpha

    def create_basis_func(self, j, layer=3):
        """
        Creates basis function with index j.
        :param j:
        :param layer: number of layers left of the recursive algorithm.
        :return: Python function representing the basis function.
        """
        if layer == 0:
            def basis(u):
                if self.us[j - 1] <= u < self.us[j]:
                    return 1
                else:
                    return 0
            return basis
        else:
            def basis(u):
                # calculate basis function with recursive algorithm until we reach layer 0.
                # Expression 1 in the recursive algorithm:
                first_quota = (u - self.us[j - 1]) / (self.us[j + layer - 1] - self.us[j - 1])
                b_func1 = self.create_basis_func(j, layer - 1)

                # Expression 2 in the recursive algorithm:
                second_quota = (self.us[j + layer] - u) / (self.us[j + layer] - self.us[j])
                b_func2 = self.create_basis_func(j + 1, layer - 1)
                return first_quota * b_func1(u) + second_quota * b_func2(u)
            return basis
