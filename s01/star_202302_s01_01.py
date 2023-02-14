#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/14 10:52:38 (CST) daisuke>
#

# calculation of distance to Proxima Centauri

# annual parallax of Proxima Centauri in arcsec
p = 0.76

# calculation of distance to Proxima Centauri in parsec
d = 1.0 / p

# printing result of calculation
print (f"distance to Proxima Centauri = {d:4.2f} pc")
