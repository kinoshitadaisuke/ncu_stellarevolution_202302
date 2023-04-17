#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/04/17 23:41:39 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# coefficient
k = 0.1

# initial condition
y_0 = 100.0

# output file name
file_output = 'simple_01.png'

# equation to solve
def dydx (t, y):
    # dy/dx = -ky
    dy = -k * y
    # returning value
    return dy

# x values
output_x = numpy.linspace (0.0, 50.0, 5001)

# solving differential equation using Runge-Kutta method
sol = scipy.integrate.solve_ivp (dydx, [0.0, 50.0], [y_0], \
                                 dense_output=True, t_eval=output_x, \
                                 rtol=10**-6, atol=10**-9)

# x and y
list_x = sol.t
list_y = sol.y[0]

# printing results
print (f'numerical solution:')
print (f'{list_x}')
print (f'{list_y}')

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'$dy/dx = -ky$')
ax.set_xlabel (r'$x$')
ax.set_ylabel (r'$y$')

# plotting data
ax.plot (list_x, list_y, 'b-', label='numerical solution', linewidth=5)
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=300)
