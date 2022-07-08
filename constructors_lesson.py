class Point:  # Class naming convention is Pascal (Capitalise start of each word)
    def __init__(self, x, y):  # constructor object "self" is a reference to the current object
        self.x = x  # set x attribute to the x argument passed to the function
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)  # self references this in memory so x becomes 10 and y becomes 20
print(point.x)
