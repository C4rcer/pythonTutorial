phone = input("Phone: ")  # Store the "phone number" in our case it's just 4 digits
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""  # Output string
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
