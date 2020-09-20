# O(n)
def factorial(number):
    # base case
    if number == 0:
        return 1

    # recursive part
    return number * factorial(number - 1)


"""
-> Given a number N return the index value of the fibonacci series
for example fibonacci(8) return 21 (0,1,1,2,3,5,8,13,21, ...)

 O(2^n) Exponential -Recursive alogorithms that solve a problem of size N.
 
"""


def fibonacci(number):
   # base case
    if number < 2:
        return number

    # recursive case
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(40))
