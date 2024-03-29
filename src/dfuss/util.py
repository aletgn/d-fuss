import numpy as np
from math import pi
import matplotlib.pyplot as plt

def calc_a_0(f: np.ndarray) -> np.ndarray:
    """
    Calculate the coefficient a_0 for the Fourier series.

    Parameters
    ----------
    f : np.ndarray
        Input data array.

    Returns
    -------
    float
        Coefficient a_0 for the Fourier series.

    """
    return f.mean() 

def arg(k: int, n: np.ndarray, N: int) -> float:
    """
    Calculate the argument for Fourier coefficients.

    Parameters
    ----------
    k : int
        Index of the Fourier coefficient.
    n : np.ndarray
        Samples.
    N : int
        Total number of data points.

    Returns
    -------
    float
        Argument for the Fourier coefficient.

    """
    return (2*pi*k*n)/N

def calc_a_k(k: int, n: np.ndarray, N: int, f: np.ndarray) -> float:
    """
    Calculate the coefficient a_k for the Fourier series.

    Parameters
    ----------
    k : int
        Index of the Fourier coefficient.
    n : int
        Index of the data point.
    N : int
        Total number of data points.
    f : np.ndarray
        Input data array.

    Returns
    -------
    float
        Coefficient a_k for the Fourier series.

    """
    return (2/N)*np.inner(f, np.cos(arg(k, n, N)))

def calc_b_k(k: int, n: np.ndarray, N: int, f: np.ndarray) -> float:
    """
    Calculate the coefficient b_k for the Fourier series.

    Parameters
    ----------
    k : int
        Index of the Fourier coefficient.
    n : int
        Index of the data point.
    N : int
        Total number of data points.
    f : np.ndarray
        Input data array.

    Returns
    -------
    float
        Coefficient b_k for the Fourier series.

    """
    return (2/N)*np.inner(f, np.sin(arg(k, n, N)))

def inspect(x: np.ndarray, f: np.ndarray, F) -> None:
    """
    Plot the input data and its Fourier series.

    Parameters
    ----------
    x : np.ndarray
        Input data points.
    f : np.ndarray
        Input data array.
    F : object
        FourierSeries object representing the Fourier series.

    """
    plt.figure(dpi=300)
    plt.plot(x, f, label="Data")
    plt.plot(x, F.series(F.n), label="Series")
    plt.legend(loc="best")
    plt.show()
