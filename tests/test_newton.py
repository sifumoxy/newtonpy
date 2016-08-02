import unittest

from numpy import sin, cos, abs

from newtonpy.newtonpy import newton


class NewtonTest(unittest.TestCase):
    def test_sin(self):
        result = newton(sin, cos, 0.5)
        assert(abs(sin(result)) < 1e-8)
        assert(abs(result) < 1e-8)

    def test_polynomial(self):
        def fun(x):
            return x**2 - 1
        result = newton(fun, lambda x: 2 * x, 2.)
        assert(abs(fun(result)) < 1e-8)
        assert(abs(1 - result) < 1e-8)
