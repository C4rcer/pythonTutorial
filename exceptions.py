try:  # Try running this code
    age = int(input("Age: "))
    income = 27000
    risk = income / age
    print(age)
except ZeroDivisionError:  # exception if division by zero then print below
    print("Age cannot be 0.")
except ValueError:  # instead of crashing print this if it's a value error
    print("Invalid value")

