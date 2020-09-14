# Mainly there are 2 types of loop in Python
# >>>>>> While Loop
# >>>>>> for Loop

# Keywords
# >>>> continue
# >>>> break
# >>>> pass

################### While Loop ###########

count = 0
while count <= 9:
    print("Count Value is", count)
    count += 1
else:
    print("Value of count exceeds limit")

################### for Loop ###########
# >>>>>> Example 1

random_list = [1, 2, 'azhar', 23.6]
for item in range(len(random_list)):
    print(item)

# >>>> Example 2

# finding prime number
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print(f"{num} equals {i} * {int(j)}")
            break
    else:
        print(f"{num} is a prime number")
