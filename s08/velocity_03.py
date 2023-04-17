#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/04/18 00:33:04 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'velocity_03.png'

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

output_x = numpy.linspace (0.0, 25.0, 2501)

# solving differential equation using Runge-Kutta method
sol = scipy.integrate.solve_ivp (dydx, [0.0, 25.0], [v_0], \
                                 dense_output=True, t_eval=output_x, \
                                 rtol=10**-6, atol=10**-9)

# x and y
list_t = sol.t
list_v = sol.y[0]

# printing result
print (f'{list_t}')
print (f'{list_v}')

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'velocity change')
ax.set_xlabel (r'$t$')
ax.set_ylabel (r'$v$')

# plotting data
ax.plot (list_t, list_v, 'b-', label='numerical solution', linewidth=5)
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=300)
