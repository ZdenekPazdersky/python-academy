

# Extract and print first 5 letters
origin="indexing"
print("Start string:" + origin)
first5letters=origin[0:5]
print("First 5 letters: "+ first5letters)



# Extract and print last 5 letters
last5letters=origin[-5:]
print("Last 5 letters: "+ last5letters)


# Extract and print each 3rd letter
origin_l=len(origin)
step3=origin[0:origin_l:3]
#step3=origin[::3]
print("Every 3rd letter: "+ step3)