capitals = {
 "France" : "Paris",
 "Germany" : "Berlin"
}

# Nested List in Dictionary
travel_log = {
 "France" : ["Paris","Lille", "Dijon"],
 "Germany" : ["Stuttgart","Berlin"]
}

# Accessing element in nested dictionary & list
print(travel_log["France"][1])

nested_list = ['A','B',['C','D']]
print(nested_list[2][1])

# Nested dictionary: Dictionary inside Dictionary
travel_log = {
    "France":{
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits" : 12
    },
    "Germany":{
        "cities_visited": ["Berlin","Hamburg","Stuttgart"],
        "total_visits" : 5
    }
}

# Accessing element from nested dictionary (Stuttgart)
print(travel_log["Germany"]['cities_visited'][2])