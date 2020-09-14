

def greetings(name):
    print(f"Hello {name}")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


result = multiply(3, 4, 5)


def save_user(**user):
    return "Save Successfully"


save_user(id=1, name="Azhar", degree="Computer Science")


# Fizz_buzz quiz app
def fizz_buzz(input):
    if(input % 3 == 0 and input % 5 == 0):
        print("Fizz Buzz")
    elif(input % 3 == 0):
        print("Fizz")
    elif(input % 5 == 0):
        print("Buzz")
    else:
        print(input)


fizz_buzz(7)
