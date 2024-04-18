# D-FUSS: Discrete-FoUrier SerieS

An elementary Python package to compute discrete Fourier series.

# Introduction to Fourier Series

In mathematical analysis, Fourier series provide a way to represent periodic functions as a trigonometric polynomial. Given a periodic function $f(t)$ with period $T$, the Fourier series expansion is given by:

$$ f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos \left( \frac{2\pi nt}{T} \right) + b_n \sin \left( \frac{2\pi nt}{T} \right),$$

where the coefficients $a_0$, $a_n$, and $b_n$ are given by:

$$a_0 = \frac{1}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \ dt,$$

$$a_n = \frac{2}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \cos \left( \frac{2\pi nt}{T} \right) \ dt,$$

$$b_n = \frac{2}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}} f(t) \sin \left( \frac{2\pi nt}{T} \right) \ dt.$$
