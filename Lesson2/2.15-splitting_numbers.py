###2DO########
# Create a script split_nums.py that will:
#
# ask the user for a number
# split the given number in halves (e.g. 123456 -> split to 123 and 456, 12345 -> 12 and 345)
# convert both halves into an integer
# if both halves are an even integer, print: 'Success' - e.g. 12 and 34
# if only the first part is even, print: 'First' - e.g. 12 and 345
# if the second part is even, print: 'Second' - e.g. 123 and 456
# if neither of the numbers is even print: 'Neither' - 123 and 455
# if nothing has been entered (the user just hit Enter), print: 'No input provided'
#########

num=input('Please, enter number:')
if num:
    num_1st = int(num[:(len(num)//2)])
    num_2nd = int(num[(len(num)//2):])
    print('Number splitted into: ' + str(num_1st) +' ' + str(num_2nd))

    num_1st_res = bool(num_1st % 2)     # 1=True=odd, 0=False=even
    num_2nd_res = bool(num_2nd % 2)

    if not num_1st_res and not num_2nd_res: #better to read >> if 0 == num_1st % 2 and 0 == num_2nd % 2
        print('Success (both even)')
    elif num_1st_res and num_2nd_res:
        print('Neither (both are odd) ')
    elif not num_1st_res:
        print('First part is even')
    else:
        print('Second is even')
else:
    print('No input provided')