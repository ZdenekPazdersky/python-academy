# ###2DO
# Create a function change_coins that will simulate a ticket machine in that it will return the least possible amount of coins.
#
# Our machine should work with coins of the following denominations: 1, 2, 5, 10, 20, 50
#
# For example, if the amount to be returned by the machine is 124, the returned coins should be: two 50, one 20, two 2
#
# And this is how it will look like in a terminal:
# >>> change_coins(124)
# {50:2, 20: 1, 2:2}
# >>> change_coins(0)
# {}
# ######

def change_coins(number):
    coins = [1, 2, 5, 10, 20, 50]
    result = {}
    division_result = 0
    for index in range(len(coins) -1, -1, -1):
        division_result = number // coins[index]
        if division_result > 0:
            result[coins[index]] = division_result
            number -= coins[index] * division_result
    return result

print(change_coins(1376))

# ###ENGETO solution
# def change_coins(amount, coins = [50,20,10,5,2,1]):
#     coin_counts = {}
#     for coin in coins:
#         if not amount:    break
#         count, amount = divmod(amount, coin)
#         if count:
#             coin_counts[coin] = count
#     return coin_counts
# print(change_coins(1376))