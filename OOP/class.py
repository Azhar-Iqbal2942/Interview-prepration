class Point:

    # Magic Methods
    def __init__(self, x, y, color='red'):
        self.x = x
        self.y = y
        self.__default_color = color  # private Member

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __gt__(self, value):
        return (self.x > value.x) and (self.y > value.y)

    # Getter Setter
    def set_default_color(self, color):
        self.__default_color = color
        return "Operation Successful"

    def get_default_color(self):
        return self.__default_color

    # Decorator for initializing value in constructor
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Points ({self.x} {self.y})")


# this will create object at runtime with values provided in zero method
point = Point.zero()
other = Point(1, 5)

print(point.__dict__)  # to get compete overview of object

point.set_default_color("Blue")
print(point.get_default_color())
print(other._Point__default_color)
