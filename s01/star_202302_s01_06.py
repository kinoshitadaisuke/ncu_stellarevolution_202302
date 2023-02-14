#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/14 11:08:00 (CST) daisuke>
#

# calculation of radius of Betelgeuse

# importing math module
import math

# luminosity of Betelgeuse in solar luminosity
L = 126000

# effective temperature of Betelgeuse in K
T = 3600

# effective temperature of the Sun in K
T_s = 5800

# calculation of radius of Betelgeuse in solar radius
R = math.sqrt (L) * (T / T_s)**-2

# printing result of calculation
print (f"radius of Betelgeuse = {R:5.1f} solar radius")
