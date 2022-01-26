""" Prints info about the users """

users = [
  { 'first_name': 'Rebekah', 'last_name': 'CK', 'user_id': 1 },
  { 'first_name': 'Galata', 'last_name': 'Tona', 'user_id': 2 },  
]

# Print first user's full name
first_user = users[0]
print(f"{first_user['first_name']} {first_user['last_name']}")

# Print last user's full name
last_user = users[-1]
print(f"{last_user['first_name']} {last_user['last_name']}")

