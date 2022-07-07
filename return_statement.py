def square(number):
    return number * number  # returns the value to a caller of this function


# No return results in a None value which is default

result = square(3)  # Passes the value 3 to the square function and stores it in result
print(result)

print(square(3))  # Works the same as above but shortens the code needed
