users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
emptylist = []

print("Dave" in users)
# returns boolean

print(users[0])
print(users[-1])
print(users[0:2])
print(users[0:])
print(users.index('Sara'))
print(len(data))

#modifying lists

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
#returns the value
print(users)

del users[0]
print(users)

data.clear()
print(data)

#sorting
users[1:2] = ['dave'] #replaces alex
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]

# nums.reverse()
# print(nums)

# nums.sort(reverse=True) #descending
# print(nums)

print(sorted(nums, reverse=True)) #non-destructive


#creating copies
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)

print(type(nums))