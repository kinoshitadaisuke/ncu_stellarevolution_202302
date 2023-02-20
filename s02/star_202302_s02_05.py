#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/20 15:51:06 (CST) daisuke>
#

# calculation of pressure at the centre of the Sun

# importing math module
import math

# value of pi
pi = math.pi

# gravitational constant
G = 6.67 * 10**-11

# solar radius in metre
R_s = 6.96 * 10**8

# solar mass in kg
M_s = 1.99 * 10**30

# calculation of pressure at the centre of the Sun
P_c = G * M_s**2 / (8.0 * pi * R_s**4)

# printing result of calculation
print (f"pressure at the centre of the Sun = {P_c:g} N m^-2")
print (f"                                  = {P_c / (1.013 * 10**5):g} atm")
