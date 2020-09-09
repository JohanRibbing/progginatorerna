import matplotlib.pyplot as plt
import numpy as np

class Spline:
    
    #ds assumed to be list of ndarrays
    def __init__(self, us, ds):
        self.us = us
        self.ds = ds

    #antar att self.us är sorterad stigande och att ds är sorterad för att passa us
    def plot(self, degree):

        #only plot where spline is defined
        us_no_extra = self.us[2:-2]
        u_interval = np.linspace(us_no_extra[0], us_no_extra[-1], 1000).tolist()

        #plot control polygon
        dx, dy = zip(*self.ds)
        plt.plot(dx, dy, 'r--')
        plt.plot(dx, dy, 'ro')

        #plot knot points
        ss = [self(u) for u in us_no_extra]
        ssx, ssy = zip(*ss)
        plt.plot(ssx, ssy, 'b+')
        
        #plot spline between knots
        s_interval = [self(u) for u in u_interval]
        s_interval_x, s_interval_y = zip(*s_interval)

        #create lower orders of blossoms
        subsplines = [self.sub_call(u) for u in u_interval]

        #unpack list of n 3-tuples of 2-tuples into 6 n-tuples to match with plt.plot()
        s0, s1, s2 = zip(*subsplines)
        s0x, s0y = zip(*s0)
        s1x, s1y = zip(*s1)
        s2x, s2y = zip(*s2)

        #plot blossoms of correct degree, degree 3 = s(u)
        if degree == 0:
            plt.plot(s0x, s0y, 'g+')
        elif degree == 1:
            plt.plot(s1x, s1y, 'y-')
        elif degree == 2:
            plt.plot(s2x, s2y, 'c-')
        elif degree >= 3:
            plt.plot(s_interval_x, s_interval_y, 'b-')

        plt.show()
    
    #recursive definition of blossoms, with alternative notation
    #n = degree of blossom, n=0 gives a control point, n=3 gives s(u)
    #k = index of leftmost knot point of this blossom
    #u = parameter value to evaluate spline blossom at
    def d(self, n, k, u):
        if n == 0:
            return self.ds[k]
        elif n >= 1:
            return self.alpha(n, k, u) * self.d(n-1, k-1, u) + (1-self.alpha(n, k, u)) * self.d(n-1, k, u)
    #starts recursion to calculate s(u)
    def __call__(self, u):
        index = self.hot_index(u)
        return self.d(3, index, u)
    
    def sub_call(self, u):
        index = self.hot_index(u)
        return (self.d(0, index-2, u), self.d(1, index-1, u), self.d(2, index, u))

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

    #Returns the value of alpha for a given
    def alpha(self, n, k, u):
        """
        :param n: distance from bottom layer in Blossom
        :param k: index for Knot point
        :param u: position in spline
        :return: value of alpha for a given layer and position in recursive Blossom algorithm
        """
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
