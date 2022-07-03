numbers = [5, 2, 5, 2, 2]
for x_count in numbers:  # set x_count to store the number
    output = ""  # Set empty string
    for count in range(x_count):  # Using range function
        output += "x"  # Add as many x's from numbers to output
    print(output)  # Print output
