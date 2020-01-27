# Greet the client
print("="*30)
print("""Welcome to the DESTINATIO,
place where people plan their trips""")
print("="*30)

# Offer destinations
print("The following destination could be offered:")
print("-"*30)
print("""
1 - Prague  | 1000
2 - Wien    | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
""")
print("-"*30)

# Get input from user about destination
dest_select=int(input("Please enter the destination number to select:"))
print("Your selection:", dest_select)

# Assign variables appropriate data
offer_dest=["Prag","Wien", "Brno", "Svitavy", "Zlin", "Ostrava"]
offer_price=[1000,1100,2000,1500,2300,3400]

# Get data from variables based on user's input

# Introduce registration
print("-"*30)
print("""In order to complete your reservations, please share few details 
about yourself with us""")
print("-"*30)


# Get input from user about personal data
NAME="Zdenek"
#NAME=str(input("Enter your name:"))
#SURNAME=str(input("Enter your surname:"))
#BIRTH=int(input("Enter year of birth:"))
#EMAIL=str(input("Enter your email:"))
#PWD=str(input("Enter your password:"))

# Thank user by the input name and inform him/her about the reservation made
print("Thank you", NAME)
print("We have made your reservation to "+ offer_dest[dest_select-1]) #second argument list
print("The total price is", offer_price[dest_select-1]) #second argument integer

