#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/14 11:10:31 (CST) daisuke>
#

# calculation of radius of a M-type dwarf

# importing math module
import math

# luminosity of a M-type dwarf in solar luminosity
L = 10**-3

# effective temperature of a M-type dwarf in K
T = 3000

# effective temperature of the Sun in K
T_s = 5800

# calculation of radius of a M-type dwarf in solar radius
R = math.sqrt (L) * (T / T_s)**-2

# printing result of calculation
print (f"radius of a M-type dwarf = {R:4.2f} solar radius")
