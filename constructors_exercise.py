class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

# Class of "Person" is created with 2 functions (Objects?)
# john = Person("John Smith") instance is created by __init__ and stored in "name"
# john.talk is called which prints the formatted string using the instance name "John Smith"
# this is then printed and repeats for bob
