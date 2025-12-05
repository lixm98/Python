# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
myDict = {
  "one" : 1,
  "two" : 2,
  3 : "three",
  4.5 : ["four", "point", "five"]
  }
print(myDict)
# dictionaries are accessed via keys
print(myDict["one"])
print(myDict[3])

# you can also set dictionary data by creating a new key
myDict["seven"] = 7
print(myDict)

# Trying to access a nonexistent key will produce an error


# To avoid this, you can use the "in" operator to see if a key exists
print("two" in myDict)
print("blarg" in myDict)

# You can retrieve all of the keys and values from a dictionary
print(myDict.keys())
print(myDict.values())

# You can also iterate over all the items in a dictionary
for key, val in myDict.items():
  print(key, val)