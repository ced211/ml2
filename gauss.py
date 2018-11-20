import math
import numpy as np

mean = np.array([[0,0],[0,0]])
cov = np.array([ [[1,0],[0,1]], [[2,0],[0,0.5]] ])
nb_classes = 2

x = np.array([2,3])

f = lambda x, k: ((2 * math.pi)**(nb_classes / 2) *
                               math.sqrt(np.linalg.det(cov[k])))**-1 * \
            np.exp(-0.5 * np.dot(np.dot((x - mean[k]),
                                        np.linalg.inv(cov[k])), (x - mean[k])))

print(f(x,0))
print(f(x,1))

g = lambda x, k, p: (np.sqrt(math.pi)*cov[k][p][p])**-1 * np.exp(-0.5 * np.square((x[p]- mean[k][p])/cov[k][p][p]))

print(g(x,0,0))
print(g(x,0,1))
print( g(x,0,0)*g(x,0,1) )
print( g(x,1,0)*g(x,1,1) )

print(cov[0]**-2)
print(cov[1]**-2)

print(np.linalg.inv(cov[0]))