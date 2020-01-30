##########2do
# In Python window you already have conversion rates. Create variables with amount of units to convert and variables with calculation.
#
# Your task is to convert:
#
# 80 kg to lb
# 54 km to miles
# 5 l to gal
# Finally, print results in sentences.
############

# Conversion rates
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Amount of units for conversion.
var_weight_kg=80
var_dist_km=54
var_volume_l=5

# Conversion calculations
var_weight_lb=var_weight_kg * kg_lb
var_dist_mile=var_dist_km * km_mile
var_volume_gal=var_volume_l * l_gal

# Final answers
print(var_weight_kg, "kg =", var_weight_lb, "lb")
print(var_dist_km, "km =", var_dist_mile, "miles")
print(var_volume_l, "l =", var_volume_gal, "gal")