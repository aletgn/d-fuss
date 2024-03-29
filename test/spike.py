from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.expanduser("~"), '/home/ale/Desktop/d-fuss/src/'))

import numpy as np
from math import pi

from dfuss.fourier import DiscreteFourierSeries as DFS
from dfuss.util import inspect

def spike():
    npts = 1000
    order = 4
    x = np.linspace(-pi,pi,npts)
    f = []
    ra = pi/4
    for k in x:
        if abs(k) < ra:
            f.append(-1000*(k)**2+1000*ra**2) 
            #y.append(1) #for square wave
        else:
            f.append(0)
    f = np.array(f)

    F = DFS(M=order)
    F.coefficients(x, f)
    print(F)

    inspect(x, f, F)

if __name__ == "__main__":
    spike()