# Mixture fitting library

```pymixfit``` is a Python mixture fitting library. This library tries
to fit a variety of candidate functions to presented measurement data
to extract the different components that make up the sampled data
points. This may be used to identify different mechanisms that contribute
to formation of data.

This library is based on fitting capabilities of [lmfit](https://lmfit.github.io//lmfit-py/).

The whole idea of mixture fitting and fitting sums using least squares
is built on the ideas of

* [Fitting mixtures of statistical distributions](https://arvix.org/abs/1901.06708)
* [Bundle adjustment methods in engineering photogrammetry](https://doi.org/10.1111/j.1477-9730.1980.tb00020.x)

## Installation

```
pip install pymixfit-tspspi
```

## Currently implemented model functions

* Constant (```mixfitfunctions.constant.MixfitFunctionConstantFactory```)
   * $f(x) = \text{offset}$
* Linear (```mixfitfunctions.linear.MixfitFunctionLinearFactory```)
   * $f(x) = \text{slope} * x + \text{intercept}$
* Gaussian (```mixfitfunctions.gaussian.MixfitFunctionGaussianFactory```)
   * $f(x) = \text{amp} * \frac{1}{\sqrt{2 \pi}} e^{- \frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2} + \text{offset}$
* Differential Gaussian (```mixfitfunctions.differentialgaussian.MixfitFunctionDifferentialGaussian```)
* Cauchy / Lorentz (```mixfitfunctions.cauchy.MixfitFunctionCauchyFactory```)
* Differential Cauchy / Lorentz (```mixfitfunctions.cauchy.MixfitFunctionDifferentialCauchyFactory```)

By default all functions are used as candidate functions by the mixture fitter

## Usage

To use the mixture fitter simply instantiate the ```Mixfit``` class and
perform a ```fit``` function. It's a good idea to apply one of the abort
conditions, else the fitter only aborts when it reaches the point of no
further improvements. Possible abort conditions are:

* ```stopError``` is the improvement of the $\chi^2$. As soon as the
  fit quality of the fit goes below the threashold the process is aborted
* ```maxIterations``` limits the number of components that are fit

## Example

For more advanced examples take a look at the ```examples``` directory


