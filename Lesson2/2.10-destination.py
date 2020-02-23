# Greet the client
print('=' * 80)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print('=' * 80)

# Offer destinations
print('We can offer you the following destinations:')
print('-' * 80)
print('''
1 - Prague | 1000
2 - Wien | 1100
3 - Brno | 2000
4 - Svitavy | 1500
5 - Zlin | 2300
6 - Ostrava | 3400
''')
print('-' * 80)

# Get input from user about destination
selection = int(input('Please enter the destination number to select: '))

# Assign variables appropriate data
DESTINATIONS = ['Prague', 'Wien','Brno','Svitavy','Zlin','Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Check, whether entered valid input

# Get data from variables based on user's input
destination = DESTINATIONS[selection-1]
# Calculate the price and check whether discount applicable for the selected destination
if destination in DISCOUNT_25:
    print('We have a 25% discount for you...')
    price = PRICES[selection - 1] * 0.75
else:
    price = PRICES[selection - 1]

# Introduce registration

# Get input from user about personal data
name = input('NAME: ')
print('=' * 40)
surname = input('SURNAME: ')
print('=' * 40)
birth_year = input('YEAR of BIRTH: ')
print('=' * 40)
email = input('EMAIL: ')
print('=' * 40)
password = input('PASSWORD: ')
print('=' * 80)

# Check if the user is older than 15 years old
birth_year = int(birth_year)
if 2020-birth_year < 15:
        print('We cannot place discount for people younger than 15.')
# Check if email contains @ symbol
#char_at = '@'
elif '@' not in email:
        print('Missing @ in your email!')
# Check if password
# - is at least 8 chars long,
# - doesn't begin and end with a number
# - and contains both letters and numbers

elif (len(password) < 8
      or password[-1].isnumeric() or password[0].isnumeric()
      or password.isnumeric() or password.isalpha()
):
    print('Invalid characters')

# Thank user by the input name and inform him/her about the reservation made
else:
        print('Thank you ' + str(name))
        print('Your reservation has been done successful!')
        print('Total price is ' + str(price))