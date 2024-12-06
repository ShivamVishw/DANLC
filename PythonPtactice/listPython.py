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
# from start
print(nested_list[::2]) 
# from end to start(specific index)
print(nested_list[2::])


# Appending or Adding
myList.append(25)
myList.append(43)
myList.append(90)
print(myList)

# Chainging Lists(Updating)
myList[1]= -32
print(myList)

# Removing Element by remove or pop methods
# myList.remove(-32)
# if -32 in myList:
#     myList.remove(-32)
# else:
#     print("Not found")
# myList.pop()
print(myList)


# Lets find fo squares
# n= int(input())
# squares= [i**n for i in range(1,10)]
# print(squares)


nums= [4,23,6,2,1]
print(nums)
# sort methods
nums.sort()
print(nums)

# Zipping learn()
names = ["Alice", "Bob"]
ages = [25, 30]
zipped = zip(names, ages)
print(list(zipped))

# Ooposite to ziping i.e extracting
names_ages = [("Alice", 2),("Bob", 3)]
names, ages = zip(*names_ages)
print(names)
print(ages)

# Advantages:
# It can store data dynamically
# It can store different data type
# Has various inbuilt methods also
# Good for searchin sorting in sorted dataset not large unsorted dataset
    
# DisAdvantages:
# Slower copare to tupple for large data operations
# It uses more memory due to dynamic memory allocation 


