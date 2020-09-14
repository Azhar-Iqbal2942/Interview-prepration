# Two ways to create getter setter methods in python
# Method 1: More of Java style code
# Method 2: More of Pythonic way usng Decorator


# Method 1
class ProductJava:
    def __init__(self, price):
        self.price = price

    def __get_price(self):
        print("Getting Value using decorator")
        return self.__price

    def __set_price(self, value):
        print("Setting Value using decorator")
        if value < 0:
            raise ValueError("Price Cannot be Negative")
        self.__price = value

    price = property(__get_price, __set_price)


# Method 2
# Using @property decorator
class ProductPython:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        print("Getting ...")
        return self.__price

    # if you want only getter you can remove this code
    @price.setter
    def price(self, value):
        print("Setter ... ")
        if value < 0:
            raise ValueError("Price cannot be Negative")
        self.__price = value
