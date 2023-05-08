#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/05/08 23:31:51 (CST) daisuke>
#

# importing math module
import math

# value of pi
pi = math.pi

# gravitational constant
G = 6.67 * 10**-11

# constant B
B = 0.157

# constant K2'
K2p = 1.24 * 10**10

# mu_e
mu_e = 2

# Chandrasekhar mass
Mch = math.sqrt ( K2p**3 / (mu_e**4 * 4 * pi * B**3 * G**3) )

# solar mass
Ms = 1.99 * 10**30

# printing result of calculation
print (f'Mch = {Mch:G} kg')
print (f'    = {Mch / Ms:4.2f} Msolar')
