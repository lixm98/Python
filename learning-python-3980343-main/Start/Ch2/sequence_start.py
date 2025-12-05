# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
myList = [0, 1, "two", 3.2, False]
print(len(myList))

# to access a member of a sequence type, use []
print(myList[2])
print(myList[-1])
myList[0] = 10
print(myList)

# add a list to another list
another_List = [6, 7, 8]
myList = myList + another_List
print(myList)
# string is a list but immutable
myStr = "This is a string"
print(myStr[0], myStr[2], myStr[3])

# use slices to get parts of a sequence
print(myList[1:4:2])
print(myList[::2])


# you can use slices to reverse a sequence
print(myList[::-1])

# Tuples are like lists, but they are immutable
myTuple = (0, 1, 2, "three")
print(myTuple[1])

# Sets are also sequences, but they contain unique values（重复的值会被过滤）
mySet = {1, 2, 3, 2, 4, "hey"}
print(mySet)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in myList)
print(3 in myTuple)
print(5 in mySet)