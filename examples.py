value = "y"
count = 0

while value: # equivalent of 'while value exists' or while value == True
    count += 1
    print(count)
    if (count == 5): # this code won't be reached due to the else continue statement
        break
    else:
        value = 0
        continue