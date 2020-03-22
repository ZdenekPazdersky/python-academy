# ###2DO
# Let's create a program that will sort any list of strings according to alphabetical order. It is not permitted to use methods and functions as sort() or sorted().
# ######
names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal'
        ]
sorted_names = []
print(names.pop(0))
while names:
    minimum = min(names)
    for index in range(0, len(names)):
        if minimum == names[index]:
            sorted_names.append(names[index])
            names.remove(minimum)
            break
#print('Original list: ', names)
print('Sorted names: ', sorted_names)

# ####ENGETO SOLUTION
# sorted_names = [names.pop(0)]
# for name in names:
#     for i,s_name in enumerate(sorted_names):
#         if name < s_name:
#             sorted_names.insert(i,name)
#             break
#     else:
#         sorted_names.append(name)
# print(sorted_names)
# ###################