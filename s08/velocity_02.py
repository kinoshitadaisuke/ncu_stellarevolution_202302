#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/04/18 00:25:57 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.integrate

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

# initial condition (v_0 = 100 m/s)
v_0 = 100.0

# equation to solve
def dydx (t, y):
    # dy/dx = -g
    dy = -g_value
    # returning value
    return dy

output_x = numpy.linspace (0.0, 21.0, 2101)

# solving differential equation using Runge-Kutta method
sol = scipy.integrate.solve_ivp (dydx, [0.0, 50.0], [v_0], \
                                 dense_output=True, t_eval=output_x, \
                                 rtol=10**-6, atol=10**-9)

# x and y
list_t = sol.t
list_v = sol.y[0]

# printing result
print (f'{list_t}')
print (f'{list_v}')
