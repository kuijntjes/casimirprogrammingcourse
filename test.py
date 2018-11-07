print ("Hello world! Blup")

import numpy as np
import matplotlib as plt

r = np.random.random_sample((60))
circumference = 2 * np.pi * r


plt.hist(circumference, bins=20)


