# Sets
nums = { 1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

# no duplicates allowed

nums = {1 , 2, 2, 3}
print(nums)
# {1, 2, 3}

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)
# {False, 1, 2, 3, 4}

# check for value in a set
print(2 in nums) # True

# but no index positions or keys

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# can use update with lists, tuples and dictionaries too

# merge 2 sets to create an entirely new set
one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)

print(one)
print(two)
print(mynewset)


# keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)

