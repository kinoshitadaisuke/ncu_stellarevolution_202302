#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/05/01 17:59:07 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_eps = 'rho_T_state.eps'
file_png = 'rho_T_state.png'
file_pdf = 'rho_T_state.pdf'
file_ps  = 'rho_T_state.ps'

# number of data points
n = 10000

# border of ideal gas and degenerate gas
ideal_deg_logx = numpy.linspace (5.0, 9.0, n)
ideal_deg_logy = 1.5 * ideal_deg_logx - 4.13

# border of ideal gas and relativistic degenerate gas
ideal_rdeg_logx = numpy.linspace (9.0, 10.0, n)
ideal_rdeg_logy = 3.0 * ideal_rdeg_logx - 17.60

# border of degenerate gas and relativistic degenerate gas
deg_rdeg_logx = numpy.linspace (5.0, 9.0, n)
deg_rdeg_logy = numpy.array ([9.34] * n)

# border of ideal gas and radiation
ideal_rad_logx = numpy.linspace (6.5, 10.0, n)
ideal_rad_logy = 3.0 * ideal_rad_logx - 20.73

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel (r"$\log (T_c)$")
ax.set_ylabel (r"$\log (\rho_c)$")
ax.set_xlim (5.0, 10.0)
ax.set_ylim (0.0, 13.0)
ax.set_box_aspect (1)

# plotting data
ax.plot (ideal_deg_logx, ideal_deg_logy, '-', label=r"$P_{ideal}=P_{deg}$")
ax.plot (ideal_rdeg_logx, ideal_rdeg_logy, '-', label=r"$P_{ideal}=P_{r-deg}$")
ax.plot (deg_rdeg_logx, deg_rdeg_logy, '-', label=r"$P_{deg}=P_{r-deg}$")
ax.plot (ideal_rad_logx, ideal_rad_logy, '-', label=r"$P_{ideal}=10 P_{rad}$")
ax.text (7.5, 5.0, "ideal gas", horizontalalignment='center')
ax.text (6.0, 7.0, "degenerate gas", horizontalalignment='center')
ax.text (7.0, 11.0, "relativistic degenerate gas", horizontalalignment='center')
ax.text (9.0, 3.0, "radiation pressure", horizontalalignment='center')
ax.set_title (r"$\rho$-$T$ diagram")
ax.legend (loc='lower left')

# saving file
fig.savefig (file_eps, dpi=450)
fig.savefig (file_pdf, dpi=450)
fig.savefig (file_png, dpi=450)
fig.savefig (file_ps,  dpi=450)
