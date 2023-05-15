#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/05/15 12:08:06 (CST) daisuke>
#

# importing sympy module
import sympy

# variable
x = sympy.Symbol ('x')

# function f(x)
func = 1 / sympy.sqrt (1/x - 1)

# integration of f(x) from x=0 to x=1
I = sympy.integrate (func, (x, 0, 1))

# printing result
print (f'I = {I}')
