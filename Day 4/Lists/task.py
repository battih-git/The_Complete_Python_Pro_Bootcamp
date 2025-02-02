# Store the name of US States
states_of_america =[
    "Delaware",	"Pennsylvania",	"New Jersey",	"Georgia",	"Connecticut",	"Massachusetts",
    "Maryland",	"South Carolina",	"New Hampshire",	"Virginia",	"New York",	"North Carolina",
    "Rhode Island",	"Vermont",	"Kentucky",	"Tennessee",	"Ohio",	"Louisiana",	"Indiana",
    "Mississippi",	"Illinois",	"Alabama",	"Maine",	"Missouri",	"Arkansas",	"Michigan",
    "Florida",	"Texas",	"Iowa",	"Wisconsin",	"California",	"Minnesota",	"Oregon",
    "Kansas",	"West Virginia",	"Nevada",	"Nebraska",	"Colorado",	"North Dakota",	"South Dakota",
    "Montana",	"Washington",	"Idaho",	"Wyoming",	"Utah",	"Oklahoma",	"New Mexico",	"Arizona",
    "Alaska",	"Hawaii",
]

# Accessing the element from a list
print(states_of_america[0]) # Positive indexing # First element
print(states_of_america[-1]) # Negative indexing. Last element

# Modifying a data in a list
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# Appending element in list
states_of_america.append("Angealand") # New item is added to end of the list.
print(states_of_america[-1])

# Extending an existing list with another list
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)

