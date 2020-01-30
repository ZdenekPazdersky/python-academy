########2do
# Your task is to create a script called convert_day.py that will:
#
# ask for a number between 1 to 7
# return the name of corresponding weekday (1 - 'Monday', 2-'Tuesday', 3 - 'Wednesday', 4 - 'Thursday', 5 - 'Friday', 6 - 'Saturday', 7 - 'Sunday')
# if no input has been provided (user hitting enter without typing anything), the program should print: 'No input provided'
# if the input is not a number the program should print: 'Enter only numbers, please'
###########

day_Nr=input('Enter the number of the day in week [1..7]:')
valid_Nr=['1','2','3','4','5','6','7']
week_day=('Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday')
#if day_Nr=='':
if not day_Nr:
    print('No input provided!')
elif day_Nr not in valid_Nr:
    print('Enter only numnbers 1..7 please!')
else:
    print('You have chosen ' + week_day[int(day_Nr) -1])