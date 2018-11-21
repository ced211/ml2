from scipy.integrate import quad, dblquad
import numpy as np
from math import exp, sqrt,pi

def gaussian1 (x0,x1):
    sigma_n = 1
    sigma_p0 = 2 
    sigma_p1 = 0.5

    a = exp(-0.5*(x0**2 + x1**2)/sigma_n**2) / (2 * pi * sigma_n**2) 
    b = exp(-0.5*(x0**2 / (sigma_p0**2) + x1**2 / (sigma_p1**2)))  / (2 * pi * sqrt(sigma_p0**2 * sigma_p1**2))
    return min(a,b)/2

def gaussian2 (x0,x1):
    sigma_n = 1
    sigma_p0 = 2 
    sigma_p1 = 0.5
    u0 = 5
    u1 = 5

    a = exp(-0.5*((x0-u0)**2 + (x1-u1)**2)/sigma_n**2) / (2 * pi * sigma_n**2) 
    b = exp(-0.5*(x0**2 / (sigma_p0**2) + x1**2 / (sigma_p1**2)))  / (2 * pi * sqrt(sigma_p0**2 * sigma_p1**2))
    return max(a,b)/2

def gaussian3 (x0,x1):
    sigma_n = 1
    sigma_p0 = 5 
    sigma_p1 = 10

    a = exp(-0.5*(x0**2 + x1**2)/sigma_n**2) / (2 * pi * sigma_n**2) 
    b = exp(-0.5*(x0**2 / (sigma_p0**2) + x1**2 / (sigma_p1**2)))  / (2 * pi * sqrt(sigma_p0**2 * sigma_p1**2))
    return max(a,b)/2    

def gaussian4 (x0,x1):
    sigma_n = 1
    sigma_p0 = 0.1 
    sigma_p1 = 0.2

    a = exp(-0.5*(x0**2 + x1**2)/sigma_n**2) / (2 * pi * sigma_n**2) 
    b = exp(-0.5*(x0**2 / (sigma_p0**2) + x1**2 / (sigma_p1**2)))  / (2 * pi * sigma_p0 * sigma_p1)
    return max(a,b)/2  


if __name__ == "__main__":

    area = dblquad(gaussian1, -np.inf, np.inf, lambda x: - np.inf, lambda x: np.inf)
    print(area)