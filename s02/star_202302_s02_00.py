#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/20 15:35:44 (CST) daisuke>
#

# calculation of radius of delta Cep A

# importing math module
import math

# luminosity of delta Cep A in solar luminosity
L = 2000

# effective temperature of delta Cep A in K
T = 6000

# effective temperature of the Sun in K
T_s = 5800

# calculation of radius of delta Cep A in solar radius
R = math.sqrt (L) * (T / T_s)**-2

# printing result of calculation
print (f"radius of delta Cep A = {R:4.2f} solar radius")
