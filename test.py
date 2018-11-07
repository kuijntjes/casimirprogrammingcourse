print ("Hello world! Blup")

import numpy as np 
import matplotlib.pyplot as plt

n_samples = int(1E4)
sigma = 10
mu = 3

r = np.random.normal(loc=mu, scale=sigma, size=n_samples)

circumference = 2 * np.pi * r
plt.hist(circumference, bins=100)

