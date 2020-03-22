# ###2DO
# Our task is to create a program that will take time input in 24 hours format and will convert it into english time format including PM and AM.
#
# Example of running the program:
#
# ~/PythonBeginner/Lesson6 $ python convert_time.py
# Please enter your time: 17 : 35
# Converted to English: 5 : 35 PM
# ######
print(5 % 12)
Input_time = input('Please enter your time in the 24h format HH:MM: ').split(':')
#Input_time = Input_time.split(':')
print(Input_time, type(Input_time))
result = []
format_hour = 'AM'
for index in Input_time:
    index = int(index.strip())
    result.append(index)
if result[0] > 12:
    result[0] = result[0] % 12
    format_hour = 'PM'
converted_time = str(result[0]) + ':' + str(result[1]).zfill(2) + ' ' + format_hour
print(converted_time)

#ENGETO SOLUTION
# time = input('Please enter your time: ')
# hours, mins = time.split(':')
# adjusted_h = hours if int(hours)==12 else str(int(hours) % 12)
# print(adjusted_h)
# daytime = ['AM','PM'][int(hours)>=12]
# print('Converted to English: ' + adjusted_h + ':' + mins + ' ' + daytime)
# ###############
