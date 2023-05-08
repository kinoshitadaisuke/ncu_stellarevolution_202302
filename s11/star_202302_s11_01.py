#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/05/08 23:41:20 (CST) daisuke>
#

# central temperature of the Sun
Tsc = 1.5 * 10**7

# lowest hydrogen ignition temperature
Tmin = 4 * 10**6

# minimal mass of stars
Mmin = (Tmin / Tsc)**(7.0/4.0)

# printing result of calculation
print (f'Mmin = {Mmin:4.2f} Msolar')
