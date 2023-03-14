#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/14 12:42:54 (CST) daisuke>
#

# escape velocity from the Earth

# gravitational constant
G = 6.67 * 10**-11

# Earth mass
M_e = 5.97 * 10**24

# Earth radius
R_e = 6.37 * 10**6

# calculation of escape velocity from the Earth
v_esc = (2.0 * G * M_e / R_e)**0.5

# printing result of calculation
print (f'Escape velocity from the Earth:')
print (f'  v_esc = {v_esc:8.1f} m/s')
print (f'        = {v_esc * 10**-3:8.1f} km/s')
