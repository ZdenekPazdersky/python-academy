# ####2DO
# Create a function that will be able to generate a table that should have the following headers: 'Name','Item','Amount','Unit_Price', 'Total_Price'
#
# The function should take only one input - number of rows, the generated table should have. The data should be generated from the following variables:
#
# values from customers should randomly populate the column Name
# customers = ['Bettison, Elnora',
#              'Doro, Jeffrey',
#              'Idalia, Craig',
#              'Conyard, Phil',
#              'Skupinski, Wilbert',
#              'McShee, Glenn',
#              'Pate, Ashley',
#              'Woodison, Annie']
# values from products should randomly populate the columns Item - the first part of the tuple, Unit_Price - second part of the tuple
# products = [('DROXIA', 33.86),('WRINKLESS PLUS',23.55),
#             ('Claravis', 9.85), ('Nadolol', 12.35),
#             ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
#             ('Metolazone', 43.06), ('PAXIL', 14.78)]
# values for the column Amount should be generated randomly from numbers in range 1 to 100 (including)
# values for the column Total_Price should be calculated as the product of Amount and Unit_Price
# The resulting list could look like this:
#
# dataset = [ ['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
#             ['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
#             ['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
#             ['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
#             ['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
#             ['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
#             ['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
#             ['Woodison, Annie', 'DROXIA', 50, 33.86, 1693.0],
#             ['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],
#             ...
# #######
customers = ['Bettison, Elnora', 'Doro, Jeffrey', 'Idalia, Craig', 'Conyard, Phil', 'Skupinski, Wilbert',
                 'McShee, Glenn', 'Pate, Ashley', 'Woodison, Annie']
products = [('DROXIA', 33.86), ('WRINKLESS PLUS', 23.55),
            ('Claravis', 9.85), ('Nadolol', 12.35),
            ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
            ('Metolazone', 43.06), ('PAXIL', 14.78)]

dataset = [['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price']]


def generate_data(rows_max:int):
    import random
    for index in range(0, rows_max):
        name = random.choice(customers)
        item, unit_price = random.choice(products)
        amount = random.randint(1, 100)
        data_insert = [name, item, amount, unit_price, amount * unit_price]
        dataset.append(data_insert)
    return dataset

test = generate_data(3)
print(test)
