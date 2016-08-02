from numpy.linalg import norm


def newton(f, Df, x0):
    tol = 1e-8
    x = x0
    while norm(f(x)) > tol:
        x = x - f(x)/Df(x)
    return x
