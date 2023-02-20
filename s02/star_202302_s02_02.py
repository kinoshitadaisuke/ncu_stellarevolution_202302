#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/20 15:36:02 (CST) daisuke>
#

# calculation of radius of Vega

# importing math module
import math

# luminosity of Vega in solar luminosity
L = 40

# effective temperature of Vega in K
T = 9600

# effective temperature of the Sun in K
T_s = 5800

# calculation of radius of Vega in solar radius
R = math.sqrt (L) * (T / T_s)**-2

# printing result of calculation
print (f"radius of Vega = {R:4.2f} solar radius")
