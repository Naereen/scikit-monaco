# This example shows how to use the mcquad function to perform
# Monte Carlo integration in Python.
# It integrates the function sqrt(x^2 + y^2 + z^2) over the unit cube
# [0,1]^3 using 1 million points.
# The result of the integration and the estimated error are printed to the console.
# The function mcquad is imported from the skmonaco module.
# The function mcquad takes a function to integrate, the number of points
# to use for the integration, and the lower and upper bounds of the
# integration region as arguments. It returns the result of the
# integration and an estimate of the error.
# The function to integrate is defined as a lambda function that takes
# a list of points as input and returns the value of the function
# at those points. The lower and upper bounds of the integration region
# are defined as lists of the lower and upper bounds for each dimension.
# The result of the integration is printed to the console, along with
# the estimated error.

from skmonaco import mcquad
from math import sqrt
result, error = mcquad(
    lambda xs: sqrt(xs[0]**2 + xs[1]**2 + xs[2]**2),
    npoints=1e6, xl=[0.,0.,0.], xu=[1.,1.,1.]
)

print("{} +/- {}".format(result, error))