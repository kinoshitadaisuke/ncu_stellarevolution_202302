#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/14 12:57:07 (CST) daisuke>
#

# thermal timescale of the Sun

# gravitational constant
G = 6.67 * 10**-11

# solar mass
M_s = 1.99 * 10**30

# solar radius
R_s = 6.96 * 10**8

# solar luminosity
L_s = 3.84 * 10**26

# calculation of thermal timescale of the Sun
tau_th = G * M_s**2 / (R_s * L_s)

# printing result of calculation
print (f'Thermal timescale of the Sun:')
print (f'  tau_th = {tau_th:g} sec')
print (f'         = {tau_th / 3600.0:g} hr')
print (f'         = {tau_th / (3600.0 * 24.0):g} day')
print (f'         = {tau_th / (3600.0 * 24.0 * 365.25):g} yr')
