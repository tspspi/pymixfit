import sys
import numpy as np
import matplotlib.pyplot as plt

from mixfit.mixfit import Mixfit

data = np.load(sys.argv[1])

# Just a way to get the sample data
# This data includes different runs capturing
# in-phase and quadrature channels during
# frequency sweeps. The x axis is the frequencies,
# the fitted data is the mean of all runs
x = data["f_RF"]
I = data["sigI"].mean(1)

# Now create the mixture fitter for _all_
# models
mf = Mixfit(
	maxIterations = 4,
	stopError = 0.05
)

# And execute
resI = mf.fit(x, I)

# Dump
print(resI)

# Plot
fig, ax = plt.subplots(1, 2, figsize=(6.4*2, 4.8))
ax[0].plot(x*2, I) # We plot raw data
ax[0].plot(x*2, resI(x)) # and our fit result
ax[0].grid()

ax[1].plot(resI._chis)
ax[1].grid()

plt.show()
