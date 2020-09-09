import matplotlib.pyplot as plt
import numpy as np
import scipy
class Spline:

    def __init__(self, us=None, ds=None, interpolation_points=None):
        """
        Init either takes us and ds, or it takes interpolation points that you want the curve to pass.
        :param us: Knot points. K + 1
        :param ds: Control points. K - 1
        :param interpolation_points: The points to pass.
        """
        self.interpolation_points = interpolation_points
        if us is not None and ds is not None:
            self.us = us
            self.ds = ds
        elif interpolation_points is not None:
            self.ds = self.get_control_points(interpolation_points)
        else:
            pass

    def get_control_points(self, interpolation_points):
        """
        :param interpolation_points: Points to pass through.
        :return: The control points that give the correct curve.
        """
        L = len(interpolation_points)-1
        us = np.linspace(0, 1, L+3)
        us[1] = us[2] = us[0]
        us[-3] = us[-2] = us[-1]
        self.us = us

        # Calc de Boor points, basis functions and with those compute vandermonde matrix.
        grevilles = [(self.us[i] + self.us[i+1] + self.us[i+2]) / 3 for i in range(L+1)]
        basis_func = [self.create_basis_func(j) for j in range(L+1)]
        vandermonde = np.array([[basis_func[col](grevilles[row]) for col in range(L+1)] for row in range(L+1)])

        xs, ys = zip(*interpolation_points)
        
        dxs = np.linalg.solve(vandermonde, xs)
        dys = np.linalg.solve(vandermonde, ys)
        ds = np.array(list(zip(dxs, dys)))

        return ds

    def plot(self, degree):
        """
        Plots blossoms of order degree.
        param degree: order of blossoms to plot
        """
        #only plot where spline is defined
        us_no_extra = self.us[2:-2]
        u_interval = np.linspace(us_no_extra[0], us_no_extra[-1], 1000).tolist()

        #plot control polygon
        dx, dy = zip(*self.ds)
        plt.plot(dx, dy, 'r--')
        plt.plot(dx, dy, 'ro')

        #plot interp points
        if self.interpolation_points is not None:
            interp_x, interp_y = zip(*self.interpolation_points)
            plt.plot(interp_x, interp_y, 'yo')

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
    
    def d(self, n, k, u):
        """
        recursive definition of blossoms, with alternative notation
        param: n = degree of blossom, n=0 gives a control point, n=3 gives s(u)
        param: k = index of leftmost knot point of this blossom
        param: u = parameter value to evaluate spline blossom at
        return: blossom value
        """

        if n == 0:
            return self.ds[k]
        elif n >= 1:
            return self.alpha(n, k, u) * self.d(n-1, k-1, u) + (1-self.alpha(n, k, u)) * self.d(n-1, k, u)

    #starts recursion to calculate s(u)
    def __call__(self, u):
        """
        starts recursion to calculate s(u)
        param u: parameter value to évaluate spline at
        return: value of spline at u, s(u)
        """

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
                if self.get_u_by_index(j - 1) <= u < self.get_u_by_index(j):
                    return 1
                # Bad solution to end point issue. Prevents singular vandermonde matrix. Otherwise last row
                # of matrix is empty, giving a singular matrix without solutions.
                elif self.get_u_by_index(j) == 1 and u == 1:
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
        Wrapper so that when you try to call for gridpoint outside of range, another gridpoint is returned.
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
