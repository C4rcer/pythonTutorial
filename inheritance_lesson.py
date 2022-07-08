class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):  # Dog class inherits all the methods in the mammal class
    def bark(self):
        print("Bark")
#    pass  # pass this line python hates empty classes


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()
