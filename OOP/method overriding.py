class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mamal(Animal):
    def __init__(self):
        super().__init__()  # method overriding
        self.weight = 2

    def walk(self):
        print("walk")


m = Mamal()
print(m.age)
print(m.weight)
