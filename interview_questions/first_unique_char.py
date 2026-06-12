# First non-repeating character in a string
# def first_unique_char(s):
    
#     char_index_hash = {}
    
#     for i, char in enumerate(s):
#         if char not in char_index_hash:
#             char_index_hash[char] = 1
#             print(char_index_hash)
#         else:
#             char_index_hash[char] += 1
#             print(char_index_hash)
    
#     for i, char in enumerate(s):
#         if char_index_hash[char] == 1:
#             print([char_index_hash[char], i])
#             return i
#     print(-1)
#     return -1

def first_unique_char(s):
    char_index_hash = {}

    for char in s:
        char_index_hash[char] = char_index_hash.get(char, 0) + 1
        #.get(char, 0) looks up the current count for char.
        # If char is not already in the dictionary, it returns 0.
        # Then + 1 increases that count by one.
        # Finally, it stores the new count back into char_index_hash[char].

    for i, char in enumerate(s):
        if char_index_hash[char] == 1:
            return i

    return -1

# return index of 1st char that appears once || return -1 if none

first_unique_char("leetcode")      # 0
first_unique_char("loveleetcode")  # 2
first_unique_char("aabb")          # -1