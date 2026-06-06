band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Accessing Items

print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value paris as tuples
print(band.items())
# dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

# verify key exists -> returns boolean
print("guitar" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
# pop returns what is removed
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # returns a tuple
print(band)

# delete and clear
band["drums"] = "Bonham"
print(band)

del band["drums"] # deletes item
print(band)

band2.clear() # empties dict
print(band2)

del band2 # deletes whole dictionary

# copy dictionaries
# band2 = band X creates reference not a new copy X

band2 = band.copy()
band3 = dict(band)

# Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])