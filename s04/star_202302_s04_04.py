#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/14 12:58:41 (CST) daisuke>
#

# thermal timescale of the Sun

# gravitational constant
G = 6.67 * 10**-11

# solar mass
M_s = 1.99 * 10**30

# solar radius
R_s = 6.96 * 10**8

# solar luminosity
L_s = 3.84 * 10**26

# speed of light in vacuum
c = 2.998 * 10**8

# proton mass
m_p = 1.6726 * 10**-27

# helium-4 nucleus mass
m_he4 = 6.643 * 10**-27

# delta-m
delta_m = m_p * 4 - m_he4

# calculation of epsilon
epsilon = delta_m / (m_p * 4)

# calculation of nuclear timescale of the Sun
tau_nuc = epsilon * M_s * c**2 / L_s

# printing result of calculation
print (f'Nuclear timescale of the Sun:')
print (f'  tau_nuc = {tau_nuc:g} sec')
print (f'          = {tau_nuc / 3600.0:g} hr')
print (f'          = {tau_nuc / (3600.0 * 24.0):g} day')
print (f'          = {tau_nuc / (3600.0 * 24.0 * 365.25):g} yr')
