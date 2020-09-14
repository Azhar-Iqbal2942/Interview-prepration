# List
sample_list = [1, 2, "Azhar", 23.5]

# Operation on list
x = sample_list[0]  # Accessing value from list
sample_list[1] = 50  # Updating value in list
del sample_list[1]  # Deleting value in list
ret = sample_list.index(23.5)

# Special function
length = sample_list.__len__()  # Return length of list


# Tuple (Immutable data structure)
sample_tuple = (1, 2, 'Azhar', 23.5)

# Operation in Tuple
tup_val = sample_tuple[0]  # getting first value in tuple
new_tup = tuple(sample_list)  # Converting list into tupe


# Dictionary
sample_dict = {'name': 'Azhar', 'age': 23, 'degree': "Computer Science"}

# Operation on Dictionary
val = sample_dict['name']   # getting value from dictionary
sample_dict['name'] = "Nabeel"  # Updating value in dictionary
del sample_dict['name']  # deleting key:value pair in dictionary


# Drive Code
# print(sample_dict['name'])
