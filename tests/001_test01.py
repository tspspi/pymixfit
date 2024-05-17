import matplotlib.pyplot as plt
import numpy as np

from mixfit.mixfit import Mixfit

from mixfitfunctions.mixfitfunction import MixfitFunctionFactory
from mixfitfunctions.gaussian import MixfitFunctionGaussianFactory
from mixfitfunctions.constant import MixfitFunctionConstantFactory
from mixfitfunctions.linear import MixfitFunctionLinearFactory
from mixfitfunctions.differentialgaussian import MixfitFunctionDifferentialGaussianFactory
from mixfitfunctions.cauchy import MixfitFunctionCauchyFactory
from mixfitfunctions.differentialcauchy import MixfitFunctionDifferentialCauchyFactory

if __name__ == "__main__":
    dc = MixfitFunctionCauchyFactory()
    ddc = MixfitFunctionDifferentialCauchyFactory()
    dc = dc()
    ddc = ddc()

    #fig, ax = plt.subplots()
    #x = np.linspace(-10, 10, 1000)
    #ax.plot(x, dc({"x0" : 3, "gamma" : 5, "offset" : 0, "amp" : 2}, x))
    #ax.plot(x, ddc({"x0" : 3, "gamma" : 5, "offset" : 0, "amp" : 10}, x))
    #ax.grid()
    #plt.show()
    #sys.exit(0)
        
    dgf = MixfitFunctionDifferentialGaussianFactory()
    dg = dgf()
           
    x = np.linspace(-10, 10, 100)
    testsigma = 3
    testmu = 1
    testoffset = 0.5

    testsigma2 = 0.7
    testmu2 = -3
    testamp2 = 0.3
    testoffset2 = 0

    testsigma3 = 0.1
    testmu3 = 6
    testamp3 = -0.1
    testoffset3 = 0

    testdta = np.exp(-0.5 * ((x - testmu)/(testsigma))**2.0) * 1.0 / np.sqrt(2 * np.pi * testsigma) - testoffset
    testdta = testdta + testamp2 * np.exp(-0.5 * ((x - testmu2)/(testsigma2))**2.0) * 1.0 / np.sqrt(2 * np.pi * testsigma2) + testoffset
    testdta = testdta + testamp3 * np.exp(-0.5 * ((x - testmu3)/(testsigma3))**2.0) * 1.0 / np.sqrt(2 * np.pi * testsigma3) + testoffset
    testdta = testdta + x * 0.001
    testdta = testdta + dg({ "mu" : 2, "sigma" : 0.22, "amp" : 0.05, "offset" : 0 }, x)
    testdta = testdta + np.random.normal(0, 0.015, testdta.shape)
    testdta = testdta + np.full((len(x),),5.5)

    mf = Mixfit(
#        maxIterations = 10,
        stopError = 0.05
#        allowed = [
#           MixfitFunctionGaussianFactory(limits = {"mu" : (-10, 10), "sigma" : (0.5, 3)}),
#           MixfitFunctionDifferentialGaussianFactory(limits = { "sigma" : (0.01, 1) }),
#           MixfitFunctionLinearFactory(),
#           MixfitFunctionCauchyFactory()
#        ]
    )
    res = mf.fit(x, testdta)

    fig, ax = plt.subplots(1,2,figsize=(6.4*4, 4.8*2))
    ax[0].plot(x, testdta, 'x')
    ax[0].plot(x, res(x))
    ax[0].grid()
    ax[1].plot(res._chis)
    ax[1].grid()
    plt.show()

