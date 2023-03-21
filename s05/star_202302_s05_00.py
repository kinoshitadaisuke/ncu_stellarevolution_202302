#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/21 09:35:20 (CST) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
f = 2 * x

# integration of f(x)
I = sympy.integrate (f, (x, 0, 10))

# printing result
print (f'I = {I}')
