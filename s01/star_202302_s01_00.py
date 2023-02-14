#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/14 10:49:09 (CST) daisuke>
#

# calculation of 1 parsec in metre

# importing math module
import math

# 1 au in metre
au = 1.496 * 10**11

# value of pi
pi = math.pi

# calculation of 1 pc in metre
pc = au * 180 * 3600 / pi

# printing result
print (f"1 pc = {pc:g} m")
