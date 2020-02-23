####2Do##
# We have this dictionary:
# data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}
#
# In this task, we will try to verify if the user enters a password that belongs to his account.
#
# The output should looks like:
#
# ~/PythonBeginner/Lesson3 $ python verify.py
# Please enter username: Mark
# Please enter password: 1234
# Permission granted
# If the password will be type incorrectly or is incorrect in general:
#
# ~/PythonBeginner/Lesson3 $ python verify.py
# Please enter username: Mark
# Please enter password: 444
# Password or username is wrong
#########
data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}
print(data)
usr=input('Please enter username:')
pwd=input('Please enter password:')

if usr in data.keys() and pwd == data.get(usr):
    print('Permission granted...User: ', usr, ', pwd:', pwd)
else:
    print('Password or username is wrong.')

####Engeto solution
# our dictionary with data
# data = {
# 'user1': 'password1',
# 'Mark': '1234',
# 'Danny': 'qwert',
# }
# 
# # we want to ask user for username and password
# username    = input('Please enter the username: ')
# password    = input('Please enter the password: ')
#
# # two conditions for evaluating the inputs
# if data.get(username) != password:
#     print('Password or username is wrong')
#
# elif data.get(username) == password:
#     print('Permission granted')
###################
