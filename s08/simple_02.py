#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/04/17 23:42:03 (CST) daisuke>
#

# importing numpy module
import numpy

# coefficient
k = 0.1

# initial condition
y_0 = 100.0

# x values
output_x = numpy.linspace (0.0, 50.0, 5001)

# analytical solution
ana_x = output_x
ana_y = y_0 * numpy.exp (-k * ana_x)

# printing result
print (f'analytical solution:')
print (f'{ana_x}')
print (f'{ana_y}')
