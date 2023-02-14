#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/14 11:03:05 (CST) daisuke>
#

# calculation of peak wavelength of T=3000 K blackbody radiation

# temperature of blackbody in K
T = 3000

# calculation of peak wavelength of blackbody radiation
lambda_max = 2.898 * 10**-3 / T

# printing result of calculation
print (f"peak wavelength of T={T}K blackbody")
print (f"  {lambda_max:g} m")
print (f"= {lambda_max * 10**6:4.2f} micron")
print (f"= {lambda_max * 10**9:6.1f} nm")
