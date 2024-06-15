# D-FUSS: Discrete-FoUrier SerieS

An elementary Python package to compute discrete Fourier series.

# Introduction to Fourier Series

In mathematical analysis, Fourier series (FS) provide a way to represent periodic functions as a trigonometric polynomial. Given a periodic function $f(t)$ with period $T$, the Fourier series expansion is given by:

$$ f(t) = \frac{a_0}{2} + \sum_{k=1}^{\infty} a_k \cos \left( \frac{2\pi kt}{T} \right) + b_k \sin \left( \frac{2\pi kt}{T} \right),$$

where the coefficients $a_0$, $a_n$, and $b_n$ are given by:

$$a_0 = \frac{1}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \ dt,$$

$$a_k = \frac{2}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \cos \left( \frac{2\pi kt}{T} \right) \ dt,$$

$$b_k = \frac{2}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \sin \left( \frac{2\pi kt}{T} \right) \ dt.$$

# Discretisation

In order for (FS) to be numerically computable we need to truncate the series to a finite order, say $M$. Hence:

$$f(t) = a_0 +\sum_{k = 1}^{M}a_k\cos\left({\frac{2\pi k}{T}t}\right) + b_k\sin\left({\frac{2\pi k}{T}t}\right).$$

Assume that we wish to perform FS on a given signal. Accordingly we acquired $N$ samples $n=1,2,\dots,N$ at sampling period a $T_s$, so $ t= n T_s$. The period of the signal is, therefore, given by $T = N T_s$. Consequently, the prior relationship becomes:

$$f(t=nT_s) = f(n) = a_0 +\sum_{k = 1}^{M}a_k\cos\left({\frac{2\pi k}{N}n}\right) + b_k\sin\left({\frac{2\pi k}{N}n}\right),$$

which is the discrete Fourier series (DFS). The coefficients are discretised as well in a similar fashion:

$$ a_0 = \frac{1}{N} \sum_{n = 1}^{N} f(n),$$

$$a_k = \frac{2}{N}\sum_{n = 1}^{N} f(n) \cos\left({\frac{2\pi k}{N}n}\right)\quad \forall\, k=1,2,\dots,M,$$

$$b_k = \frac{2}{N}\sum_{n = 1}^{N} f(n) \sin\left({\frac{2\pi k}{N}n}\right)\quad \forall\, k=1,2,\dots,M.$$

The last four relationships are implemented in D-FUSS.
