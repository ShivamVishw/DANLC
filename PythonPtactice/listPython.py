# A list in Python is a collection of ordered, mutable, and heterogeneous elements.

# Started with python List

myList = []

# basic list
temps = [23, 25, 30, 21]

# MixedList
mixed_list = [1, "hello", 3.14, True]

# NestedList
nested_list = [1, [2, 3], [4, [5, 6]]]

print(myList)
print(mixed_list)
print(nested_list)

# print(nested_list[1,1])
print(nested_list[2][1])
print(nested_list[2][0])

# Slicing
print(nested_list[::2])