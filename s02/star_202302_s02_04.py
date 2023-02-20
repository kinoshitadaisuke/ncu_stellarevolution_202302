#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/20 15:36:27 (CST) daisuke>
#

# calculation of mean density of a white dwarf

# importing math module
import math

# value of pi
pi = math.pi

# radius of typical white dwarf in solar radius
R = 0.01

# mass of typical white dwarf in solar mass
M = 1.0

# solar radius in metre
R_s = 6.96 * 10**8

# solar mass in kg
M_s = 1.99 * 10**30

# calculation of mean density of white dwarf
rho_SI = M * M_s / (4.0 / 3.0 * pi * (R * R_s)**3 )

# printing result of calculation
print (f"mean density of white dwarf = {rho_SI:g} kg/m^3")
print (f"                            = {rho_SI * 10**-3:g} g/cc^3")
