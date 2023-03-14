#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/14 12:45:08 (CST) daisuke>
#

# dynamical timescale of the Sun

# gravitational constant
G = 6.67 * 10**-11

# solar mass
M_s = 1.99 * 10**30

# solar radius
R_s = 6.96 * 10**8

# calculation of dynamical timescale of the Sun
tau_dyn = (R_s**3 / (2.0 * G * M_s) )**0.5

# printing result of calculation
print (f'Dynamical timescale of the Sun:')
print (f'  tau_dyn = {tau_dyn:8.1f} sec')
print (f'          = {tau_dyn / 60.0:8.1f} min')
