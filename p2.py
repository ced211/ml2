from scipy.integrate import quad, dblquad
import matplotlib.pyplot as plt
import numpy as np
from math import exp, sqrt,pi
from matplotlib.colors import ListedColormap

def gaussian1 (x0,x1):
    sigma_n = 1
    sigma_p0 = 2 
    sigma_p1 = 0.5

    a = exp(-0.5*(x0**2 + x1**2)/sigma_n**2) / (2 * pi * sigma_n**2) 
    b = exp(-0.5*(x0**2 / (sigma_p0**2) + x1**2 / (sigma_p1**2)))  / (2 * pi * sqrt(sigma_p0**2 * sigma_p1**2))
    return min(a,b)/2

def classifier (x0,x1,sigma_n= np.matrix('1 0; 0 1'),mu_n = np.matrix('0 0'),sigma_p = np.matrix('2 0; 0 0.5') ,mu_p = np.matrix('0 0')):

    sigma_n0 = sigma_n[0,0]
    sigma_n1 = sigma_n[1,1]
    mu_n0 = mu_n[0,0]
    mu_n1 = mu_n[0,1]

    sigma_p0 = sigma_p[0,0]
    sigma_p1 = sigma_p[1,1]
    mu_p0 = mu_p[0,0]
    mu_p1 = mu_p[0,1]

    n = exp(-0.5*((x0-mu_n0)**2 / sigma_n0**2 + (x1-mu_n1)**2 /sigma_n1**2)) / (2 * pi * sqrt(sigma_n0**2 * sigma_n1**2))
    p = exp(-0.5*((x0-mu_p0)**2 / sigma_p0**2 + (x1-mu_p1)**2 /sigma_p1**2)) / (2 * pi * sqrt(sigma_p0**2 * sigma_p1**2))
    return n-p

def draw_boundary(fname,sigma_n= np.matrix('1 0; 0 1'),mu_n = np.matrix('0 0'),sigma_p = np.matrix('2 0; 0 0.5') ,mu_p = np.matrix('0 0')):
   #show boundary decision:
    step = 0.1
    max_value = 6
    nb_case = max_value * int(1/step)
    Z = np.zeros(shape=(2*nb_case,2* nb_case))
    xx = np.arange(2*nb_case)
    yy = np.arange(2*nb_case)
    for x in xx:
        for y in yy:
            Z[y,x] = classifier((x-nb_case)*step,(y-nb_case)*step,sigma_n,mu_n,sigma_p,mu_p)

    plt.contourf(xx,yy,Z)
    # Plot the decision boundary.
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    plt.figure()
    plt.title("Decision boundary gaussian")
    plt.xlabel("X_0")
    plt.ylabel("X_1")

    # Put the result into a color plot
    plt.contourf(xx, yy, Z, cmap=cm, alpha=.8)
    plt.savefig("%s.pdf" % fname)
    plt.close()


def residual_error (x0,x1,sigma_n= np.matrix('1 0; 0 1'),mu_n = np.matrix('0 0'),sigma_p = np.matrix('2 0; 0 0.5') ,mu_p = np.matrix('0 0')):
    sigma_n0 = sigma_n[0,0]
    sigma_n1 = sigma_n[1,1]
    mu_n0 = mu_n[0,0]
    mu_n1 = mu_n[0,1]

    sigma_p0 = sigma_p[0,0]
    sigma_p1 = sigma_p[1,1]
    mu_p0 = mu_p[0,0]
    mu_p1 = mu_p[0,1]

    n = exp(-0.5*((x0-mu_n0)**2 / sigma_n0**2 + (x1-mu_n1)**2 /sigma_n1**2)) / (2 * pi * sqrt(sigma_n0**2 * sigma_n1**2))
    p = exp(-0.5*((x0-mu_p0)**2 / sigma_p0**2 + (x1-mu_p1)**2 /sigma_p1**2)) / (2 * pi * sqrt(sigma_p0**2 * sigma_p1**2))
    return min(n,p)/2    

if __name__ == "__main__":

    #compute error rate
    area = dblquad(gaussian1, -np.inf, np.inf, lambda x: - np.inf, lambda x: np.inf)
    print("error rate is: " + str(area))
    mu = np.matrix('0 0')
    for x in range(0,3,1):
        for y in range(0,3,1):
            mu[0,0] = x
            mu[0,1] = y
            fname = str(x) + str(y) + "mu_p2"
            draw_boundary(fname,mu_p = mu)

    sigmaP = np.matrix('0 0; 0 0')
    for x in np.arange(0,2,0.25):
        for y in np.arange(0,2,0.25):
            sigmaP[0,0] = x
            sigmaP[1,1] = y
            fname = str(x) + str(y) + "sigma_p2"
            draw_boundary(fname,sigma_p = sigmaP)
