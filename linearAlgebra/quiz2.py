import numpy as np
import matplotlib.pyplot as pt

# create a normal distribution with some noise
mu = 15
sigma = 3
signal = np.random.normal(mu, sigma, 100)
noise = np.random.normal(mu, sigma, 100)/mu
distribution = signal + noise

# create a model that will approximate the actual distribution by minimizing SSR (sum of squared residuals)
ssr = 1
error = 0.0002
mbar = 13
se = 1

# visualize an overlay of the estimate on the actual distribution
# pt.hist(distribution, bins='auto', alpha=0.5, label='actual')
# pt.hist(estimate, bins='auto', alpha=0.5, label='estimate')
# pt.show()

# need to alter mbar and se to lower ssr below the acceptable error level
# initialize the guess somewhere and get the initial SSR
estimate = np.random.normal(mbar, se, 100)
ssr = sum(abs(distribution - estimate) ** 2)

# set up some increments by which to alter the parameters of the estimate
mean_move = 0.01
se_move = 0.001

# while SSR is greater than the allowable error, iterate by changing the parameters
while ssr > error:

    # first try adding the increments
    mbar += mean_move
    se += se_move
    estimate_new = np.random.normal(mbar, se, 100)
    ssr_new = sum(abs(distribution - estimate) ** 2)

    # if the new ssr is better than the last SSR, then leave the increments the same, otherwise, try new
    if ssr_new > ssr:

        # how do I decide which direction to move in for mbar and se (which gradient to descend)?
        mean_move = -0.015
        se_move = -0.0005






