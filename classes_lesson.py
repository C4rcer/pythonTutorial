# we use classes to define new types
# Numbers
# Strings
# Booleans
# ---
# Lists
# Dictionaries
class Point:  # Class naming convention is Pascal (Capitalise start of each word)
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()  # creates new object which is an instance of a class (blueprint)
point1.x = 10  # Attribute set
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()  # New object is not the same as point1 but is still an instance of the point class
point2.x = 1
print(point2.x)
