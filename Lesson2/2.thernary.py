my_str = 'python'
result = ''

# if my_str.istitle():
#     result = 'Titlecased'
# else:
#     result = 'Not titlecased'

result='Titlecased' if my_str.istitle() else 'Not titlecased'
print(result)