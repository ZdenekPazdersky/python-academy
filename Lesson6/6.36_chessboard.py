# ###2DO
# # Write a program that prints a chessboard of given size to the terminal. The program will need:
# #
# # the length of board's edge and
# # character that will serve to fill in the black squares
# # Example of running the program for the edge length of 5 and fill character "#":
# # ######
# f_char = input('Please enter the character string:')
# f_len = int(input('Please enter integer for length of your chessboard:'))
#
# for i in range(0, f_len):
#     for j in range(0, f_len):
#        if (i+j) % 2 == 0:
#            print(f_char, end='')
#        else:
#            print(' ', end='')
#     print('')

#ENGETO SOLUTION:
size = 5
sym = ['#',' ']
desk = []
for row in range(size):
    line = []
    for cell in range(size):
        i = (row+cell) % len(sym)
        line.append(sym[i])
    desk.append(''.join(line))
    print(''.join(line)) #sjednoti list naprovo do stringu nalevo
    print('Line: ', line)
    #print('desk: ', desk)
print(desk)
print('\n'.join(desk))  #sjednoti jednotlive polozky listu, zde s odsazenim na novy radek
print()
################