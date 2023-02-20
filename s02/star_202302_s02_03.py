#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/20 15:36:15 (CST) daisuke>
#

# calculation of radius of the Sun in red giant phase

# importing math module
import math

# luminosity of the Sun in red giant phase in solar luminosity
L = 1000

# effective temperature of the Sun in red giant phase in K
T = 3000

# effective temperature of the current Sun in K
T_s = 5800

# calculation of radius of the Sun in red giant phase in solar radius
R = math.sqrt (L) * (T / T_s)**-2

# solar radius in metre
R_s = 6.963 * 10**8

# length of 1 au in metre
au = 1.496 * 10**11

# radius of the Sun in red giant phase in au
R_au = R * R_s / au

# printing result of calculation
print (f"radius of then Sun in red giant phase = {R:4.2f} solar radius")
print (f"                                      = {R_au:4.2f} au")
