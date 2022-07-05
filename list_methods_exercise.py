numbers = [5, 2, 1, 7, 4, 4, 2, 10]  # List
uniques = []  # New list to store numbers
for number in numbers:  # for each number in numbers
    if number not in uniques:  # if number is not already in uniques
        uniques.append(number)  # Append the number into uniques
print(uniques)
