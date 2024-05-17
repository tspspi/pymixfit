import sys

import numpy as np
import matplotlib.pyplot as plt

from mixfit.mixfit import Mixfit

from mixfitfunctions.mixfitfunction import MixfitFunctionFactory
from mixfitfunctions.gaussian import MixfitFunctionGaussianFactory
from mixfitfunctions.constant import MixfitFunctionConstantFactory
from mixfitfunctions.linear import MixfitFunctionLinearFactory
from mixfitfunctions.differentialgaussian import MixfitFunctionDifferentialGaussianFactory
from mixfitfunctions.cauchy import MixfitFunctionCauchyFactory
from mixfitfunctions.differentialcauchy import MixfitFunctionDifferentialCauchyFactory

def printUsage():
    print("Usage:\n")
    print("\t{sys.argv[0]} datafile")
    print("\nPerform mixture fit on supplied EPR current or frequency scan")

if len(sys.argv) < 2:
    printUsage()
    sys.exit(1)

data = np.load(sys.argv[1])


x = data["f_RF"]
I = data["sigI"].mean(1)
Q = data["sigQ"].mean(1)

mf = Mixfit(
    maxIterations = 4,
    stopError = 0.05,
    allowed = [
        MixfitFunctionGaussianFactory(limits = { "sigma" : (3, 20) }),
        MixfitFunctionDifferentialCauchyFactory(limits = { "gamma" : (0.5, 2) })
    ]
)
resI = mf.fit(x, I)
resQ = mf.fit(x, Q)

ycount = np.max((len(resI._functions), len(resQ._functions)))

fig, ax = plt.subplots(ycount+1, 2, figsize=(6.4*2, 4.8*(ycount+1)))
ax[0][0].plot(x*2, I)
ax[0][0].plot(x*2, resI(x))
ax[0][0].grid()

ax[0][1].plot(x*2, Q)
ax[0][1].plot(x*2, resQ(Q))
ax[0][1].grid()

for i in range(ycount):
    if i < len(resI._functions):
        ax[i+1][0].plot(x*2, resI._functions[i](resI._params[i], x))
        ax[i+1][0].grid()
    if i < len(resQ._functions):
        ax[i+1][1].plot(x*2, resQ._functions[i](resQ._params[i], x))
        ax[i+1][1].grid()

plt.show()
    
