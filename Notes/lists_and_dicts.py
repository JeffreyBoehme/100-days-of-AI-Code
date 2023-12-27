# new list and dict
list = []
Dict = {}
dict_name = {"Keyname": "value"}
list_name = []


# getting Dict item value by Key name;
dict_name["KeyName"]

##### Adding Items #####
# Adding a new Dict item value by new Key name
dict_name["NEW_Keyname"] = "the value here"
# Note: must be a new keyname, otherwise updates the old value to the new.

list_name.append("new item")

##### Editing Items #####

# clear a dict
dict_name = {}

# loop through dict - This pulls the Key name NOT the Value as the for object

for key in dict_name:
    print(dict_name[key])  # This would print the value of each key in the dictionary

# Nesting a list in a dict
dict = {
    "dict_key": ["list_item1", "list_item2", "list_item3"],
    "dict_key2": ["list_item1", "list_item2", "list_item3"],
}

# Travel Log as a Dictionary
travel_log = {"France": {"cities_visited": ["Paris", "Lille", "Dijon"]}}

# In the below we are Accessing the Travel Log, Selecting the France Key, Inside the France Item, We are selecting the cities_visited Key, and Inside that item we are selecting the 1st item in the list (REMEMBERING Lists start at 0)
print(travel_log["France"]["cities_visited"][1])

##### SEPERATE NOTES #####
# You can select list items by their placements in the list like [1]
# You CANNOT select dict items by their placements in the dict like [1] and MUST use the Key name
# You can select dict items by their Key name like ["Keyname"] to get the value

##### RANDOM #####
# for random interactons with lists and dicts

### Lists ###
# you can use random.choice(list) to select a random item from a list

### Dicts ###
# you can use random.choice(list(dict.items())) to select a random Item from a dict (the Key and Value)
# you can use random.choice(list(dict.keys())) to select a random Key from a dict
# you can use random.choice(list(dict.values())) to select a random Value from a dict
# You can use list(dict.values()) or just simply [dict.values()] to get a list of all the values in a dict (same for keys) The [] converts the dict to a list on the fly
