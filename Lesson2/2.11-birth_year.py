##########2Do
# Your task is to create a script called birth_year.py that will:
#
# ask the user for his/her age
# calculate the year the person was born in
# print the resulting year
# Example of running the script:
##############

from datetime import datetime
age=int(input('How old are you?'))
current_year = datetime.now().year
born_year=current_year - age
if born_year:
    print('You were born in ' + str(born_year))
else:
    print('You have entered something incorrect!')