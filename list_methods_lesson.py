numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()  # This list will copy and if printed will have the original numbers in the list.
# numbers.clear()  # Clears the list
# numbers.pop()  # removes all the values
numbers.remove(5)  # this will remove the designated number (5 in this case)
numbers.insert(0, 10)  # 1st number is index 2nd number is the inserted value
numbers.append(20)  # Append method, will append to the end of a list
print(numbers.index(7))  # Prints the index of a specified value so for 7 this is the first instance of the value
# it's at index 3 (0,1,2,3)
print(numbers)
print(50 in numbers)  # we are checking for the existence of 50 in this list of numbers
print(numbers.count(5))  # Will check how many of a value are in the list
print(numbers.sort())   # Will sort numbers in ascending items .reverse will do it backwards

