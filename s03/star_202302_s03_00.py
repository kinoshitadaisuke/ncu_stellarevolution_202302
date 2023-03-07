#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/07 14:04:01 (CST) daisuke>
#

# parameters
alpha   = 1/2
m_H     = 1.66 * 10**-27
G       = 6.67 * 10**-11
k       = 1.38 * 10**-23
M_solar = 1.99 * 10**30
R_solar = 6.96 * 10**8

# calculation of average temperature of 1 solar mass star of 1 solar radius
T = alpha * 1/3 * m_H * G / k * M_solar / R_solar

# printing average temperature of 1 solar mass 1 solar radius star
print (f"T = {T:g} K")
