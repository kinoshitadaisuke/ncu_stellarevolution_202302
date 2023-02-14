#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/02/14 10:55:30 (CST) daisuke>
#

# calculation of distance to Vega

# annual parallax of Vega in mas
p_mas = 130.23

# calculation of distance to Vega in parsec
d = 1.0 / (p_mas * 10**-3)

# printing result of calculation
print (f"distance to Vega = {d:5.3f} pc")
