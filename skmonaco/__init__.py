
"""
=======================
Monte Carlo integration
=======================

This module provides a toolkit for Monte Carlo integration.

    mcquad   -- Integration over a uniformly-sampled hypercube.
    mcimport -- Integration over points distributed according to a particular pdf.
    mcmiser  -- Integration over a hypercube using MISER algorithm.
    integrate_from_points -- Integration of a function over specific points.
"""

__version__ = "0.3.1"

try:
    __SKMONACO_SETUP__
except NameError:
    # skmonaco is not being run from the setup script.
    __SKMONACO_SETUP__ = False

if not __SKMONACO_SETUP__ :
    from .uniform import mcquad
    from .importance import mcimport
    from .from_pts import integrate_from_points
    from .miser import mcmiser

    try:
        from numpy.testing import Tester
        test = Tester().test
        bench = Tester().bench
    except ImportError:
        # numpy is too recent, the Tester class is no longer available, see #17
        # https://github.com/scikit-monaco/scikit-monaco/issues/17
        def test():
            raise ImportError("numpy.testing.Tester could not get imported. Cannot run tests.")
        def bench():
            raise ImportError("numpy.testing.Tester could not get imported. Cannot run benchmarks.")
