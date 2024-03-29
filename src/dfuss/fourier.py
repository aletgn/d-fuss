import numpy as np
from matplotlib import pyplot as plt
from math import pi

from dfuss.util import calc_a_0, calc_a_k, calc_b_k, arg

class DiscreteFourierSeries():
    """
    Class for computing and representing the discrete Fourier series.

    Parameters
    ----------
    M : int, optional
        Truncation order (default is 1).

    Attributes
    ----------
    M : int
        Truncation order.
    N : np.ndarray
        Number of samples.
    a_0 : float
        Coefficient a_0 for the Fourier series.
    a_k : np.ndarray
        Coefficients a_k for the Fourier series.
    b_k : np.ndarray
        Coefficients b_k for the Fourier series.
    x : np.ndarray
        Input data points.
    f : np.ndarray
        Input data array.
    n : np.ndarray
        Array of sample indices.
    
    """
    def __init__(self, M: int = 1) -> None:
        """
        Initialize the DiscreteFourierSeries object.

        Parameters
        ----------
        M : int, optional
            Truncation order (default is 1).

        Returns
        -------
        None

        """
        self.M = M
        self.N = None
        self.n = None
        self.a_0 = None
        self.a_k = [None]
        self.b_k = [None]
        self.x = None
        self.f = None
    
    def coefficients(self, x: np.ndarray, f: np.ndarray) -> None:
        """
        Compute the coefficients of the Fourier series.

        Parameters
        ----------
        x : np.ndarray
            Input data points.
        f : np.ndarray
            Input data array.
        
        Returns
        -------
        None

        """
        self.N = x.shape[0]
        self.n = np.array(range(0, self.N))
        
        self.a_0 = calc_a_0(f)
        self.a = np.array([calc_a_k(k, self.n, self.N, f) for k in range(1, self.M+1)])
        self.b = np.array([calc_b_k(k, self.n, self.N, f) for k in range(1, self.M+1)])

    def series(self, n: np.ndarray) -> np.ndarray:
        """
        Compute the Fourier series.

        Parameters
        ----------
        n : np.ndarray
            Array of sample indices.

        Returns
        -------
        np.ndarray
            Fourier series values corresponding to the input sample indices.

        """
        return self.a_0 +\
            np.array([self.a[k]*np.cos(arg(k+1, n, self.N)) for k in range(0, self.M)]).sum(axis=0) +\
                  np.array([self.b[k]*np.sin(arg(k+1, n, self.N)) for k in range(0, self.M)]).sum(axis=0)
    
    def __repr__(self) -> str:
        ord = f"order = {self.M}\n"
        samples = f"samples = {self.N}\n"
        s_a_0 = f"a_0 = {self.a_0}\n"
        s_a = f"a = {self.a}\n"
        s_b = f"b = {self.b}\n"
        return ord+samples+s_a_0 + s_a + s_b
