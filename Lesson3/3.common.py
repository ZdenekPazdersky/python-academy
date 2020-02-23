
str_1='Ney York'
str_2 = 'Yorkshire'
print(str_1)
print(str_2)

str_1 = set(str_1)
print(type(str_1))
str_2 = set(str_2)

print('Common letters:', str_1 & str_2) #prunit znaku INTERSECTION
print('Common', str_1.intersection(str_2))

print('Common letters:', str_1 | str_2) #sjednoceni UNION str1.union(str2)
print('Common', str_1.union(str_2))

print('Unique str_1:', str_1 - str_2) #unikatni str_1 DIFFERENCE    str1.difference(str2
print('Unique 1st', str_1.difference(str_2))

print('Unique str_2:', str_2 - str_1) #unikatni str_1  DIFFERENCE
print('Unique 1st', str_2.difference(str_1))

print('SUnique in both:', str_1 ^ str_2) #Symetrick difference, to co neni spolecne ve sjednoceni, tj unikatni znaky pro oba
print('Unique 1st', str_2.symmetric_difference(str_1))