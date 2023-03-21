#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/21 09:39:14 (CST) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = sympy.exp (-x**2)

# positive infinity
pinf = sympy.oo

# negative infinity
ninf = -sympy.oo

# integration of f(x)
I = sympy.integrate (f, (x, ninf, pinf))

# printing result
print (f'I = {I}')
