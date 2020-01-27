# Save name
name=input("Enter your first name:")

# Print name
print(name +" has been saved.")

# Save surname
surname=input("Enter your surname:")

# Print surname
print (surname + " has been saved.")

# Create and print variable full_name
fullname=name+" "+surname
print("Full name: "+fullname)

# Create and print variable name_length
fullname_lenght=len(fullname)
print("Your fullname has ", fullname_lenght, " characters.")


# Print bounded variable full_name
print("="*fullname_lenght)
print(fullname)
print("="*fullname_lenght)