#Todo
# Create script, which will:
#
# assign an empty list to variable candidates,
# print the content of variable candidates introducing it with a string 'Candidates at the beginning:',
# assign a list to variable employees, containing strigns: 'Francis', 'Ann', 'Jacob', 'Claire',
# print employees content introducing it with a string 'Employees at the beginning:',
# add the names 'Bruno' and 'Agnes' to the empty 'candidates' list,
# print the content of candidates introducing it with a string 'New names added to candidates:',
# insert the name 'Bruno' stored in the candidate list into the` employees' list at index 1,
# print the content of the employees variable introducing it with a string: 'New names added to employees':

# Create Candidate
candidates = []

# Print candidates at the beginning
print("Candidates at the beginning:", candidates)

# Create employees
employees = ["Francis", "Ann", "Jacob", "Claire"]

# Print employees at the beginning
print("Employees at the beginning:", employees)


# Add new candidates
#candidates = candidates + ["Bruno", "Agnes"]
candidates.append("Bruno")
candidates.append("Agnes")


# Print new candidates
print("New names added to candidates:", candidates)


# Insert name
employees.insert(1, candidates[0]) #To Insert Bruno from list candidates into employees list at index1

# Print the employees list after entering a new name
print("New names added to employees: ", employees)