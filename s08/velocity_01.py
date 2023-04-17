#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/04/18 00:17:45 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# standard acceleration of gravity
g = scipy.constants.physical_constants['standard acceleration of gravity']

# value of g
g_value = g[0]

# unit of g
g_unit = g[1]

# error of g
g_error = g[2]

# printing result
print (f'g = {g_value} +/- {g_error} [{g_unit}]')
