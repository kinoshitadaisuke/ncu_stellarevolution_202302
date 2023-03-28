#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/03/28 12:35:48 (CST) daisuke>
#

# importing nuclyr module
import nuclyr.mass

# mass excess of 4He (helium-4)
massexcess_4He, err_massexcess_4He = nuclyr.mass.massExcess (2, 4)

# mass excess of 12C (carbon-12)
massexcess_12C, err_massexcess_12C = nuclyr.mass.massExcess (6, 12)

# energy produced by triple-alpha process
energy_3alpha = massexcess_4He * 3 - massexcess_12C

# printing results
print (f'mass excess of 4He (helium-4)   = {massexcess_4He:6.3f}', \
       f'+/- {err_massexcess_4He} MeV')
print (f'mass excess of 12C (carbon-12)  = {massexcess_12C:6.3f}', \
       f'+/- {err_massexcess_12C} MeV')
print (f'energy produced by triple-alpha = {massexcess_4He:6.3f} x 3', \
       f'- {massexcess_12C} MeV')
print (f'                                = {energy_3alpha:6.3f} MeV')
