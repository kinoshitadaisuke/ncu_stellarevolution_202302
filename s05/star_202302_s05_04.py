#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/21 09:39:50 (CST) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = x**3 * sympy.exp (-x**2)

# positive infinity
pinf = sympy.oo

# integration of f(x)
I = sympy.integrate (f, (x, 0, pinf))

# printing result
print (f'I = {I}')
