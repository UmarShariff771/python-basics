# 1. Given a list of dictionaries, each representing a person with 'name' and 'age' keys,
# use lambda functions to filter out a people under 18
# and then map the remaining people's names to a new list.

people = [
    {"name": "Arjun", "age": 22},
    {"name": "Zara", "age": 17},
    {"name": "Rahul", "age": 25},
    {"name": "Neha", "age": 16},
    {"name": "Kiran", "age": 19},
    {"name": "Sana", "age": 15}
]

# Filter only people whose age is 18 or above
adults = filter(lambda details: details["age"] >= 18, people)

# From the filtered people, extract only the names
adultNames = list(map(lambda person: person["name"], adults ))

# Print final list of adult names
print(adultNames)