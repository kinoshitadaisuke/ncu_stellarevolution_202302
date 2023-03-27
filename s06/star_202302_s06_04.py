#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/27 17:24:29 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# files
file_data   = 'binding_energy.data'
file_output = 'binding_energy_110.png'

# lists for storing data
data_x = []
data_y = []
names  = []

# opening data file
with open (file_data, 'r') as fh:
    # reading data file
    for line in fh:
        # splitting line
        list_record    = line.split ()
        # data
        mass_number    = int (list_record[2])
        binding_energy = float (list_record[6])
        isotope_name   = "%s-%s" % (list_record[3], list_record[2])
        # printing data
        print ("%d %f %s" % (mass_number, binding_energy, isotope_name) )
        # appending data to lists
        data_x.append (mass_number)
        data_y.append (binding_energy)
        names.append (isotope_name)

# printing data read
print (f'{data_x}')
print (f'{data_y}')
print (f'{names}')

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Atomic Weight [amu]')
ax.set_ylabel ('Binding Energy per Nucleon [keV]')
ax.set_xlim (1.0, 110.0)
ax.set_ylim (0.0, 9000.0)
ax.set_xticks (range (10, 110, 10) )
ax.grid ()

# making a plot
ax.plot (data_x, data_y, marker='o', markersize=8, \
         color='black', markerfacecolor='blue')
ax.arrow (56.0, 6500.0, 0.0, 1700.0, length_includes_head=True, width=0.5, \
          head_length=500, color='red')
ax.text (56.0, 5700, "$\sf {}^{56}Fe$", fontsize=24, \
         horizontalalignment='center', verticalalignment='center')
fig.savefig (file_output, dpi=450)
