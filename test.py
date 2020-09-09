from spline import Spline
from matplotlib.pyplot import *
import numpy as np


s = Spline(us=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], ds=[])

print(np.linspace(0.0, 1.0, 100))
print([s.create_basis_func(5)(x) for x in np.linspace(0.0, 1.0, 100)])
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    plot(np.array(np.linspace(0.0, 1.0, 100)), np.array([s.create_basis_func(i)(x) for x in np.linspace(0.0, 1.0, 100)]))


show()