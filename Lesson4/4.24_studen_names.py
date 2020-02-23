#####2do
# We have a class of students. All the student names are stored in the list students.
# Our task is to extract an overview of what unique names and surnames do we have in the class.
########
students = ['Adam, Baker', 'Chelsea, Archer',
            'Marcus, Archer', 'Oliver, Cook',
            'Alex, Dyer', 'Sandra, Turner',
            'Ann, Fisher', 'Glenn, Hawkins',
            'Samuel, Baker', 'Clara, Slater',
            'Tyler, Hunt', 'Alex, Smith',
            'Clara, Woodman', 'Abraham, Mason',
            'Marcus, Sawyer', 'Alex, Glover',
            'Glenn, Cook', 'Clara, Fisher',
            'Alfred, Dyer', 'Curt, Head',
            'Oliver, Slater', 'Alex, Mason',
            'Tyler, Fisher', 'Ann, Parker',
            'Samuel, Hawkins', 'Ann, Woodman',
            'Sandra, Slater', 'Curt, Dyer']
unique_names = set()
unique_surnames = set()
# i = 0
# j = 0
# while i < len(students):
#     j = students[i].index(',')
#     unique_names.add(students[i][:j])
#     unique_surnames.add(students[i][j+2:])
#     i = i + 1
#Engeto solution
while students:
    name, surname = students.pop().split(', ')
    unique_names.add(name)
    unique_surnames.add(surname)
#End of Engeto solution

print('Unique names: ', unique_names)
print('Unique surnames: ', unique_surnames)