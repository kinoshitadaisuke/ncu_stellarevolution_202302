#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/05/08 23:48:39 (CST) daisuke>
#

# radius of red giant of L = 600 Ls and Teff = 3000 K

# effective temperature of the Sun
Ts = 5800

# effective temperature of red giant in K
Trg = 3000

# luminosity of red giant in solar luminosity
Lrg = 700

# radius of red giant in solar radius
Rrg = Lrg**0.5 * (Trg / Ts)**-2

# printing result of calculation
print (f'Rrg = {Rrg:5.1f} Rsolar')
