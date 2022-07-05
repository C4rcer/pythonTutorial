matrix = [  # 2d list each data science and machine learning.
    [1, 2, 3],  # 3 by 3 matrix each item in this list is another list (here it's a list with 3 more lists or 3 items).
    [4, 5, 6],  # You must use , to denote that each item is a new item
    [7, 8, 9]
]
for row in matrix:  # iterate over the matrix list each row is 1 list so iterate 3 times
    for item in row:  # for each item in a row
        print(item)  # print the item
# matrix[0][1] = 20  # we can change what's in the matrix too
# print(matrix[0][1])   # returns the inner list 0 being the "main" list and 1 being the 2nd item (computers start at 0)
