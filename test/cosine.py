from sys import path as syspath
from os import path as ospath
syspath.append(ospath.join(ospath.expanduser("~"), '/home/ale/Desktop/d-fuss/src/'))

import numpy as np
from math import pi

from dfuss.fourier import DiscreteFourierSeries as DFS
from dfuss.util import inspect

def cosine():
    x = np.linspace(0,2*pi,1000)
    f = 50*np.cos(x)-20
    
    F = DFS(M=1)
    F.coefficients(x, f)
    print(F)

    inspect(x, f, F)

if __name__ == "__main__":
    cosine()