#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/27 16:55:30 (CST) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 1H (proton)
massexcess_1H, err_massexcess_1H = nuclyr.mass.massExcess (1, 1)

# mass excess of 4He (helium-4)
massexcess_4He, err_massexcess_4He = nuclyr.mass.massExcess (2, 4)

# energy produced by a reaction to create a 4He from four protons
energy_ppchain = massexcess_1H * 4 - massexcess_4He

# printing results
print (f'mass excess of 1H (proton)    = {massexcess_1H:6.3f}', \
       f'+/- {err_massexcess_1H} MeV')
print (f'mass excess of 4He (helium-4) = {massexcess_4He:6.3f}', \
       f'+/- {err_massexcess_4He} MeV')
print (f'energy produced by pp-chain   = {massexcess_1H:6.3f} x 4 -', \
       f'{massexcess_4He} MeV')
print (f'                              = {energy_ppchain:6.3f} MeV')
