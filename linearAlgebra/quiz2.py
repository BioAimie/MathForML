import numpy as np
import matplotlib.pyplot as pt

# create a normal distribution with some noise
mu = 15
sigma = 3
n = 100
signal = np.random.normal(mu, sigma, n)
noise = np.random.normal(mu, sigma, n)/mu
distribution = signal + noise

mbar = sum(distribution) / n
se = (1/n*sum((distribution - mbar) ** 2))**0.5

print(mbar, se)