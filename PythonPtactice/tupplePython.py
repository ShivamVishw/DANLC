# A tuple is an immutable, ordered collection of elements in Python. 
# Unlike lists, tuples cannot be modified after creation, 
# Meaning that you cannot change, add, or remove elements once they are defined.

my_tupple = (1, 1, 3,4,5,6,7)
print(my_tupple)
print(my_tupple[0])
print(my_tupple[2])
print(my_tupple[1::])
print(my_tupple[::3])  #moving by twice or thrice


# Tuples are indexed, ordered, and can store multiple data types.

# This is a tuple with one element
single_element_tuple = (1,)  
# This is just an integer, not a tuple
not_a_tuple = (1)  


tuple_1 = (1,2)
tuple_2 = (3,4)
Final_tuple = tuple_1+ tuple_2
print(Final_tuple)

# Unpacking the values into indivual integer
a,b,c,d,e,f,g= my_tupple
print(a,b,c,d,e,f,g)

print(my_tupple.count(1)) #It will print number of frequency of particular elements available in tupple
print(my_tupple.index(7))



# Now let's see Tupple as a dictionary working 
tuple_as_dic = {('a', 'b'): 1, ('x', 'y'): 2}
print(tuple_as_dic[('a', 'b')])
print(tuple_as_dic[('x', 'y')])


# Tuples vs Lists
# Immutability: Tuples are immutable, whereas lists are mutable.
# Performance: Tuples are faster and use less memory than lists.
# Usage: Tuples are ideal for data that should not be modified, while lists are better when you need to add, remove, or change elements frequently.
