# we use classes to define new types
# Numbers
# Strings
# Booleans
# ---
# Lists
# Dictionaries
class Point:  # Class are named differently
    def move(self):
        print("move")

    def draw(self):  # template for an object
        print("draw")


point1 = Point()  # creates new object and returns, it's now stored in point1
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
