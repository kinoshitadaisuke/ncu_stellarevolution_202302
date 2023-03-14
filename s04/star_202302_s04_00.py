#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/14 12:41:21 (CST) daisuke>
#

# escape velocity from the Sun

# gravitational constant
G = 6.67 * 10**-11

# solar mass
M_s = 1.99 * 10**30

# solar radius
R_s = 6.96 * 10**8

# calculation of escape velocity from the Sun
v_esc = (2.0 * G * M_s / R_s)**0.5

# printing result of calculation
print (f'Escape velocity from the Sun:')
print (f'  v_esc = {v_esc:8.1f} m/s')
print (f'        = {v_esc * 10**-3:8.1f} km/s')
