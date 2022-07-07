# function is a container for a few lines of code that do a specific task
def greet_user(first_name, last_name):  # Meaningful name, these are parameters, you must pass arguments to these
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


# Need two line breaks
print("Start")
greet_user("John", last_name="Smith")  # keyword argument comes 2nd never first
# calc_cost(total=50, shipping=5, discount=0.1)  # keyword arguments are good for readability
greet_user("Mary", "Poppins")  # Mary is an argument that we pass top the name parameter of the greet_user function
print("Finish")
