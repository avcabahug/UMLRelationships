# Inheritance (Is-a)

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(self.name + " says Woof!")

# Run
my_dog = Dog("Buddy")
my_dog.bark()
