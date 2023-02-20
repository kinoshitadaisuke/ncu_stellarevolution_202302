#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/20 15:35:54 (CST) daisuke>
#

# calculation of radius of Sirius B

# importing math module
import math

# luminosity of Sirius B in solar luminosity
L = 0.056

# effective temperature of Sirius B in K
T = 25000

# effective temperature of the Sun in K
T_s = 5800

# calculation of radius of Sirius B in solar radius
R = math.sqrt (L) * (T / T_s)**-2

# printing result of calculation
print (f"radius of Sirius B = {R:5.3f} solar radius")
