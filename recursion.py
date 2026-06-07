def add_one(num):
    
    if (num >=9):
        return num + 1  # exits function nb not printed
    
    total = num + 1
    print(total)

    return add_one(total) # recursion

mynewtotal = add_one(0)
print(mynewtotal)