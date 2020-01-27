# ###Todo
# #In the Python window you already have Mercedes and Rolls-Royce prices listed (don't forget to covert string to integer!). In addition, you have to create a variable that will ask the user for the extra cost. Then you will need to calculate:
# The price for two Mercedes,
# The Mercedes and Rolls-Royce prices,
# The price of two Rolls-Royce with extra equipment (each),
# Price for Mercedes with optional equipment.
# Finally, the program should print down everything clearly. Go ahead!
# ###

# Prices
mercedes    = 150
rolls_royce = '400'
rolls_royce = int(rolls_royce)
extra_cost=int(input("Enter extra cost:"))

price_1=2*mercedes
price_2=mercedes+rolls_royce
price_3=2*(rolls_royce+extra_cost)
price_4=mercedes+extra_cost

print("PRICE TABLE:")
print("2xMercedes           |",  price_1)
print("Mercedes+Rolls-Royce |",  price_2)
print("2x extra Rolls-Royce |",  price_3)
print("extra Mercedes       |",  price_4)