import matplotlib.pyplot as plt
import numpy as np

class Spline:
    
    #ds assumed to be list of ndarrays
    def __init__(self, us, ds):
        self.us = us
        self.ds = ds

    #antar att self.us är sorterad stigande och att ds är sorterad för att passa us
    def plot(self):
        us_no_extra = self.us[2:-3]

        dx, dy = zip(*self.ds)
        plt.plot(dx, dy, 'r--')
        plt.plot(dx, dy, 'ro')

        ss = [self(u) for u in us_no_extra]
        ssx, ssy = zip(*ss)
        plt.plot(ssx, ssy, 'b+')

        u_interval = np.linspace(us_no_extra[0], us_no_extra[-1], 100).tolist()
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
                if self.get_u_by_index(j - 1) <= u < self.get_u_by_index(j):
                    return 1
                else:
                    return 0
            return basis
        else:
            def basis(u):
                # calculate basis function with recursive algorithm until we reach layer 0.
                # Expression 1 in the recursive algorithm:
                first_quota = 0 if (self.get_u_by_index(j + layer - 1) - self.get_u_by_index(j - 1)) == 0 else (u - self.get_u_by_index(j - 1)) / (self.get_u_by_index(j + layer - 1) - self.get_u_by_index(j - 1))
                b_func1 = self.create_basis_func(j, layer - 1)

                # Expression 2 in the recursive algorithm:
                second_quota = 0 if (self.get_u_by_index(j + layer) - self.get_u_by_index(j)) == 0 else (self.get_u_by_index(j + layer) - u) / (self.get_u_by_index(j + layer) - self.get_u_by_index(j))
                b_func2 = self.create_basis_func(j + 1, layer - 1)
                return first_quota * b_func1(u) + second_quota * b_func2(u)
            return basis

    def get_u_by_index(self, j):
        """
        Wrapper so that when you try to call for u outside of range, another is returned.
        :param j: The index of the u wanted.
        :return: gridpoint
        """
        if j < 0:
            return self.us[0]
        elif j > len(self.us) - 1:
            return self.us[len(self.us) - 1]
        else:
            return self.us[j]


    def spline_basis_representation(self, u):
        """
        Used to calculate the spline value using a linear combination of the basis functions along with the
        control points.
        :param u: The point in which to evaluate the value of the spline.
        :return: The spline value, s(u).
        """
        # su is our output vector, s(u).
        su = np.array([0, 0])

        for j, d in enumerate(self.ds):
            # for each d, add a sum of d * N_j (u) to the su array.
            basis_func = self.create_basis_func(j)

            su = su + d * basis_func(u)

        return su
