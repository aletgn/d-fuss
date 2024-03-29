from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.expanduser("~"), '/home/ale/Desktop/d-fuss/src/'))

import numpy as np
from math import pi

from dfuss.fourier import DiscreteFourierSeries as DFS
from dfuss.util import inspect

def smooth_square():
    npts = 1000
    order = 4
    x = np.linspace(-pi,pi,npts)
    f = []
    ra = pi/4
    for k in x:
        if abs(k) < ra:
            f.append(-100*k**2+100*ra**2) 
        else:
            f.append(0)

    f = np.array(f)
    F = DFS(M=4)
    F.coefficients(x, f)
    print(F)

    inspect(x, f, F)

if __name__ == "__main__":
    smooth_square()