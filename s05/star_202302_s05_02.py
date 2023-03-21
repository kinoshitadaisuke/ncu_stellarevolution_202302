#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/21 09:38:02 (CST) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = sympy.sqrt (4 - x**2)

# integration of f(x)
I = sympy.integrate (f, (x, 0, 2))

# printing result
print (f'I = {I}')
