####2DO###
#some_str = input('Hello, please enter anything you want: ")

# if isupper(some_str):
# print('All letters in your input are uppercase')
# else if islower(some_str):
# print('All letters in your input are lowercase')
# else
# print('There are both uppercase and lowercase letters')
##################

some_str = input('Hello, please enter anything you want: ')
if some_str.isupper():
    print('All letters in your input are uppercase')
elif some_str.islower():
    print('All letters in your input are lowercase')
else:
    print('There are both uppercase and lowercase letters')