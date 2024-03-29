from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.expanduser("~"), '/home/ale/Desktop/d-fuss/src/'))

import numpy as np
from math import pi

from dfuss.fourier import DiscreteFourierSeries as DFS
from dfuss.util import inspect

def shifted_spike():
    npts = 1000
    order = 10
    x = np.linspace(0,2*pi,npts)
    f = []
    phi = pi/2
    ra  = pi/4 
    for k in x:
        if abs(k-phi) < ra: 
            f.append(-1000*(k-(phi-ra))*(k-(phi+ra)))
        else:
            f.append(0)
    f = np.array(f)

    F = DFS(M=order)
    F.coefficients(x, f)
    print(F)

    inspect(x, f, F)
    
if __name__ == "__main__":
    shifted_spike()