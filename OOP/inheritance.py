class Animal:
    def __init__(self, age=1):
        self.age = age

    def eat(self):
        print('eat')

# Animal: Parent, base class
# Mamal: child, sub class


class Mamal(Animal):
    def walk(self):
        print('walk')


m = Mamal(23)
a = Animal()
print(isinstance(a, Mamal))
print(issubclass(Animal, object))
