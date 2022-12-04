from calendar import c
import numpy as np
import math
# from tabulate import tabulate
# import matplotlib.pyplot as plt
from itertools import product
import sys

print()

def my_bisection(f, a, b, tol):
    # approximates a root, R, of f bounded
    # by a and b to within tolerance
    # | f(m) | < tol with m the midpoint
    # between a and b Recursive implementation

    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    # get midpoint
    m = (a + b) / 2

    if np.abs(f(m)) < tol:
        # stopping condition, report m as root
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a.
        # Make recursive call with a = m
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b.
        # Make recursive call with b = m
        return my_bisection(f, a, m, tol)

def isReal(txt):
    try:
        float(txt)
        return True
    except ValueError:
        return False

def catenary_plot(h,s):
    if (isReal(h) & isReal(s)):
        h=float(h)
        s=float(s)
        f = lambda x: -(h+x)/x+math.cosh(s/(2*x))
        r01 = my_bisection(f, 0.1, 1000, 0.000001)
        span_div=np.linspace(-s/2, s/2, 100)
        a=-r01*np.cosh(span_div/(-r01))+r01
        a= a.tolist()
        b=span_div
        b= b.tolist()
        # c=list(product(b,a))
        c=list(zip(b, a))
        
        c=' '.join(map(str,(c)))
        c=c.replace(" ","")
        c=c.replace("(","")
        c=c.replace(")","\n")
        # c="\n".join(c)
        result=c
    else:
        result = "Please enter a valid number for Span & Rise"
    

    return result       