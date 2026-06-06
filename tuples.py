#tuples can't be changed

mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

#packing tuples
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

#unpacking tuples

(one, *two, hey) = anothertuple
print(one)
print(two) #remaining values unpacked into a list
print(hey) 

print(anothertuple.count(2)) # returns number of '2's in the tuple
