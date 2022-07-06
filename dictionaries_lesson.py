customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])  # this returns the value of the key name
print(customer.get("birthday"))  # doesn't throw error for missing key
customer["birthdate"] = "Jan 1 1980"  # you can add key values here
# Dictionary and key values can be strings bools lists anything
