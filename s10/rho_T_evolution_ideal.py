#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/05/01 17:59:15 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constants
G  = scipy.constants.G
pi = scipy.pi
K0 = 1.36 * 10**4 # for solar composition
Bn = 0.206       # for n=1.5
Ms = 1.99 * 10**30

# output file name
file_eps = 'rho_T_evo_ideal.eps'
file_png = 'rho_T_evo_ideal.png'
file_pdf = 'rho_T_evo_ideal.pdf'
file_ps  = 'rho_T_evo_ideal.ps'

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
ideal_rad_logx = numpy.linspace (5.5, 10.0, n)
ideal_rad_logy = 3.0 * ideal_rad_logx - 20.73

# evolutionary track of 0.1 solar mass star
M = 0.1 * Ms
evo_001_logx = numpy.linspace (5.0, 7.05, n)
evo_001_logy = 3.0 * evo_001_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 0.3 solar mass star
M = 0.3 * Ms
evo_003_logx = numpy.linspace (5.0, 7.65, n)
evo_003_logy = 3.0 * evo_003_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 1 solar mass star
M = 1.0 * Ms
evo_010_logx = numpy.linspace (5.0, 8.35, n)
evo_010_logy = 3.0 * evo_010_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 3 solar mass star
M = 3.0 * Ms
evo_030_logx = numpy.linspace (5.0, 9.0, n)
evo_030_logy = 3.0 * evo_030_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 10 solar mass star
M = 10.0 * Ms
evo_100_logx = numpy.linspace (5.0, 10.0, n)
evo_100_logy = 3.0 * evo_100_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 30 solar mass star
M = 30.0 * Ms
evo_300_logx = numpy.linspace (5.0, 10.0, n)
evo_300_logy = 3.0 * evo_300_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel (r"$\log (T_c)$")
ax.set_ylabel (r"$\log (\rho_c)$")
ax.set_xlim (6.0, 10.0)
ax.set_ylim (0.0, 13.0)
ax.set_box_aspect (1)

# plotting data
ax.plot (ideal_deg_logx, ideal_deg_logy, '--')
ax.plot (ideal_rdeg_logx, ideal_rdeg_logy, '--')
ax.plot (deg_rdeg_logx, deg_rdeg_logy, '--')
ax.plot (ideal_rad_logx, ideal_rad_logy, '--')
ax.plot (evo_001_logx, evo_001_logy, '-', label=r"0.1 $M_\odot$", lw=3)
ax.plot (evo_003_logx, evo_003_logy, '-', label=r"0.3 $M_\odot$", lw=3)
ax.plot (evo_010_logx, evo_010_logy, '-', label=r"1 $M_\odot$", lw=3)
ax.plot (evo_030_logx, evo_030_logy, '-', label=r"3 $M_\odot$", lw=3)
ax.plot (evo_100_logx, evo_100_logy, '-', label=r"10 $M_\odot$", lw=3)
ax.plot (evo_300_logx, evo_300_logy, '-', label=r"30 $M_\odot$", lw=3)
ax.text (8.1, 5.0, "ideal gas", horizontalalignment='center')
ax.text (7.0, 8.0, "degenerate gas", horizontalalignment='center')
ax.text (8.0, 11.0, "relativistic degenerate gas", horizontalalignment='center')
ax.text (9.0, 2.5, "radiation pressure", horizontalalignment='center')
ax.set_title (r"evolutionary track on $T$-$\rho$ plane")
ax.legend (bbox_to_anchor=(1.01, 1.0), alignment='left')

# saving file
fig.savefig (file_eps, dpi=450)
fig.savefig (file_pdf, dpi=450)
fig.savefig (file_png, dpi=450)
fig.savefig (file_ps,  dpi=450)
