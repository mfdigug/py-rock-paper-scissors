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

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)
