dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dict2 = {
    "d": 4,
    "e": 5,
    "f": 6,
    "b": 2,
    "c": 3
}
dict3 = {
    "g": 7,
    "h": 8,
    "i": 9
}

# Merging dictionaries
dict1.update(dict2)  
dict1.update(dict3)
print("Merged Dictionary:", dict1)
