#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/21 09:37:20 (CST) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = sympy.sin (x)

# pi
pi = sympy.pi

# integration of f(x)
I = sympy.integrate (f, (x, 0, pi))

# printing result
print (f'I = {I}')
